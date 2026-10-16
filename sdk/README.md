# NAVIG Plugin SDK

Build JSON-RPC stdio plugins for the [NAVIG CLI](https://github.com/navig-run/core) in Python or TypeScript/Node.js.

The canonical SDK source lives here in `sdk/` — both Python and TypeScript.

## Quick start — Python

```bash
pip install navig-sdk
```

```python
from navig_sdk import NavigPlugin

plugin = NavigPlugin(name="my-plugin", version="1.0.0")

@plugin.command("greet")
def greet(name: str = "world") -> str:
    return f"Hello, {name}!"

@plugin.command("add")
def add(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    plugin.run()
```

Register in `.navig/agents/my-plugin.yaml`:

```yaml
id: my-plugin
runtime: python
entry: my_plugin.py
provides:
  commands:
    - greet
    - add
```

## Quick start — TypeScript / Node.js

```bash
npm install navig-sdk
```

```ts
import { NavigPlugin } from "navig-sdk";

const plugin = new NavigPlugin("my-plugin", "1.0.0");

plugin.command("greet", ({ name = "world" }: { name?: string }) => {
  return `Hello, ${name}!`;
});

plugin.run();
```

Register in `.navig/agents/my-plugin.yaml`:

```yaml
id: my-plugin
runtime: node
entry: dist/plugin.js
```

## Protocol

NAVIG communicates with plugins over **newline-delimited JSON-RPC on stdin/stdout**:

```
stdin  → {"id": 1, "method": "greet", "params": {"name": "Alice"}}
stdout ← {"id": 1, "result": "Hello, Alice!"}
```

Params can be a `dict` / object (keyword) or an `array` (positional).
Absent or null `params` calls the handler with no arguments.

## `navig_config()` — read NAVIG config in plugins

```python
from navig_sdk import navig_config

cfg = navig_config()          # reads ~/.navig/config.yaml
api_key = cfg.get("API_KEY")  # handles upper/mixed-case keys and quoted values
```

Pure-Python parser — no PyYAML required.

## See also

- [Example plugin](../examples/hello-app/) — full lifecycle example (new model)
- [NAVIG Handbook](https://github.com/navig-run/core/blob/main/docs/user/HANDBOOK.md)
- [Contributing](../CONTRIBUTING.md)

## Development

```bash
# Python SDK — run tests
cd sdk/python
python -m pytest tests/ -q

# TypeScript — type-check
cd sdk/typescript
npm install
npx tsc --noEmit
```

## Versions

| Package   | Registry | Version |
|-----------|----------|---------|
| navig-sdk | PyPI     | 2.4.14  |
| navig-sdk | npm      | 2.4.14  |
