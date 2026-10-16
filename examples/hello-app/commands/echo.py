"""
hello-app/commands/echo.py

Echo input back — useful for round-trip testing.
"""
from typing import Any


def handle(args: dict, ctx: Any = None) -> dict:
    """
    Echo the input back unchanged.

    args:
      text (str): Text to echo.
    """
    text = args.get("text", "")
    if not text:
        return {"status": "error", "message": "Missing 'text' argument"}
    return {"status": "ok", "data": {"echo": text}}
