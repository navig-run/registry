# GENESIS — Forge Space (agent briefing)

> **If you are an AI agent:** read this before acting in this space.
> The human-facing purpose lives in [`../GENESIS.md`](../GENESIS.md) and [`../README.md`](../README.md).

**Space:** `forge-space` · **Tier:** studio · **Status:** planned

Status **planned**: the features in `GENESIS.md` are the design target. Do not tell the owner they work.

## What this space ships today

- Purpose and design target: `GENESIS.md`, `README.md`
- Seed goals and context: `.navig/memory/*.example.json` (copy them to their live
  names on first run, see `.navig/memory/README.md`)
- Inbox routes: `.navig/inbox/routes.example.yaml` (see `.navig/inbox/README.md`)
- Plans: `.navig/plans/CURRENT_PHASE.md`, `.navig/plans/DEV_PLAN.md`
- Context and runbooks: `.navig/context.md`, `.navig/ops/README.md`, `.navig/wiki/`

It ships **no agents, skills, workflows or formations**: `.navig/space.json` lists none.

## First run

1. Copy the memory and inbox examples to their live names.
2. Read `.navig/plans/CURRENT_PHASE.md` and work only on its open items.
3. Capture input through the inbox: drop files in `.navig/inbox/`, then run
   `navig wiki inbox process`.
4. Check the space with `navig space doctor`.

## Rules

- Do not describe a feature as working until it exists on disk and is listed in
  `.navig/space.json`.
- New capability goes in `.navig/skills/`, `.navig/store/agents/`,
  `.navig/store/workflows/` or `.navig/store/formations/`, and is added to
  `.navig/space.json` in the same change.
- Keep every path relative to the space; never write machine-specific paths.

## Dream-compiler pattern (design target)

The intended Forge flow: describe a capability in plain English, get a package skeleton.

1. The owner describes the capability ("monitor my GitHub repos and send a daily digest").
2. Decompose it into tools, skills, config schema and integration points.
3. Scaffold a plugin skeleton with `navig plugin new` (or a skill with `navig skill new`).
4. Fill the implementation, or propose it with the gaps clearly marked.
5. Validate it (`navig skill validate` / `navig plugin inspect`) before anyone installs it.

Narrate each step; never build silently.
