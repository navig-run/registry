# hello-app

The **canonical minimal NAVIG pack** — the cleanest starting point for writing your own pack.

## What it demonstrates

| File | Purpose |
|------|---------|
| `plugin.json` | Modern manifest with all required fields |
| `handler.py` | Lifecycle hooks (`on_load`, `on_unload`, `on_event`) |
| `commands/hello.py` | Business logic — reads `config.greeting` |
| `commands/echo.py` | Round-trip test command |
| `commands/__init__.py` | `COMMANDS` dict — maps name → handler |
| `tests/test_hello.py` | Full test suite |

## Install locally

```bash
navig store install ./examples/hello-app --yes   # from the root of a registry clone
```

## Use

```bash
navig hello --name Alice
# → Hello, Alice!

navig echo --text "ping"
# → ping
```

## Copy this example

```bash
cp -r examples/hello-app my-pack
# Edit plugin.json: change id, name, description
# Edit commands/ with your business logic
```
