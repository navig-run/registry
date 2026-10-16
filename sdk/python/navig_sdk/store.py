"""A plugin's SQLite store, the same file whether navig is installed or not.

    from navig_sdk.store import BaseStore

    class MyStore(BaseStore):
        SCHEMA_VERSION = 1
        def _create_schema(self, conn): conn.executescript("CREATE TABLE IF NOT EXISTS …")

Inside navig, :data:`BaseStore` IS ``navig.store.base.BaseStore`` — navig's storage engine
(shared thread-local connections, per-database write locks, its PRAGMA profiles). Without
navig it is a faithful standalone class with the same API and, crucially, the same on-disk
contract: the same ``schema_version`` table, the same stamp-then-migrate order, and navig's
default connection profile for a database it does not know (WAL, ``synchronous=NORMAL``,
5 s busy timeout, ``sqlite3.Row`` rows). A database written by either side opens in the other
— a user who starts with the standalone plugin and later installs navig keeps their data.
"""

from __future__ import annotations

import sqlite3
import threading
from pathlib import Path
from typing import Any

__all__ = ["BaseStore", "utcnow"]


def utcnow() -> str:
    """The ISO-8601 UTC timestamp navig's stores write (``2026-09-29T12:00:00.000000Z``)."""
    try:
        from navig.store.base import _utcnow  # noqa: PLC0415
    except ImportError:
        from datetime import datetime, timezone  # noqa: PLC0415

        return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    return _utcnow()

try:
    from navig.store.base import BaseStore  # noqa: PLC0415
except ImportError:

    class _Engine:
        """The slice of navig's storage engine a store needs: connections and write locks."""

        _PRAGMAS = {"journal_mode": "WAL", "synchronous": "NORMAL", "busy_timeout": 5000}

        def __init__(self) -> None:
            self._local = threading.local()
            self._locks: dict[str, threading.Lock] = {}
            self._meta = threading.Lock()

        def connect(self, db_path: Path) -> sqlite3.Connection:
            conns = self._local.__dict__.setdefault("conns", {})
            key = str(db_path)
            conn = conns.get(key)
            if conn is None:
                db_path.parent.mkdir(parents=True, exist_ok=True)
                conn = sqlite3.connect(key, check_same_thread=False)
                conn.row_factory = sqlite3.Row
                for pragma, value in self._PRAGMAS.items():
                    try:
                        conn.execute(f"PRAGMA {pragma}={value}")
                    except sqlite3.OperationalError:
                        pass
                conns[key] = conn
            return conn

        def write_lock(self, db_path: Path) -> threading.Lock:
            with self._meta:
                return self._locks.setdefault(str(db_path), threading.Lock())

        def close(self, db_path: Path) -> None:
            conn = self._local.__dict__.get("conns", {}).pop(str(db_path), None)
            if conn is not None:
                conn.close()

    _ENGINE = _Engine()

    class BaseStore:  # type: ignore[no-redef]
        """Standalone twin of ``navig.store.base.BaseStore`` (same API, same file format)."""

        SCHEMA_VERSION: int = 1
        PRAGMAS: dict[str, Any] = {}

        def __init__(self, db_path: Path, *, engine: Any = None) -> None:
            self.db_path = Path(db_path)
            self._engine = engine or _ENGINE
            self._lock = self._engine.write_lock(self.db_path)
            self.db_path.parent.mkdir(parents=True, exist_ok=True)
            self._init_schema()

        def _get_conn(self) -> sqlite3.Connection:
            conn = self._engine.connect(self.db_path)
            for pragma, value in dict(self.PRAGMAS).items():
                if pragma == "mmap_size":
                    continue  # unreliable with WAL on Windows; navig drops it there too
                try:
                    conn.execute(f"PRAGMA {pragma}={value}")
                except sqlite3.OperationalError:
                    pass
            return conn

        def _init_schema(self) -> None:
            conn = self._get_conn()
            conn.execute("CREATE TABLE IF NOT EXISTS schema_version (version INTEGER PRIMARY KEY)")
            self._create_schema(conn)
            row = conn.execute("SELECT version FROM schema_version LIMIT 1").fetchone()
            current = row[0] if row else 0
            if current == 0:
                conn.execute(
                    "INSERT OR REPLACE INTO schema_version (version) VALUES (?)", (self.SCHEMA_VERSION,)
                )
                conn.commit()
            elif current < self.SCHEMA_VERSION:
                self._migrate(conn, current, self.SCHEMA_VERSION)
                conn.execute("UPDATE schema_version SET version = ?", (self.SCHEMA_VERSION,))
                conn.commit()

        def _create_schema(self, conn: sqlite3.Connection) -> None:
            raise NotImplementedError

        def _migrate(self, conn: sqlite3.Connection, from_version: int, to_version: int) -> None:
            """Subclass SHOULD override: incremental schema migrations."""

        def _write(self, sql: str, params: tuple | None = None) -> sqlite3.Cursor:
            with self._lock:
                conn = self._get_conn()
                old = conn.isolation_level
                try:
                    conn.isolation_level = None
                    conn.execute("BEGIN IMMEDIATE")
                    cursor = conn.execute(sql, params or ())
                    conn.execute("COMMIT")
                    return cursor
                except Exception:
                    try:
                        conn.execute("ROLLBACK")
                    except Exception:  # noqa: BLE001
                        pass
                    raise
                finally:
                    conn.isolation_level = old

        def _write_many(self, sql: str, seq_of_params: list[tuple]) -> int:
            if not seq_of_params:
                return 0
            with self._lock:
                conn = self._get_conn()
                old = conn.isolation_level
                try:
                    conn.isolation_level = None
                    conn.execute("BEGIN IMMEDIATE")
                    conn.executemany(sql, seq_of_params)
                    conn.execute("COMMIT")
                    return len(seq_of_params)
                except Exception:
                    try:
                        conn.execute("ROLLBACK")
                    except Exception:  # noqa: BLE001
                        pass
                    raise
                finally:
                    conn.isolation_level = old

        def _write_script(self, sql: str) -> None:
            with self._lock:
                self._get_conn().executescript(sql)

        def _read_one(self, sql: str, params: tuple | None = None) -> sqlite3.Row | None:
            return self._get_conn().execute(sql, params or ()).fetchone()

        def _read_all(self, sql: str, params: tuple | None = None) -> list[sqlite3.Row]:
            return self._get_conn().execute(sql, params or ()).fetchall()

        def maintenance(self) -> dict[str, Any]:
            self._get_conn().execute("PRAGMA optimize")
            return {"optimized": True}

        def backup(self, dest: Path) -> Path:
            dest = Path(dest)
            dest.parent.mkdir(parents=True, exist_ok=True)
            with self._lock:
                target = sqlite3.connect(str(dest))
                try:
                    self._get_conn().backup(target)
                finally:
                    target.close()
            return dest

        def close(self) -> None:
            self._engine.close(self.db_path)

        def get_schema_version(self) -> int:
            row = self._read_one("SELECT version FROM schema_version LIMIT 1")
            return row[0] if row else 0

        def __repr__(self) -> str:
            return f"{type(self).__name__}({str(self.db_path)!r})"

