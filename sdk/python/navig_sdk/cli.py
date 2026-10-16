"""The front door of a standalone plugin: ``navig-<name>`` runs the same app as ``navig <verb>``.

    # navig_<name>/cli.py
    from navig_sdk.cli import run
    from navig_<name>.commands.<name> import app

    def main() -> None:
        run(app, "navig-<name>")

Two things every standalone entry point needs, done once:

* **A console that can print the help.** Typer help text carries emoji; on a legacy Windows
  console (cp1251, cp866…) Rich raises ``UnicodeEncodeError`` while rendering ``--help``,
  before a single line reaches the user. Inside navig the console is already set up;
  standalone nothing does it.
* **A clear line instead of a traceback for a navig-only feature.** Some features are about
  navig itself (its managed browser, its daemon, its Telegram bot). Standalone they import a
  ``navig.*`` module that is not installed; this turns that ``ModuleNotFoundError`` into
  "this needs navig: pip install navig" and exit status 1. Any other error is left alone.
"""

from __future__ import annotations

import sys
from typing import Any

__all__ = ["run"]


def _ensure_utf8_stdio() -> None:
    if sys.platform != "win32":
        return
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[union-attr]
        except (AttributeError, OSError, ValueError):
            pass


def run(app: Any, prog_name: str) -> None:
    """Run a Typer/Click *app* as the console script *prog_name*."""
    _ensure_utf8_stdio()
    try:
        app(prog_name=prog_name)
    except ModuleNotFoundError as exc:
        name = exc.name or ""
        if name == "navig" or name.startswith("navig."):
            print(
                f"{prog_name}: this feature is part of navig and needs it installed "
                f"(it uses {name}).\n  pip install navig",
                file=sys.stderr,
            )
            sys.exit(1)
        if name.startswith("navig_"):
            # A first-party package behind an optional extra (navig_browser for TikTok login,
            # filming a page …): name the package to install instead of a traceback.
            package = name.split(".", 1)[0].replace("_", "-")
            print(
                f"{prog_name}: this feature needs the {package} package.\n  pip install {package}",
                file=sys.stderr,
            )
            sys.exit(1)
        raise
