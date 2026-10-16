"""navig_sdk.plugin — JSON-RPC stdio plugin host.

Bug-fixes over original navig-core implementation (2026-03-17):
  BUG-1  navig_config() regex dropped uppercase / mixed-case keys  → fixed
  BUG-2  navig_config() left surrounding YAML quotes in values      → fixed
  BUG-3  run() coerced empty-list params [] to {} via `or {}`       → fixed
  BUG-4  run() leaked "None" into error when method was JSON null   → fixed
  BUG-5  package had no __init__.py, breaking editable installs     → fixed
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any, Callable


def _reply(id: Any = None, *, result: Any = None, error: str | None = None) -> dict:
    """Build a JSON-RPC response dict."""
    if error is not None:
        return {"id": id, "error": error}
    return {"id": id, "result": result}


class NavigPlugin:
    """JSON-RPC stdio plugin host for NAVIG.

    Usage::

        from navig_sdk import NavigPlugin

        plugin = NavigPlugin(name="my-plugin", version="1.0.0")

        @plugin.command("greet")
        def greet(name: str = "world") -> str:
            return f"Hello, {name}!"

        if __name__ == "__main__":
            plugin.run()
    """

    def __init__(self, name: str, version: str = "0.1.0") -> None:
        self.name = name
        self.version = version
        self._commands: dict[str, Callable] = {}

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def command(self, name: str) -> Callable:
        """Decorator — register *name* as a dispatchable command."""
        def decorator(func: Callable) -> Callable:
            self._commands[name] = func
            return func
        return decorator

    # Convenience attribute — exposes registered command names
    @property
    def commands(self) -> dict[str, Callable]:
        return self._commands

    def meta(self) -> dict:
        """Return plugin metadata (name, version, commands)."""
        return {
            "name": self.name,
            "version": self.version,
            "commands": list(self._commands),
        }

    def run(self) -> None:
        """Read JSON-RPC messages from stdin and write replies to stdout.

        Each line of stdin must be a single JSON object.  Empty / whitespace-only
        lines are silently skipped.  The method key may be absent or JSON null —
        both produce an ``"Unknown method:"`` error without leaking Python ``None``
        into the message (BUG-4 fix).
        """
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue  # BUG-3 adjacent: skip blank lines gracefully

            try:
                message = json.loads(line)
            except json.JSONDecodeError as exc:
                print(json.dumps({"error": f"JSON parse error: {exc}"}))
                sys.stdout.flush()
                continue

            msg_id = message.get("id")
            # BUG-4: `message.get("method")` may return None (JSON null key).
            # Coerce None → "" so the "not method" guard works cleanly and the
            # error message reads "Unknown method: " instead of "Unknown method: None".
            method: str = message.get("method") or ""

            # BUG-3: params may be explicitly [] (a valid positional call with
            # zero args).  Do NOT replace it with {} via `or {}`.
            params: Any = message.get("params")

            if not method or method not in self._commands:
                reply = _reply(msg_id, error=f"Unknown method: {method}")
            else:
                try:
                    if isinstance(params, list):
                        result = self._commands[method](*params)
                    elif isinstance(params, dict):
                        result = self._commands[method](**params)
                    else:
                        # params is None (key absent) — call with no arguments
                        result = self._commands[method]()
                    reply = _reply(msg_id, result=result)
                except Exception as exc:  # noqa: BLE001
                    reply = _reply(msg_id, error=str(exc))

            print(json.dumps(reply))
            sys.stdout.flush()


# ---------------------------------------------------------------------------
# Alias — navig-community README previously used NavigStdioPlugin
# ---------------------------------------------------------------------------
NavigStdioPlugin = NavigPlugin


# ---------------------------------------------------------------------------
# Config helper
# ---------------------------------------------------------------------------

def navig_config(path: str | None = None) -> dict[str, str]:
    """Load ``~/.navig/config.yaml`` and return it as a plain ``dict``.

    Does **not** require PyYAML — uses a minimal line-based parser so plugins
    can load NAVIG config without pulling in runtime dependencies.

    Fixes:
    * BUG-1: Key regex now allows uppercase letters and digits (``\\w+``).
    * BUG-2: Values wrapped in matching single or double quotes are unquoted.

    Returns an empty dict when the config file is absent or unreadable.
    """
    cfg_path = Path(path) if path else Path.home() / ".navig" / "config.yaml"

    try:
        text = cfg_path.read_text(encoding="utf-8")
    except OSError:
        return {}

    result: dict[str, str] = {}
    # BUG-1 fix: \w+ accepts any ASCII letter (upper/lower), digit, and underscore.
    _kv_re = re.compile(r"^(\w+):\s*(.*?)\s*$")

    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = _kv_re.match(line)
        if not m:
            continue
        key, value = m.group(1), m.group(2)
        # BUG-2 fix: strip matching surrounding quotes (both single and double).
        if len(value) >= 2 and value[0] == value[-1] and value[0] in ('"', "'"):
            value = value[1:-1]
        result[key] = value

    return result
