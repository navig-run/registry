# Incident War Room

> When things break, everything you need is already open.

**Tier:** operational · **Status:** ready  
**Owner:** navig-run · **Created:** 2026-03-17

---

## Purpose

Incidents are not just technical problems — they're coordination failures.
This space provides a structured context that activates the moment an alert
fires: live log stream, triage board, runbook assistant with injected context,
and a timeline recorder that auto-drafts the postmortem when you close the
incident.

The agent context injection is real: it reads from `navig/memory/` and
`navig/blackbox/timeline.py` which already exist in the codebase.

---

## What lives here

- Active incident timelines
- Runbooks and SOPs
- Post-mortem drafts and archives
- Alert history and patterns

---

## Capability dependencies

`agent` · `memory` · `tools` · `storage`

## Navig files backing this space

- `navig/blackbox/timeline.py`
- `navig/memory/`
- `navig/agent/`

## Viral hook

> Auto-generated postmortem report — share with your team in one click.

---

*See `.navig/GENESIS.md` for AI agent bootstrap instructions.*
