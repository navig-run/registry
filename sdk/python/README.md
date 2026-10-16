# navig-sdk

The Python SDK for NAVIG plugins. It lets one plugin work in two places:

- **inside navig**, as `navig <verb>`, and
- **on its own**, as `navig-<name>`, with no navig installed.

When a plugin needs AI, it uses navig's AI setup inside navig and **the user's own AI** outside it.

```bash
pip install navig-sdk
```

Standard library only. It adds nothing else to an install.

## Bring your own AI

```python
from navig_sdk import ai

print(ai.generate("Write a one-line tagline for a label printer", max_tokens=200))
```

Inside navig, this goes through navig's AI (its routing, modes and subscriptions). Without navig,
the first of these that is set up answers:

| Set this | Uses |
|---|---|
| `NAVIG_AI_BASE_URL` + `NAVIG_AI_MODEL` (+ `NAVIG_AI_API_KEY`) | any OpenAI-compatible server: LM Studio, vLLM, a company gateway |
| `NAVIG_AI_PROVIDER=<name>` | that provider, if its key is set |
| `OPENAI_API_KEY` | OpenAI (`gpt-4.1-mini`) |
| `OPENROUTER_API_KEY` | OpenRouter (`openai/gpt-4.1-mini`) |
| `ANTHROPIC_API_KEY` / `CLAUDE_API_KEY` | Anthropic (`claude-haiku-4-5`) |
| `GROQ_API_KEY` | Groq (`openai/gpt-oss-20b`) |
| `GEMINI_API_KEY` / `GOOGLE_API_KEY` | Google Gemini (`gemini-2.5-flash`) |
| `MISTRAL_API_KEY` | Mistral (`mistral-small-latest`) |
| `XAI_API_KEY` | xAI (`grok-3-mini`) |
| nothing, with Ollama running | the first local Ollama model (`OLLAMA_HOST`, default `localhost:11434`) |

`NAVIG_AI_MODEL` overrides the model for any of these.

Keys are also read from the shared navig vault when [`navig-vault`](https://pypi.org/project/navig-vault/)
is installed (`nv add`). Keys are never logged. If nothing is configured, the call raises `ai.AINotConfigured`,
whose message tells the user how to set one up.

## Run the same with or without navig

```python
from navig_sdk import console as ch, host

ch.success("Saved", "3 files")        # navig's console inside navig, a Rich stand-in without it
db = host.data_dir() / "myplugin.db"  # the SAME directory navig uses (~/.navig/data)
host.atomic_write_text(host.config_dir() / "myplugin.json", "{}")
proc = host.run_text(["git", "status"])  # output decoded safely on every platform
```

Paths follow navig's own rules (`NAVIG_CONFIG_DIR`, `NAVIG_DATA_DIR`, `NAVIG_CACHE_DIR`,
`NAVIG_LOG_DIR`, system-service locations), so data written standalone is data navig finds
later, and the reverse. navig's test suite checks this against navig's resolvers.

For a plugin's own JSON or YAML files, `navig_sdk.files` gives the read-modify-write helpers
navig uses: a file that exists but cannot be read raises instead of loading as empty, so a
failed read can never be saved back over real data.

```python
from navig_sdk import files

state = files.load_json_for_update(path, default={})  # raises JsonReadError if it can't read
state["last_run"] = now
files.atomic_write_json(state, path)
```

Settings that predate `plugins.<name>` keep their own path: `settings.get_path("adapters.social.
facebook.page_id")` and `settings.set_path(...)` read and write any dotted key in the same
config.yaml (navig's `ConfigManager` inside navig), leaving every sibling key alone.

For speech, `navig_sdk.lang.language_code("Russian")` returns the ISO code a speech model
accepts (`"ru"`), and `None` for auto-detect or anything it does not recognise, the same table
navig uses.

A plugin built on this declares `[tool.navig] mode = "standalone"`, and ships a `navig-<name>`
console script next to its `navig.commands` entry point: one app, two ways in.

## Stdio plugins

`NavigPlugin` / `NavigStdioPlugin` implement NAVIG's JSON-RPC-over-stdio plugin protocol for
tools written as separate processes. `navig_config()` reads top-level keys from `~/.navig/config.yaml`.

## License

MIT
