# GENESIS — Space Bootstrap

> **If you are an AI agent:** this is your first briefing for this space. Read
> it fully before taking any action.  
> **If you are a human:** this is your anchor. It defines what this space is
> *for* and how to let it grow without over-engineering it early.

---

## What This Space Is

This space has no defined purpose yet — that is your first task.

A space is a **context container**. It can be:
- A domain of your life (health, finance, creativity, relationships)
- A project, product, or company
- A team, a community, or a venture
- A stream of thought that hasn't found its form yet

There is no correct shape. The shape emerges from what you need to stop losing
track of.

---

## Eight Global Categories

These are not folders. They are **lenses**.

Use them to think about what belongs in this space — then create only the
folders that make sense *for this specific context*. You do not need all eight.
Start with two or three.

| # | Category | What belongs here |
|---|---|---|
| 1 | **Knowledge & Research** | Notes, saved content, synthesis, references, learning |
| 2 | **Projects & Work** | Active work, specs, deliverables, ship checklists |
| 3 | **Finance & Resources** | Money flows, budgets, invoices, assets, subscriptions |
| 4 | **Communications & Network** | Contacts, threads, outreach, relationship context |
| 5 | **Ops & Systems** | Runbooks, automations, checklists, repeating processes |
| 6 | **Health & Wellbeing** | Physical, mental, energy, habits, tracking |
| 7 | **Creative & Expression** | Writing, ideas, experiments, drafts, design |
| 8 | **Strategy & Planning** | Decisions, roadmaps, goals, open questions, long arcs |

> **Rule:** Do not organize prematurely. Let the categories that attract the
> most inbox drops become the first real folders.

---

## How This Space Grows

```
1. Drop anything into .navig/inbox/      ← capture without friction
2. navig wiki inbox process              ← agent categorizes
3. Weekly review: move processed items  ← 15 min ritual
4. Create folders as patterns emerge    ← no premature structure
```

The inbox is the immune system. Everything enters there. Nothing is lost.

---

## Root Structure

This space keeps a clean root so it can host any project or application
alongside NAVIG metadata.

```
{space-name}/
├── .navig/                  ← all NAVIG metadata (hidden, out of the way)
│   ├── GENESIS.md           ← this file (AI reads first)
│   ├── space.config.json    ← canonical identity manifest
│   ├── inbox.config.json    ← inbox zone config
│   ├── inbox/               ← universal drop zone
│   │   ├── docs/            ← curated documentation
│   │   └── shortcuts/       ← cross-platform shortcut links
│   ├── memory/              ← long-form context, agent memory
│   ├── plans/               ← active plans and phase documents
│   └── state/               ← runtime pins, last known state
├── packages/                ← installable space packages/extensions
├── README.md                ← human-facing identity (visible in repos)
│
│   [your project files go here at root level]
│   [inbox → .navig/inbox    ← optional symlink for quick access]
│   [docs  → .navig/inbox/docs]
│   [plans → .navig/plans]
```

Root symlinks are optional shortcuts. Create them with `setup-links.sh` or
`setup-links.ps1` if you want quick root-level access.

---

## AI Agent: First-Run Protocol

If you are an AI agent and this is the first time this space is being set up,
follow this sequence **before creating any files or folders**:

### Step 1 — Gather identity
Ask the owner these five questions (one at a time or all at once):

1. **What should this space be called?** (short name, lowercase, hyphenated)
2. **Who owns it?** (name or alias — used in `space.config.json`)
3. **What's the one thing you want to stop losing track of?** (free answer)
4. **Which 2–3 of the eight categories apply most to this space?**
5. **Does this space have an existing folder or codebase to attach to?**

### Step 2 — Populate the config
Fill in `space.config.json`:
- Replace `{{space-name}}` with the name from Q1
- Replace `{{owner}}` with Q2
- Replace `{{one-line description}}` with a synthesis of Q3
- Replace `{{ISO-8601 date}}` with today's date

### Step 3 — Write the README
Write `README.md` in the **owner's voice** — one paragraph saying what this
space is for and what problem it solves. Do not make it generic.

### Step 4 — Suggest the first three folders
Based on the categories chosen in Q4, suggest folder names (not paths — just
names). Only suggest. Let the owner confirm before creating.

### Step 5 — Propose a weekly ritual
One sentence: "Every [day], spend [N] minutes [doing what]."
Tie it to the space's purpose.

### Step 6 — Print summary
```
Space: {name}
Owner: {owner}
Purpose: {description}
Starter folders: {list}
Weekly ritual: {ritual}
Config written: .navig/space.config.json ✓
README written: README.md ✓
```

---

## Validation Rules

Before this space is considered ready to publish or share:

- [ ] `space.config.json` has no `{{placeholder}}` values remaining
- [ ] `space.config.json` has `"crossplatform": true`
- [ ] `space.config.json` has no `"plugins"` key — use `"packages"` only
- [ ] All paths in config files are **relative** — no `K:\`, `C:\`, `/home/`
- [ ] `README.md` is not the template — it describes *this specific space*
- [ ] `.navig/GENESIS.md` is present (do not delete — it guides future agents)
