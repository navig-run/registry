"""
hello-app/handler.py — pack lifecycle for hello-app.
"""
from __future__ import annotations
from typing import Any


def on_load(ctx: dict) -> None:
    """Register commands on pack activation."""
    try:
        from navig.commands._registry import CommandRegistry
        from .commands import COMMANDS
        for name, handler in COMMANDS.items():
            CommandRegistry.register(name, handler)
    except ImportError:
        pass  # standalone / authoring mode — ok


def on_unload(ctx: dict) -> None:
    """Deregister commands on pack deactivation."""
    try:
        from navig.commands._registry import CommandRegistry
        from .commands import COMMANDS
        for name in COMMANDS:
            CommandRegistry.deregister(name)
    except ImportError:
        pass


def on_event(event: str, ctx: dict) -> dict | None:
    return None


# For authoring tools and direct invocation
COMMANDS: dict[str, Any] = {}
try:
    from .commands import COMMANDS  # type: ignore[assignment]
except ImportError:
    pass
