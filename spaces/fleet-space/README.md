# Autonomous Fleet

> Multi-agent autonomous execution fleet — spawn, coordinate, and monitor swarms.

**Tier:** labs · **Status:** labs  
**Owner:** navig-run · **Created:** 2026-03-17

---

## Purpose

Sometimes one agent isn't enough. The fleet spawns multiple agents against the
same problem in parallel, coordinates their execution via the nervous system,
and surfaces the one that won — with a full comparison of how each approached
the task. You watch. You decide which result to accept.

**Requires:** `formations.enabled` in your Navig config.

---

## What lives here

- Fleet compositions and saved swarm configs
- Parallel execution logs
- Result comparison archives
- Winning run exports

---

## Capability dependencies

`formations` · `agent` · `tools` · `storage`

Requires config: `formations.enabled = true`

## Navig files backing this space

- `navig/formations/`
- `navig/agent/nervous_system.py`

## Viral hook

> Watch 7 agents solve a problem in parallel, then see the one that won.

---

*See `.navig/GENESIS.md` for AI agent bootstrap instructions.*
