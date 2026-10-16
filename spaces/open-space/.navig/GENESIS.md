# GENESIS — Open Space (agent briefing)

> **If you are an AI agent:** read this before acting in this space.
> The human-facing purpose lives in [`../GENESIS.md`](../GENESIS.md) and [`../README.md`](../README.md).

**Space:** `open-space` · **Tier:** community · **Status:** planned

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

## Workflow sharing (design target)

Open Space is meant to become the place where users publish, discover and fork each
other's workflows. There is **no publish or marketplace command yet**. Today:

- A repeatable, shareable outcome is a **Block**: author one with `navig block new <id>`,
  check it with `navig block verify <id>`, run it with `navig apply <id>`.
- Session history comes from the blackbox: `navig blackbox timeline`.
- Sharing a Block means publishing its folder (for example to the community registry);
  others install it with `navig install add block:<owner>/<repo>/<path>`.

When the owner asks how to share something, explain these steps honestly instead of
promising a one-click marketplace.
