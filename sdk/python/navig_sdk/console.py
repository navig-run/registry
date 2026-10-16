"""Terminal output that looks like navig's, with or without navig.

    from navig_sdk import console as ch
    ch.success("Saved")            # ✓ Saved
    ch.error("Failed", "details")  # ✗ Failed
    ch.console.print(table)

With navig installed every name resolves to ``navig.console_helper`` itself, so a plugin
running as ``navig <verb>`` prints exactly what the rest of navig prints (and gets its full
surface). Without navig, the names below are a small stand-in built on Rich when Rich is
importable (it is whenever the plugin uses Typer), and on plain ``print`` otherwise.

The stand-in covers what first-party plugins were measured to call: error, success,
console, dim, info, warning, raw_print, kv, print_table, create_table, create_spinner,
subheader, emit_json, print_json. Anything else raises AttributeError standalone rather
than silently doing nothing.
"""

from __future__ import annotations

import json
import sys
from typing import Any

_STANDALONE = (
    "console",
    "create_spinner",
    "create_table",
    "dim",
    "emit_json",
    "error",
    "info",
    "kv",
    "print_json",
    "print_table",
    "raw_print",
    "subheader",
    "success",
    "warning",
)


def __getattr__(name: str) -> Any:
    import importlib  # noqa: PLC0415

    try:
        _navig = importlib.import_module("navig.console_helper")
    except ImportError:
        _navig = None
    if _navig is not None:
        return getattr(_navig, name)
    if name in _STANDALONE:
        return getattr(_Standalone, name)
    raise AttributeError(f"navig_sdk.console has no {name!r} without navig installed")


def __dir__() -> list[str]:
    return sorted(_STANDALONE)


def _symbol(preferred: str, fallback: str) -> str:
    """The glyph if the terminal can encode it, else an ASCII stand-in (cp1251 consoles)."""
    encoding = getattr(sys.stdout, "encoding", None) or "ascii"
    try:
        preferred.encode(encoding)
    except (UnicodeEncodeError, LookupError):
        return fallback
    return preferred


class _Plain:
    """Enough of rich.console.Console for print() when Rich is not installed."""

    def print(self, *objects: Any, **_: Any) -> None:
        import re  # noqa: PLC0415

        print(*(re.sub(r"\[/?[a-z0-9 _#.-]*\]", "", str(o)) for o in objects))


class _Standalone:
    _console: Any = None

    @classmethod
    def _get(cls) -> Any:
        if cls._console is None:
            try:
                from rich.console import Console  # noqa: PLC0415
            except ImportError:
                cls._console = _Plain()
            else:
                cls._console = Console()
        return cls._console

    class _ConsoleProxy:
        def __getattr__(self, name: str) -> Any:
            return getattr(_Standalone._get(), name)

    console = _ConsoleProxy()

    @staticmethod
    def _line(color: str, mark: str, message: str, details: str | None) -> None:
        c = _Standalone._get()
        c.print(f"[{color}]{mark}[/{color}] {message}")
        if details:
            c.print(f"  [dim]{details}[/dim]")

    @staticmethod
    def success(message: str, details: str | None = None) -> None:
        _Standalone._line("green", _symbol("✓", "+"), message, details)

    @staticmethod
    def error(message: str, details: str | None = None) -> None:
        _Standalone._line("red", _symbol("✗", "x"), message, details)

    @staticmethod
    def warning(message: str, details: str | None = None) -> None:
        _Standalone._line("yellow", _symbol("⚠", "!"), message, details)

    @staticmethod
    def info(message: str, details: str | None = None, no_wrap: bool = False) -> None:  # noqa: ARG004
        _Standalone._line("cyan", _symbol("ℹ", "i"), message, details)

    @staticmethod
    def dim(message: str) -> None:
        _Standalone._get().print(f"[dim]{message}[/dim]")

    @staticmethod
    def subheader(title: str) -> None:
        _Standalone._get().print(f"[bold]{title}[/bold]")

    @staticmethod
    def kv(label: str, value: object, indent: int = 2) -> None:
        _Standalone._get().print(f"{' ' * indent}[dim]{label}:[/dim] {value}")

    @staticmethod
    def raw_print(message: str) -> None:
        print(str(message))

    @staticmethod
    def emit_json(
        data: object,
        *,
        indent: int | None = 2,
        sort_keys: bool = False,
        ensure_ascii: bool = True,
        default: Any = str,
    ) -> None:
        # Builtin print, never the Rich console: --json output must not be wrapped or coloured.
        print(json.dumps(data, indent=indent, sort_keys=sort_keys, ensure_ascii=ensure_ascii, default=default))

    @staticmethod
    def print_json(data: Any, indent: int = 2) -> None:
        _Standalone._get().print(json.dumps(data, indent=indent, default=str))

    @staticmethod
    def create_table(
        title: str | None = None,
        columns: list[dict[str, str]] | None = None,
        show_header: bool = True,
        show_lines: bool = False,
    ) -> Any:
        from rich.table import Table  # noqa: PLC0415

        table = Table(title=title, show_header=show_header, show_lines=show_lines, box=None, padding=(0, 2))
        for col in columns or []:
            table.add_column(col.get("name", ""), style=col.get("style"), justify=col.get("justify", "left"))
        return table

    @staticmethod
    def print_table(table: Any) -> None:
        _Standalone._get().print(table)

    @staticmethod
    def create_spinner(message: str = "Working...") -> Any:
        c = _Standalone._get()
        if hasattr(c, "status"):
            return c.status(message)
        import contextlib  # noqa: PLC0415

        print(message)
        return contextlib.nullcontext()
