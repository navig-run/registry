"""Find the user's API key for a provider, with or without navig.

Order, the same one navig uses for media providers:

1. environment variables — the provider's conventional names (``OPENAI_API_KEY``,
   ``ANTHROPIC_API_KEY``/``CLAUDE_API_KEY``, …), any extra names the caller passes, then
   the generic ``<PROVIDER>_API_KEY``;
2. the shared navig vault (``~/.navig/vault``) when the ``navig-vault`` package is installed.
   It is a standalone package, so a user who keeps keys with ``nv add`` gets them here even
   without navig — and with navig installed it is the very same vault navig reads.

A key is never logged or included in an error message.
"""

from __future__ import annotations

import os

__all__ = ["PROVIDER_ENV_VARS", "api_key"]

# Mirrors navig.providers.types.PROVIDER_ENV_VARS for the providers a plugin can reach over
# an OpenAI-compatible API. A parity test in core fails the build if a shared entry drifts.
PROVIDER_ENV_VARS: dict[str, list[str]] = {
    "openai": ["OPENAI_API_KEY"],
    "anthropic": ["ANTHROPIC_API_KEY", "CLAUDE_API_KEY"],
    "openrouter": ["OPENROUTER_API_KEY"],
    "groq": ["GROQ_API_KEY"],
    "google": ["GEMINI_API_KEY", "GOOGLE_API_KEY"],
    "mistral": ["MISTRAL_API_KEY"],
    "xai": ["XAI_API_KEY", "GROK_KEY"],
}


def api_key(provider: str, *extra_env: str, caller: str = "navig-sdk") -> str | None:
    """The API key for *provider*, or ``None`` when the user has not configured one."""
    names = [*PROVIDER_ENV_VARS.get(provider, []), *extra_env, f"{provider.upper()}_API_KEY"]
    for name in dict.fromkeys(names):
        value = os.environ.get(name, "").strip()
        if value:
            return value
    return _vault_key(provider, caller)


def _vault_key(provider: str, caller: str) -> str | None:
    try:
        from navig_vault.core import get_vault  # noqa: PLC0415
    except ImportError:
        return None
    try:
        key = get_vault().get_api_key(provider, caller=caller)
    except Exception:  # noqa: BLE001 - a locked or absent vault means "no key", never a crash
        return None
    return str(key).strip() if key else None
