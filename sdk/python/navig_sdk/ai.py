"""Ask an AI for text: navig's AI when navig is installed, the user's own AI when it is not.

    from navig_sdk import ai
    text = ai.generate("Write a two-line product blurb for a label printer")

**Inside navig** the request goes through ``navig.llm.generate.llm_generate``: the user's
own routing, modes, fallbacks and subscriptions. navig is authoritative there — if it fails,
the error is raised rather than quietly retried against some other AI the user did not pick.

**Without navig** the first of these that is configured answers:

1. ``NAVIG_AI_BASE_URL`` (+ optional ``NAVIG_AI_API_KEY``, ``NAVIG_AI_MODEL``): any
   OpenAI-compatible server — LM Studio, vLLM, a company gateway, a hosted proxy.
2. ``NAVIG_AI_PROVIDER`` names one of the providers below explicitly.
3. The first provider with a key (environment variable, or the shared navig vault through
   ``navig-vault``): OpenAI, OpenRouter, Anthropic, Groq, Google Gemini, Mistral, xAI.
4. A local Ollama, if one answers (``OLLAMA_HOST``, default ``http://localhost:11434``).

Every one of them is reached through the same OpenAI-compatible ``/chat/completions`` call,
so this is one code path, standard library only. ``NAVIG_AI_MODEL`` overrides the model for
any of them. Nothing here ever logs or echoes a key.
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Any

from navig_sdk.keys import api_key

__all__ = ["PROVIDERS", "AIError", "AINotConfigured", "Endpoint", "acomplete", "generate", "resolve", "status"]

_NOT_CONFIGURED = (
    "No AI is configured. Any one of these works:\n"
    "  - set a provider key, e.g. OPENAI_API_KEY, OPENROUTER_API_KEY, ANTHROPIC_API_KEY or GROQ_API_KEY\n"
    "  - point NAVIG_AI_BASE_URL (and NAVIG_AI_MODEL) at any OpenAI-compatible server\n"
    "  - run Ollama locally (https://ollama.com)\n"
    "  - or install navig (pip install navig) to use its AI setup"
)


class AIError(RuntimeError):
    """The AI was reached but the request failed (bad key, unknown model, server error…)."""


class AINotConfigured(AIError):
    """No AI is configured at all; the message says how to configure one."""

    def __init__(self) -> None:
        super().__init__(_NOT_CONFIGURED)


@dataclass(frozen=True)
class Endpoint:
    name: str
    base_url: str
    model: str
    key: str | None

    def __repr__(self) -> str:  # never show the key
        return f"Endpoint(name={self.name!r}, base_url={self.base_url!r}, model={self.model!r})"


# (provider, OpenAI-compatible base URL, default model). The default models are checked
# against navig's retired-model denylist by a test in core, so a retired id fails the build.
# Defaults are deliberately NON-reasoning models: a reasoning model spends its token budget
# thinking, so a plugin asking for a short answer can get nothing back at all (measured:
# openai/gpt-5-mini via OpenRouter, max_tokens=32 -> empty content). Each was called live.
PROVIDERS: list[tuple[str, str, str]] = [
    ("openai", "https://api.openai.com/v1", "gpt-4.1-mini"),
    ("openrouter", "https://openrouter.ai/api/v1", "openai/gpt-4.1-mini"),
    ("anthropic", "https://api.anthropic.com/v1", "claude-haiku-4-5"),
    ("groq", "https://api.groq.com/openai/v1", "openai/gpt-oss-20b"),
    ("google", "https://generativelanguage.googleapis.com/v1beta/openai", "gemini-2.5-flash"),
    ("mistral", "https://api.mistral.ai/v1", "mistral-small-latest"),
    ("xai", "https://api.x.ai/v1", "grok-3-mini"),
]


def generate(
    prompt: str | list[dict[str, str]],
    *,
    system: str | None = None,
    max_tokens: int | None = None,
    temperature: float | None = None,
    timeout: float = 120,
    mode: str | None = None,
    provider: str | None = None,
    model: str | None = None,
) -> str:
    """Return the AI's reply as text.

    *prompt* is a string or a list of ``{"role", "content"}`` messages. *mode* is passed to
    navig's router when navig answers (e.g. ``"summarize"``) and ignored otherwise.

    *provider* / *model* pin the request when the user asked for one (a plugin's
    ``--provider`` / ``--model``). Inside navig they become navig's ``provider_override`` /
    ``model_override``, so the pin is honoured there too rather than silently dropped; on
    its own they take the place of ``NAVIG_AI_PROVIDER`` / ``NAVIG_AI_MODEL``.
    Raises :class:`AINotConfigured` when nothing is set up, :class:`AIError` when the AI fails.
    """
    messages = [{"role": "user", "content": prompt}] if isinstance(prompt, str) else list(prompt)
    if system:
        messages = [{"role": "system", "content": system}, *messages]

    try:
        from navig.llm.generate import llm_generate  # noqa: PLC0415
    except ImportError:
        llm_generate = None
    if llm_generate is not None:
        pins: dict[str, str] = {}
        # Passed only when set: a navig whose llm_generate predates the overrides still
        # answers every call that does not pin a provider or model.
        if provider:
            pins["provider_override"] = provider
        if model:
            pins["model_override"] = model
        return llm_generate(
            messages, mode=mode, max_tokens=max_tokens, temperature=temperature, timeout=timeout,
            **pins,
        )

    endpoint = resolve(provider=provider, model=model)
    if endpoint is None:
        raise AINotConfigured()
    return _chat(endpoint, messages, max_tokens=max_tokens, temperature=temperature, timeout=timeout)


async def acomplete(prompt: str, *, system: str | None = None, timeout: float = 120) -> str:
    """Async one-shot completion.

    Inside navig this is navig's AI client (``navig.agent.ai_client``) — the same call the
    text, design and download plugins made before they could run on their own, so their
    behaviour inside navig does not change. On its own it is :func:`generate` off the event
    loop, against the user's own AI. Raises like :func:`generate`.
    """
    try:
        from navig.agent.ai_client import get_ai_client  # noqa: PLC0415
    except ImportError:
        get_ai_client = None
    if get_ai_client is not None:
        return await get_ai_client().complete(prompt, system_prompt=system) or ""
    import asyncio  # noqa: PLC0415

    return await asyncio.to_thread(generate, prompt, system=system, timeout=timeout)


def status() -> dict[str, Any]:
    """Is an AI ready here, and which? ``{"ready", "provider", "model", "via", "error"}``.

    Contacts nothing paid: inside navig it asks navig's AI client; on its own it resolves
    the standalone configuration (which only pings a LOCAL Ollama).
    """
    try:
        from navig.agent.ai_client import get_ai_client  # noqa: PLC0415
    except ImportError:
        get_ai_client = None
    if get_ai_client is not None:
        client = get_ai_client()
        return {
            "ready": bool(client.is_available()),
            "provider": getattr(client, "provider", None),
            "model": getattr(client, "model", None),
            "via": "navig",
            "error": None,
        }
    try:
        ep = resolve()
    except AIError as exc:
        return {"ready": False, "provider": None, "model": None, "via": "standalone", "error": str(exc)}
    if ep is None:
        return {"ready": False, "provider": None, "model": None, "via": "standalone", "error": _NOT_CONFIGURED}
    return {"ready": True, "provider": ep.name, "model": ep.model, "via": "standalone", "error": None}


def resolve(provider: str | None = None, model: str | None = None) -> Endpoint | None:
    """Which standalone AI would answer (``None``: none configured). Never contacts a paid API.

    *provider* / *model*, when given, win over ``NAVIG_AI_PROVIDER`` / ``NAVIG_AI_MODEL``.
    ``provider="custom"`` selects ``NAVIG_AI_BASE_URL``; any other explicit provider skips it.
    """
    model_override = (model or "").strip() or os.environ.get("NAVIG_AI_MODEL", "").strip()
    pinned = (provider or "").strip().lower()

    base = os.environ.get("NAVIG_AI_BASE_URL", "").strip()
    if pinned == "custom" and not base:
        raise AIError("provider 'custom' needs NAVIG_AI_BASE_URL (an OpenAI-compatible server URL)")
    if base and pinned in ("", "custom"):
        if not model_override:
            raise AIError("NAVIG_AI_BASE_URL is set but NAVIG_AI_MODEL is not; set the model to use")
        key = os.environ.get("NAVIG_AI_API_KEY", "").strip() or None
        return Endpoint("custom", base.rstrip("/"), model_override, key)

    wanted = pinned or os.environ.get("NAVIG_AI_PROVIDER", "").strip().lower()
    table = PROVIDERS
    if wanted:
        table = [p for p in PROVIDERS if p[0] == wanted]
        if not table and wanted != "ollama":
            names = ", ".join([p[0] for p in PROVIDERS] + ["ollama", "custom"])
            raise AIError(f"NAVIG_AI_PROVIDER={wanted!r} is not one of: {names}")
    for name, url, default_model in table:
        key = api_key(name)
        if key:
            return Endpoint(name, url, model_override or default_model, key)
    if wanted and wanted != "ollama":
        raise AIError(f"NAVIG_AI_PROVIDER={wanted} but no {wanted} key is set")

    return _ollama(model_override)


def _ollama(model_override: str) -> Endpoint | None:
    host = (
        os.environ.get("NAVIG_OLLAMA_URL") or os.environ.get("OLLAMA_HOST") or "http://localhost:11434"
    ).strip().rstrip("/")
    if not host.startswith(("http://", "https://")):
        host = f"http://{host}"
    try:
        with urllib.request.urlopen(f"{host}/api/tags", timeout=1.5) as resp:  # noqa: S310 - user-configured local URL
            tags = json.load(resp)
    except (OSError, ValueError):
        return None
    models = [m.get("name") for m in tags.get("models", []) if m.get("name")]
    model = model_override or (models[0] if models else "")
    if not model:
        return None
    return Endpoint("ollama", f"{host}/v1", model, None)


def _chat(
    endpoint: Endpoint,
    messages: list[dict[str, str]],
    *,
    max_tokens: int | None,
    temperature: float | None,
    timeout: float,
) -> str:
    body: dict[str, Any] = {"model": endpoint.model, "messages": messages}
    if max_tokens is not None:
        # OpenAI's newer models REJECT `max_tokens` (HTTP 400, "use max_completion_tokens");
        # OpenAI accepts the new name on every model, the other servers expect the old one.
        body["max_completion_tokens" if endpoint.name == "openai" else "max_tokens"] = max_tokens
    if temperature is not None:
        body["temperature"] = temperature
    headers = {"Content-Type": "application/json", "User-Agent": "navig-sdk"}
    if endpoint.key:
        headers["Authorization"] = f"Bearer {endpoint.key}"
    req = urllib.request.Request(
        f"{endpoint.base_url}/chat/completions",
        data=json.dumps(body).encode("utf-8"),
        headers=headers,
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:  # noqa: S310 - fixed https hosts or the user's own URL
            payload = json.load(resp)
    except urllib.error.HTTPError as exc:
        detail = exc.read(400).decode("utf-8", errors="replace").strip()
        raise AIError(f"{endpoint.name} ({endpoint.model}) answered HTTP {exc.code}: {detail}") from None
    except (OSError, ValueError) as exc:
        raise AIError(f"could not reach {endpoint.name} at {endpoint.base_url}: {exc}") from None
    try:
        choice = payload["choices"][0]
        content = choice["message"].get("content") or ""
    except (KeyError, IndexError, TypeError, AttributeError):
        raise AIError(f"{endpoint.name} returned no message: {str(payload)[:200]}") from None
    if not content.strip() and choice.get("finish_reason") == "length":
        # An empty reply here is not an answer: the token limit ran out before any text
        # (a reasoning model spends it thinking). Returning "" would read as success.
        raise AIError(
            f"{endpoint.name} ({endpoint.model}) hit the token limit before writing any text; "
            "raise max_tokens or choose a non-reasoning model with NAVIG_AI_MODEL"
        )
    return content
