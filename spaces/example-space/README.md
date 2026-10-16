# example-space

The **canonical structure** every NAVIG space gets from `navig space init`. Clone it, read it,
or use it as a template. Everything here is produced automatically by:

```bash
navig space init my-space                              # → ~/.navig/spaces/my-space
navig space init company --path ~/spaces/company       # init at any directory
```

## Structure

```
example-space/
  .navig/                  # the space "bones" — identity, plans, capabilities
    space.json             # canonical manifest — NAVIG reads this first
    space.config.json      # legacy identity + path map, kept in sync for older tools
    GENESIS.md
    plans/                 # ← canonical plans (Navig reads these into the LLM context)
      CURRENT_PHASE.md     #   what you're doing now (read first)
      VISION.md
      ROADMAP.md           #   Now / Next / Later
      DEV_PLAN.md          #   Active / Deferred / After MVP
    inbox/                 # ← drop ANY file here to capture it         (private, gitignored)
      docs/
      shortcuts/
    memory/                # long-term memory                            (private, gitignored)
    state/                 # runtime state                               (private, gitignored)
    wiki/                  # knowledge base
  .dev/                    # dev artifacts (reports, logs, audits, prompts, experiments,
                           #   archive, notes, screenshots, temp) — GITIGNORED
  .local/                  # machine-local / private — GITIGNORED
                           #   (dumps, credentials, private-notes, machine-config, scratch)
  docs/                    # curated docs (architecture, setup, operations,
                           #   decisions, reference, archive). NOT plans.
  plans  -> .navig/plans   # cross-platform root link (junction on Windows, symlink on POSIX)
  .inbox -> .navig/inbox   # cross-platform root link (hidden, like .navig)
  .gitignore               # what stays private — see below
  LICENSE
  README.md
  NAVIG.md                 # canonical project context for humans and agents
  CLAUDE.md                # thin pointer that imports NAVIG.md
```

`.dev/` and `.local/` are created by `navig space init` on your machine; they are not part of
this example because they are never committed.

## What is committed and what stays private

`.navig/` is **committable** — plans, skills, wiki and the manifests belong in version
control. Only its private state is ignored: `.navig/inbox/`, `.navig/memory/`,
`.navig/state/`, `.navig/vault/`, `.navig/credentials/`, `.navig/refs/`, `.navig/data/`,
`.navig/logs/` and key files. `.dev/`, `.local/` and the root links are ignored too.
The `.gitignore` in this folder is exactly what `navig space init` writes; `navig wire`
keeps the block between its markers up to date.

If you publish a space for others to install, ship neutral seeds as `*.example.*` files in
`memory/`, `inbox/` and `state/`, never your own state.

## The root links

`./plans` and `./.inbox` are convenience links into `.navig/` so you (and agents) can reach the
two things you touch most without typing `.navig/`. `navig space init` creates them
automatically — **NTFS junctions on Windows (no admin needed)**, symlinks on macOS/Linux.

Cloned this space manually instead of using `init`? Recreate the links once:

```bash
./setup-links.sh        # macOS / Linux
.\setup-links.ps1       # Windows (junctions — no admin)
```

## Why plans live in `.navig/plans`

Plans are **state**, not documentation, so they live with the rest of the space state in
`.navig/` and flow into the agent's context. `docs/` is for curated, human-facing documentation —
it deliberately has **no** `plans/` subfolder.
