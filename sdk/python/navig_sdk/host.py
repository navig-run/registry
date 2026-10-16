"""The host seam: navig's own implementation when navig is installed, a faithful copy when not.

A first-party plugin is meant to work in two places: as ``navig <verb>`` inside navig, and as
its own ``navig-<name>`` command with no navig installed at all. Everything such a plugin
needs from navig's core (where state lives, crash-safe writes, JSON reads, subprocess text)
goes through this one module instead of ``navig.*``, so a single import line decides nothing.

**Delegate first, always.** Every function tries navig and only falls back when navig is not
importable. In a navig install the fallback never runs, so the two cannot disagree there; and
the fallbacks that decide *where data lives* are compared against navig's own resolvers across
an environment matrix by ``core/tests/quality/test_plugin_compat_path_parity.py``. A path
fallback that drifts would make a standalone plugin read and write a directory navig never
looks at, silently, which is the whole reason it is tested by calling both and comparing.

Every fallback is its own ``_*_fallback`` function so tests can call it directly, without
evicting navig from ``sys.modules`` (an eviction outlives the test and breaks later ones).

Standard library only: this module adds nothing to a plugin's install.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any

__all__ = [
    "atomic_write_text",
    "cache_dir",
    "coerce_bool",
    "command_name",
    "config_dir",
    "data_dir",
    "decode_console_result",
    "log_dir",
    "media_dir",
    "navig_available",
    "run_text",
    "safe_json_loads",
    "set_owner_only_file_permissions",
]

# Mirrors navig.core.yaml_io's replace retry policy (a Windows antivirus or backup agent can
# hold the destination for a moment; navig's writer retries that, so this one does too).
_ATOMIC_REPLACE_RETRIES = 3
_ATOMIC_REPLACE_BACKOFF_BASE = 0.05


def navig_available() -> bool:
    """Is navig importable here? Plugins use it to word a "needs navig" message."""
    try:
        import navig  # noqa: F401, PLC0415

        return True
    except ImportError:
        return False


def command_name(verb: str, standalone: str | None = None) -> str:
    """The command a user types for this plugin HERE: ``navig <verb>`` or ``navig-<verb>``.

    Advice like "run `navig explore probe` first" names a command that does not exist when
    navig is not installed. Build it from this instead: ``f"{command_name('explore')} probe"``.
    Pass *standalone* when the console script is not ``navig-<verb>`` (navig-msstore's verb
    is ``mstore``).
    """
    return f"navig {verb}" if navig_available() else (standalone or f"navig-{verb}")


# ── where things live ────────────────────────────────────────────────────────


def _current_os() -> str:
    """Mirror of ``navig.platform.paths.current_os`` (without its process-wide cache)."""
    p = sys.platform
    if p == "win32":
        return "windows"
    if p == "darwin":
        return "macos"
    if p == "linux":
        try:
            text = Path("/proc/version").read_text(encoding="utf-8", errors="replace")
        except OSError:
            return "linux"
        return "wsl" if "microsoft" in text.lower() else "linux"
    return "linux"


def _is_system_service_fallback() -> bool:
    """Mirror of ``navig.platform.paths._is_system_service`` — all three legs.

    Dropping them is not hypothetical: a root-run service that skips this resolves
    ``/root/.navig`` instead of ``/etc/navig`` and opens a different, empty state dir.
    """
    if os.environ.get("NAVIG_SYSTEM_SERVICE") == "1":
        return True
    if _current_os() not in ("linux", "macos", "wsl"):
        return False
    try:
        import pwd  # noqa: PLC0415

        # The legacy system deploy runs as a SYSTEM account named navig. A PERSON named
        # navig (uid >= 1000, home under /home) is not a system install: treating it as one
        # moved their config to /etc/navig and the daemon crash-looped on a real Debian VM.
        entry = pwd.getpwuid(os.getuid())  # type: ignore[attr-defined]
        if entry.pw_name == "navig" and (
            entry.pw_uid < 1000 or not entry.pw_dir.startswith("/home/")
        ):
            return True
    except (ImportError, KeyError):
        pass
    if os.environ.get("INVOCATION_ID"):
        try:
            if os.getuid() == 0:  # type: ignore[attr-defined]
                return True
        except AttributeError:
            pass
    return False


def config_dir() -> Path:
    """navig's config dir (``~/.navig``), resolved the same way with or without navig."""
    try:
        from navig.platform.paths import config_dir as _impl  # noqa: PLC0415
    except ImportError:
        return _config_dir_fallback()
    return _impl()


def _config_dir_fallback() -> Path:
    env = os.environ.get("NAVIG_CONFIG_DIR")
    if env:
        return Path(env)
    if _is_system_service_fallback():
        return Path("/etc/navig")
    return Path.home() / ".navig"


def data_dir() -> Path:
    """Databases and state (``~/.navig/data``)."""
    try:
        from navig.platform.paths import data_dir as _impl  # noqa: PLC0415
    except ImportError:
        return _data_dir_fallback()
    return _impl()


def _data_dir_fallback() -> Path:
    env = os.environ.get("NAVIG_DATA_DIR")
    if env:
        return Path(env)
    if _is_system_service_fallback():
        # NOT config_dir()/data: under a service it is its own FHS location.
        return Path("/var/lib/navig")
    return _config_dir_fallback() / "data"


def media_dir(kind: str) -> Path:
    """Where generated media of *kind* lives (``images``, ``videos``, ``audio``…).

    ``<data dir>/<kind>``; without an explicit ``NAVIG_DATA_DIR`` an existing legacy
    ``<config dir>/<kind>`` is kept so media made by older builds is never orphaned.
    """
    try:
        from navig.platform.paths import media_dir as _impl  # noqa: PLC0415
    except ImportError:
        return _media_dir_fallback(kind)
    return _impl(kind)


def _media_dir_fallback(kind: str) -> Path:
    new_path = _data_dir_fallback() / kind
    if not os.environ.get("NAVIG_DATA_DIR"):
        legacy = _config_dir_fallback() / kind
        if not new_path.exists() and legacy.exists():
            return legacy
    return new_path


def cache_dir() -> Path:
    """Disposable caches (OS-idiomatic: ``%LOCALAPPDATA%\\navig\\cache``, ``~/.cache/navig``…)."""
    try:
        from navig.platform.paths import cache_dir as _impl  # noqa: PLC0415
    except ImportError:
        return _cache_dir_fallback()
    return _impl()


def _cache_dir_fallback() -> Path:
    env = os.environ.get("NAVIG_CACHE_DIR")
    if env:
        return Path(env)
    if _is_system_service_fallback():
        return Path("/var/cache/navig")
    os_name = _current_os()
    if os_name == "windows":
        local = os.environ.get("LOCALAPPDATA")
        return Path(local) / "navig" / "cache" if local else _config_dir_fallback() / "cache"
    if os_name == "macos":
        return Path.home() / "Library" / "Caches" / "navig"
    xdg = os.environ.get("XDG_CACHE_HOME")
    return Path(xdg) / "navig" if xdg else Path.home() / ".cache" / "navig"


def log_dir() -> Path:
    """Logs (OS-idiomatic: ``%LOCALAPPDATA%\\navig\\logs``, ``~/.local/state/navig/logs``…)."""
    try:
        from navig.platform.paths import log_dir as _impl  # noqa: PLC0415
    except ImportError:
        return _log_dir_fallback()
    return _impl()


def _log_dir_fallback() -> Path:
    env = os.environ.get("NAVIG_LOG_DIR")
    if env:
        return Path(env)
    if _is_system_service_fallback():
        return Path("/var/log/navig")
    os_name = _current_os()
    if os_name == "windows":
        local = os.environ.get("LOCALAPPDATA")
        return Path(local) / "navig" / "logs" if local else _config_dir_fallback() / "logs"
    if os_name == "macos":
        return Path.home() / "Library" / "Logs" / "navig"
    xdg = os.environ.get("XDG_STATE_HOME")
    return Path(xdg) / "navig" / "logs" if xdg else Path.home() / ".local" / "state" / "navig" / "logs"


# ── config values ────────────────────────────────────────────────────────────

# Mirrors navig.core.coerce; core's test suite compares every token against navig's.
_TRUE_TOKENS = frozenset({"1", "true", "yes", "on", "t", "y"})
_FALSE_TOKENS = frozenset({"0", "false", "no", "off", "f", "n", ""})


def coerce_bool(value: Any, default: bool = False) -> bool:
    """A config value as a bool. ``navig config set x false`` stores the STRING "false".

    navig's canonical ``navig.core.coerce.coerce_bool`` when installed; the same truth table
    otherwise. Unknown tokens return *default* — never a silent ``True``.
    """
    try:
        from navig.core.coerce import coerce_bool as _impl  # noqa: PLC0415
    except ImportError:
        return _coerce_bool_fallback(value, default)
    return _impl(value, default=default)


def _coerce_bool_fallback(value: Any, default: bool = False) -> bool:
    if isinstance(value, bool):
        return value
    if value is None:
        return default
    if isinstance(value, (int, float)):
        return bool(value)
    token = str(value).strip().lower()
    if token in _TRUE_TOKENS:
        return True
    if token in _FALSE_TOKENS:
        return False
    return default


# ── files and text ───────────────────────────────────────────────────────────


def set_owner_only_file_permissions(path: str | Path) -> None:
    """Owner-only access to a file holding a secret (a token, a cookie jar). Never raises.

    navig's own implementation when installed; otherwise the standalone copy navig-vault
    keeps, which core's test suite pins byte-for-byte against navig's (it guards the vault
    database, so it is the one copy that is already held to that standard).
    """
    try:
        from navig.core.file_permissions import set_owner_only_file_permissions as _impl  # noqa: PLC0415
    except ImportError:
        try:
            from navig_vault._compat import _set_owner_only_fallback as _impl  # noqa: PLC0415
        except ImportError:
            _impl = _owner_only_minimal
    _impl(path)


def _owner_only_minimal(path: str | Path) -> None:
    """Last resort with neither navig nor navig-vault installed: POSIX mode 0600.

    On Windows a file under the user profile already inherits the profile's ACL (the owner,
    SYSTEM and Administrators); the icacls hardening lives in navig / navig-vault.
    """
    if os.name != "nt":
        try:
            os.chmod(path, 0o600)
        except OSError:
            pass


def atomic_write_text(path: Path | str, content: str, *, encoding: str = "utf-8") -> None:
    """Crash-safe text write: a temp file in the same directory, then an atomic replace."""
    try:
        from navig.core.yaml_io import atomic_write_text as _impl  # noqa: PLC0415
    except ImportError:
        _atomic_write_fallback(path, content, encoding=encoding)
        return
    _impl(path, content, encoding=encoding)


def _atomic_write_fallback(path: Path | str, content: str, *, encoding: str = "utf-8") -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    for attempt in range(_ATOMIC_REPLACE_RETRIES):
        fd, tmp_name = tempfile.mkstemp(dir=p.parent, prefix=f".{p.name}.tmp", suffix=".navig~")
        try:
            with os.fdopen(fd, "w", encoding=encoding) as fh:
                fh.write(content)
                fh.flush()
                os.fsync(fh.fileno())
            os.replace(tmp_name, p)
            return
        except PermissionError:
            try:
                os.unlink(tmp_name)
            except OSError:
                pass
            # Only Windows' transient sharing lock is worth retrying; on POSIX a
            # PermissionError is a real permission problem.
            if attempt == _ATOMIC_REPLACE_RETRIES - 1 or sys.platform != "win32":
                raise
            time.sleep(_ATOMIC_REPLACE_BACKOFF_BASE * (attempt + 1))
        except BaseException:
            try:
                os.unlink(tmp_name)
            except OSError:
                pass
            raise


def safe_json_loads(raw: object, default: Any) -> Any:
    """Parse a stored JSON blob; NULL, empty or malformed reads as *default* (never written back)."""
    try:
        from navig.core.json_io import safe_json_loads as _impl  # noqa: PLC0415
    except ImportError:
        return _safe_json_loads_fallback(raw, default)
    return _impl(raw, default)


def _safe_json_loads_fallback(raw: object, default: Any) -> Any:
    if not raw:
        return default
    try:
        return json.loads(raw)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return default


def run_text(
    args: list[str],
    *,
    timeout: float | None = None,
    cwd: str | Path | None = None,
    env: dict[str, str] | None = None,
    input: str | None = None,  # noqa: A002 - mirrors subprocess.run
) -> subprocess.CompletedProcess[str]:
    """Run a command and return its output as text that never fails to decode.

    ``subprocess.run(text=True)`` decodes with the locale code page, and a tool that writes
    UTF-8 (or a localised Windows tool writing the OEM page) raises inside subprocess's reader
    thread — the call returns and the traceback lands on a thread nobody watches. So this
    captures BYTES and decodes them the way navig does: UTF-8 first, then the console code
    page, never raising.
    """
    no_window = getattr(subprocess, "CREATE_NO_WINDOW", 0) if sys.platform == "win32" else 0
    proc = subprocess.run(
        args,
        capture_output=True,
        timeout=timeout,
        cwd=cwd,
        env=env,
        input=input.encode("utf-8") if input is not None else None,
        check=False,
        creationflags=no_window,
    )
    return subprocess.CompletedProcess(
        proc.args, proc.returncode, _decode(proc.stdout), _decode(proc.stderr)
    )


def decode_console_result(result: Any) -> subprocess.CompletedProcess[str]:
    """A ``CompletedProcess`` captured in BYTES, with its streams decoded to ``str``.

    navig's own ``navig.core.proc_text.decode_console_result`` when installed (UTF-8 first,
    then the console code page — git writes UTF-8, a localised Windows tool writes cp866);
    the same two-step decode otherwise. Duck-typed like navig's: a test double without
    ``args``/``stdout`` decodes to "" rather than raising.
    """
    try:
        from navig.core.proc_text import decode_console_result as _impl  # noqa: PLC0415
    except ImportError:
        return subprocess.CompletedProcess(
            getattr(result, "args", None),
            getattr(result, "returncode", 0),
            _decode(getattr(result, "stdout", None)),
            _decode(getattr(result, "stderr", None)),
        )
    return _impl(result)


def _decode(data: bytes | str | None) -> str:
    if not data:
        return ""
    if isinstance(data, str):  # already text (a caller ran with text=True)
        return data
    try:
        from navig.core.proc_text import decode_console_output  # noqa: PLC0415
    except ImportError:
        pass
    else:
        try:
            return decode_console_output(data)
        except Exception:  # noqa: BLE001 - fall through to the local decode
            pass
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        pass
    if sys.platform == "win32":
        import ctypes  # noqa: PLC0415

        try:
            cp = ctypes.windll.kernel32.GetConsoleOutputCP() or ctypes.windll.kernel32.GetOEMCP()
            return data.decode(f"cp{cp}", errors="replace")
        except (AttributeError, LookupError, OSError):
            pass
    return data.decode("utf-8", errors="replace")
