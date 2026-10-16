"""navig_sdk — the NAVIG plugin SDK (Python).

Two things live here:

* ``navig_sdk.host``, ``navig_sdk.console``, ``navig_sdk.keys``, ``navig_sdk.ai`` — the kit a
  plugin uses so it runs the same **inside navig** (``navig <verb>``) and **on its own**
  (``navig-<name>``, no navig installed). Each uses navig's implementation when navig is
  importable and a faithful standalone one when it is not. ``ai`` answers with navig's AI
  setup inside navig, and with the user's own AI (any provider key, an OpenAI-compatible
  URL, or a local Ollama) without it.
* ``NavigPlugin`` / ``NavigStdioPlugin`` — the JSON-RPC stdio plugin protocol.

Standard library only.
"""
from __future__ import annotations

from navig_sdk.plugin import NavigPlugin, NavigStdioPlugin, navig_config

__version__ = "2.17.0"
__all__ = ["NavigPlugin", "NavigStdioPlugin", "__version__", "navig_config"]
