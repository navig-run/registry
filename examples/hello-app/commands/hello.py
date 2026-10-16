"""
hello-app/commands/hello.py

Greet someone. Reads config.greeting for the salutation.
"""
from typing import Any


def handle(args: dict, ctx: Any = None) -> dict:
    """
    Greet a person by name.

    args:
      name (str, optional): Name to greet. Defaults to "World".
    """
    name = args.get("name", "World")
    greeting = "Hello"
    if ctx and isinstance(ctx, dict) and "config" in ctx:
        greeting = ctx["config"].get("greeting", greeting)
    return {"status": "ok", "data": {"message": f"{greeting}, {name}!"}}
