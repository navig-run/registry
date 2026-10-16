# Agent Personality Studio

> Shape how your agent thinks, speaks, and decides.

**Tier:** studio · **Status:** planned  
**Owner:** navig-run · **Created:** 2026-03-17

> **Planned.** This space is a concept: it ships its purpose, goals and inbox routes,
> but no agents, skills or workflows yet. Today you can already inspect and edit your
> agent's identity with `navig agent soul` and `navig agent personality`; the
> live-preview studio and persona publishing below are the design target.

---

## Purpose

Your agent already has a soul — it lives in `navig/agent/context/SOUL.md` and
`navig/resources/PERSONA.md`. This space makes those files *live-editable with
instant preview*: adjust voice tone, decision style, and memory weight, then
test the draft persona in a conversation sandbox before publishing.

The publish step exports your persona as a community package that anyone can
fork and run in 10 seconds.

---

## What lives here

- Draft soul definitions and persona experiments
- Published persona packages
- Test conversation logs (sandbox runs against draft souls)
- Persona gallery exports

---

## Capability dependencies

`agent` · `memory` · `vault`

---

## Navig files backing this space

- `navig/agent/context/SOUL.md`
- `navig/resources/PERSONA.md`

## Viral hook

> Publish your agent persona to the gallery — others can fork and run it in
> 10 seconds.

---

*See `.navig/GENESIS.md` for AI agent bootstrap instructions.*
