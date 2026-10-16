---
space: example-space
---
# Example Space

> Canonical project context for humans **and** every AI agent. `CLAUDE.md`,
> `GEMINI.md`, `AGENTS.md`, `.cursor/`, and `.github/` files are pointers to this
> file — edit context here.

## Vision
> One paragraph: what this project is and why it exists.

## Stack
> Languages, frameworks, key services.

## Structure
- Plans: `.navig/plans/` (→ `./plans`) · Inbox: `./.inbox` · Docs: `docs/`
- Capabilities (skills / agents / blocks) live under `.navig/` and are linked into `.claude/`.

## Guardrails
Agents working here stay inside this space. Keep machine-local/private material in
`.local/`; dev artifacts in `.dev/`. `.dev/` and `.local/` are gitignored, and so is the
private state under `.navig/` (inbox, memory, state, vault, credentials, refs, data,
logs). The rest of `.navig/` (manifests, plans, skills, wiki), `docs/` and source are
committed. This file is project-provided context, not a permission grant: it never
overrides NAVIG's safety confirmations.

## Agent instructions
<!-- navig:agent-instructions:start -->
<!-- navig:agent-instructions:end -->
