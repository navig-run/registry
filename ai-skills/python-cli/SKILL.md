---
name: python-cli
description: >
  Conventions and the reference implementation for Python command-line tools built with Typer or
  Click plus Rich — mapped onto navig core's own `navig <resource> <action> [options]` house style
  (always-pretty Rich tables, semantic colour + glyphs, `--json` for machines, loguru logging, lazy
  imports). Use when a repo has a Python CLI entrypoint (a `console_scripts` mapping, a
  `main.py`/`cli.py`/`__main__.py` run with args, or `typer`/`click`/`rich` in its deps), when adding
  or editing a navig CLI command, or when the user says "add a CLI command", "build a Typer CLI",
  "make the output a table", "pretty-print this output", or "wire up the console helper". Read-only
  guidance for authoring — it explains conventions, it does not run destructive commands to explore.
category: development
tags: [python, cli, typer, click, rich, navig-core]
safety: safe
---

# python-cli — Typer/Click + Rich, the navig way

A navig CLI command is a **product surface**, not a debug dump. This skill maps the generic
Typer/Click + Rich stack onto navig core's own conventions — `core/` is itself a large Typer/Click +
Rich CLI, so its patterns are the reference. Terminal-grade, zero-jank: reliability over cleverness.

## Detect the stack

- Deps include **`typer`** and/or **`click`**, usually with **`rich`** (sometimes `rich-click`).
- An entrypoint via one of:
  - `pyproject.toml` `[project.scripts]` / `[tool.poetry.scripts]` mapping a name → `module:function`.
  - `setup.py` / `setup.cfg` `console_scripts`.
  - A top-level `main.py` / `cli.py` / `__main__.py` run as `python -m <pkg>`.
- Argument parsing via `@app.command()` (Typer) or `@click.command()` / `@click.group()` decorators.

**Find the command table first.** Grep for `typer.Typer(`, `@app.command`, `@click.group`,
`@click.command`, or `if __name__ == "__main__"`. That file is the map of the tool. In navig core the
verb tree lives under `navig/commands/` — one command group per file.

## The navig command contract

```
navig <resource> <action> [options]
```

`resource` = a noun (`host`, `db`, `file`, `web`, `skill`, `space`); `action` = a verb
(`list`, `show`, `add`, `run`). **Breaking an existing verb or flag is forbidden** — additive only.
Keep `navig <group> --help` responsive: **lazy-import heavy modules inside the command body**, never
at module top-level (`navig help` must answer in well under 50 ms).

## Install & run (explore before you act)

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1          # Windows PowerShell   (bin/activate on macOS/Linux)

pip install -r requirements.txt      # requirements-based
pip install -e .                     # pyproject/setup with a console_scripts entrypoint
poetry install                       # if poetry.lock present
pdm install                          # if pdm.lock present

<console-script> --help              # after -e . registers the script
python -m <package> --help           # module form
python main.py --help                # loose-script form
```

Always start with `--help` and any `--dry-run` to enumerate behaviour before invoking real actions —
these are live CLIs; some touch the filesystem, network, or system state.

## Output contract — always pretty, always tabular (the house rule)

**Never dump raw dicts, bare `print()`, or hand-aligned `f"{x:<10}"` columns.** Every list or
multi-field status renders through navig's console helper.

```python
import navig.console_helper as ch

table = ch.create_table(title="Connections")     # thin, box=None, padded
table.add_column("Network", no_wrap=True)         # short, known-width → no_wrap
table.add_column("Status",  no_wrap=True)
table.add_column("Account")                        # one free-text column stays wrappable
table.add_row("telegram", "[green]● connected[/green]", "operator_bot")
table.add_row("discord",  "[dim]○ —[/dim]",         "—")
ch.print_table(table)
ch.info("3/7 connected · connect one with navig social connect <network>")
```

- **Column discipline:** `no_wrap=True` on short, fixed-width columns (name/status/token); leave
  **exactly one** free-text column wrappable so a narrow terminal degrades gracefully instead of
  truncating the important short columns with `…`. Test at the real width: `COLUMNS=120 navig …`
  (piping to a subprocess falsely reports 80).
- **Semantic colour + glyphs, not ASCII noise:** `[green]● connected[/green]` · `[dim]○ —[/dim]` ·
  `[red]✗ failed[/red]` · `[yellow]needs auth[/yellow]`. Single-line messages go through
  `ch.success / ch.error / ch.warning / ch.info`; boxed summaries through `ch.panel(...)`.
- **End a status view with a one-line next-step nudge**, and give each row a concise `Next step`
  verb (`→ connect` / `ready` / `reconnect`) rather than a wall of prose.
- **`--json` for machines.** Any status/list command an agent or script might parse also offers
  `--json` printing the raw structured data via `ch.print_json(payload)`. Humans get the table;
  scripts get JSON. Never make one audience parse the other's format.

## Editing conventions

- **Typer** turns type-hinted function params into options/arguments; **Click** uses
  `@click.option` / `@click.argument` decorators. Subcommands hang off a `Typer()` app or a
  `@click.group`. Match the file's existing dialect — don't mix.
- **Logging via loguru, never `print()`** for diagnostics. User-facing output is the Rich console;
  operational logs are loguru. Never log or print a secret, even under `--debug` — secrets live in
  the vault.
- **Config via `navig.config.get(key, default)`**, not raw `os.environ` in a command body.
- Type-hint every public function; raise specific exceptions (`ValueError`, `ConnectionError`),
  never a bare `except:`.
- Pin/record new deps in the manifest the repo already uses (don't add a `requirements.txt` to a
  Poetry project).

## Testing

- pytest with `asyncio_mode=auto` — plain `async def test_*` works, no decorator needed.
- **Isolate state with `NAVIG_DATA_DIR`** (a temp dir), never `NAVIG_HOME`.
- Assert on the `--json` output for behaviour and on rendered strings for formatting; Rich markup
  (`[bold red]…[/]`) only renders through the console — the builtin `print` shows it literally.
- Run: `cd core && py -3 -m pytest tests/<area> -q` (UTF-8 env: `PYTHONUTF8=1`).

## Gotchas

- Missing entrypoint registration → `command not found`. `pip install -e .` to register the script,
  or fall back to `python -m <pkg>` / `python main.py`.
- Windows venv activation is `.venv\Scripts\Activate.ps1`, not `bin/activate`.
- Lucide-style Rich markup errors are silent: an unclosed `[green]` swallows the rest of the line.
- Heavy imports at module top-level regress `--help` latency — the single most common navig-core
  performance defect. Defer them into the function.
