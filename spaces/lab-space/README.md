# Command Laboratory

> Run, tweak, share any Navig command live.

**Tier:** studio · **Status:** planned  
**Owner:** navig-run · **Created:** 2026-03-17

> **Planned.** This space is a concept: it ships its purpose, goals and inbox routes,
> but no agents, skills or workflows yet. The REPL and share-as-URL features below
> are the design target, not something you can run today.

---

## Purpose

The problem with `--help` is that it's a wall of text. This space is the
replacement: a live REPL where you run Navig commands, see instant diffs, and
share working sequences as URLs that run in anyone's Navig instance.

Discovery happens by doing, not by reading.

---

## What lives here

- Saved command sequences and snippets
- Shared packages exported from sessions
- Notes on command patterns and edge cases
- Autocomplete source data (fed from the tool registry)

---

## Capability dependencies

`agent` · `tools` · `storage`

These must be active in your Navig instance for this space to function.

## Viral hook

> Share a working command sequence as a URL — it runs in the recipient's Navig
> instance, not as a screenshot, but as a *runnable artifact*.

---

*See `.navig/GENESIS.md` for AI agent bootstrap instructions.*
