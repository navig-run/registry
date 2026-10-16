"""Read-modify-write for a plugin's JSON and YAML files, without ever wiping one.

The rule these exist to enforce: **a failed read must never become a destructive write.**
Reading a store with ``json.loads(path.read_text()) if path.exists() else {}`` and saving
the result back destroys every record the moment a read fails transiently (an antivirus or
backup agent holding the file, a read landing mid-``os.replace``), because "unreadable"
collapses into "empty". navig lost its whole config that way, twice in one night.

So, the same contract as navig's own ``navig.core.json_io`` / ``yaml_io``:

* absent or genuinely empty → a fresh copy of *default*;
* present WITH content but unreadable after retries → :class:`JsonReadError` /
  :class:`ConfigReadError`, so the caller ABORTS instead of writing a blank over real data;
* present but corrupt → JSON: the bytes are kept beside it as ``*.corrupt`` and *default*
  returned; YAML: :class:`ConfigReadError`.

Inside navig every function IS navig's, and the two error classes ARE navig's classes, so an
``except JsonReadError`` written against this module catches what navig raises. Without navig
they are faithful standalone copies. YAML needs PyYAML, imported only when a YAML function
is called; a plugin that uses them declares ``pyyaml``.
"""

from __future__ import annotations

import copy
import json
import os
import sys
import tempfile
import time
from pathlib import Path
from typing import Any

from navig_sdk.host import atomic_write_text

__all__ = [
    "ConfigReadError",
    "JsonReadError",
    "atomic_write_json",
    "atomic_write_yaml",
    "load_json_for_update",
    "load_json_safe",
    "load_yaml_for_update",
    "read_text_retrying",
    "safe_load_yaml",
]

_RETRIES = 3
_BACKOFF = 0.05

# The error classes must be navig's own when navig is present, or a plugin's `except`
# would miss the error navig's implementation raises. Guarded, so this never requires navig.
try:
    from navig.core.yaml_io import ConfigReadError  # noqa: PLC0415
except ImportError:

    class ConfigReadError(RuntimeError):  # type: ignore[no-redef]
        """A file exists WITH content but could not be read or parsed — do not overwrite it."""


try:
    from navig.core.json_io import JsonReadError  # noqa: PLC0415
except ImportError:

    class JsonReadError(ConfigReadError):  # type: ignore[no-redef]
        """A JSON store could not be read (a lock that outlived the retries) — do not overwrite it."""


def read_text_retrying(path: Path | str, *, encoding: str = "utf-8") -> str:
    """Read text, riding out transient OS locks; raises ``OSError`` if they persist."""
    try:
        from navig.core.yaml_io import read_text_retrying as _impl  # noqa: PLC0415
    except ImportError:
        return _read_text_retrying_fallback(path, encoding=encoding)
    return _impl(path, encoding=encoding)


def _read_text_retrying_fallback(path: Path | str, *, encoding: str = "utf-8") -> str:
    fp = Path(path)
    last: OSError | None = None
    for attempt in range(_RETRIES):
        try:
            return fp.read_text(encoding=encoding)
        except OSError as exc:
            last = exc
            if attempt < _RETRIES - 1:
                time.sleep(_BACKOFF * (2**attempt))
    assert last is not None
    raise last


# ── JSON ─────────────────────────────────────────────────────────────────────


def load_json_for_update(path: str | Path, *, default: Any = None) -> Any:
    """Load a JSON store you are about to modify and save (see the module docstring)."""
    try:
        from navig.core.json_io import load_json_for_update as _impl  # noqa: PLC0415
    except ImportError:
        return _load_json_for_update_fallback(path, default=default)
    return _impl(path, default=default)


def _fresh(default: Any) -> Any:
    return {} if default is None else copy.deepcopy(default)


def _load_json_for_update_fallback(path: str | Path, *, default: Any = None) -> Any:
    p = Path(path)
    if not p.is_file():
        return _fresh(default)
    try:
        text = _read_text_retrying_fallback(p)
    except OSError as exc:
        raise JsonReadError(f"{p} exists but could not be read: {exc}") from exc
    if not text.strip():
        return _fresh(default)
    try:
        data = json.loads(text)
    except ValueError:
        _quarantine(p, text)
        return _fresh(default)
    if default is not None and not isinstance(data, type(default)):
        _quarantine(p, text)
        return _fresh(default)
    return data


def _quarantine(path: Path, text: str) -> None:
    try:
        (path.parent / (path.name + ".corrupt")).write_text(text, encoding="utf-8")
    except OSError:
        pass


def load_json_safe(path: str | Path, *, default: Any = None) -> Any:
    """Read-only load for a status or list view: any failure reads as *default*."""
    try:
        return load_json_for_update(path, default=default)
    except JsonReadError:
        return _fresh(default)


def atomic_write_json(data: Any, path: str | Path, *, indent: int = 2, sort_keys: bool = False) -> None:
    """Write JSON atomically (a crash cannot leave a truncated file that later reads as empty)."""
    try:
        from navig.core.json_io import atomic_write_json as _impl  # noqa: PLC0415
    except ImportError:
        atomic_write_text(Path(path), json.dumps(data, indent=indent, sort_keys=sort_keys))
        return
    _impl(data, path, indent=indent, sort_keys=sort_keys)


# ── YAML ─────────────────────────────────────────────────────────────────────


def safe_load_yaml(path: str | Path) -> Any:
    """Parse YAML for READING ONLY. ``None`` means missing, empty OR unreadable — never save it back."""
    try:
        from navig.core.yaml_io import safe_load_yaml as _impl  # noqa: PLC0415
    except ImportError:
        return _safe_load_yaml_fallback(path)
    return _impl(path)


def _safe_load_yaml_fallback(path: str | Path) -> Any:
    fp = Path(path)
    if not fp.is_file():
        return None  # decided before importing yaml: "no config" must not need PyYAML
    import yaml  # noqa: PLC0415
    try:
        return yaml.safe_load(_read_text_retrying_fallback(fp))
    except Exception:  # noqa: BLE001 - read-only view: unreadable reads as None
        return None


def load_yaml_for_update(path: str | Path, *, default: dict[str, Any] | None = None) -> dict[str, Any]:
    """Load a YAML mapping you are about to modify and save; refuses to mask an unreadable file."""
    try:
        from navig.core.yaml_io import load_yaml_for_update as _impl  # noqa: PLC0415
    except ImportError:
        return _load_yaml_for_update_fallback(path, default=default)
    return _impl(path, default=default)


def _load_yaml_for_update_fallback(path: str | Path, *, default: dict[str, Any] | None = None) -> dict[str, Any]:
    fp = Path(path)
    result: dict[str, Any] = {} if default is None else default
    if not fp.is_file():
        return result  # decided before importing yaml, as above
    import yaml  # noqa: PLC0415
    try:
        text = _read_text_retrying_fallback(fp)
    except OSError as exc:
        raise ConfigReadError(f"{fp} exists but could not be read: {exc}") from exc
    try:
        data = yaml.safe_load(text)
    except yaml.YAMLError as exc:
        raise ConfigReadError(f"{fp} exists but is not valid YAML: {exc}") from exc
    if data is None:
        return result
    if not isinstance(data, dict):
        raise ConfigReadError(
            f"{fp} did not parse to a mapping (got {type(data).__name__}) — refusing to overwrite it."
        )
    return data


def atomic_write_yaml(data: Any, path: Path | str, allow_unicode: bool = False) -> None:
    """Write YAML atomically (temp file, fsync, then replace)."""
    try:
        from navig.core.yaml_io import atomic_write_yaml as _impl  # noqa: PLC0415
    except ImportError:
        _atomic_write_yaml_fallback(data, path, allow_unicode=allow_unicode)
        return
    _impl(data, path, allow_unicode=allow_unicode)


def _atomic_write_yaml_fallback(data: Any, path: Path | str, *, allow_unicode: bool = False) -> None:
    import yaml  # noqa: PLC0415

    fp = Path(path)
    fp.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=fp.parent, prefix=".tmp_yaml_", suffix=".yaml")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            yaml.dump(data, fh, default_flow_style=False, sort_keys=False, allow_unicode=allow_unicode)
            fh.flush()
            os.fsync(fh.fileno())
        for attempt in range(_RETRIES):
            try:
                os.replace(tmp, fp)
                tmp = None
                return
            except PermissionError:
                if attempt == _RETRIES - 1 or sys.platform != "win32":
                    raise
                time.sleep(_BACKOFF * (2**attempt))
    finally:
        if tmp is not None:
            try:
                os.unlink(tmp)
            except OSError:
                pass
