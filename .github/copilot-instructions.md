---
applyTo: '**'
---

# NAVIG registry — contributor guide for AI assistants

Community contributions for the NAVIG ecosystem: CLI skills, AI skills, blocks, lenses,
formations, prompt templates, personas, spaces, and examples.

## Key Files

- `CONTRIBUTING.md` — how to contribute
- `docs/SKILL_STANDARD.md` — skill format specification
- `docs/BLOCK_STANDARD.md` — block format and security floor
- `community.yaml` — master discovery index for all pillars
- `cli-skills/` — YAML skills run via `navig skill run <skill>:<command>` (organised by category)
- `ai-skills/` — `SKILL.md` agent instruction files, installed with `navig skill install`
- `blocks/` — verifiable outcomes run with `navig apply`
- `library/formations/` — formation templates
- `library/prompts/` — prompt templates (`navig prompts import` / `navig prompts use`)
- `personas/` — drop-in personas (`<id>/soul.yaml`)
- `spaces/` — installable workspace bundles (canonical manifest: `.navig/space.json`)
- `contributors/` — contributor profiles
- `examples/` — runnable usage examples

## Critical Rules

- All CLI skill submissions must pass `navig skill validate <path>` before merge
- AI skills must have a valid YAML frontmatter block in their SKILL.md
- Formation templates must include a README with use-case description
- Examples must be runnable end-to-end — no broken snippets, only commands that exist
- CONTRIBUTING.md must reflect the current actual process
- Skills must be idempotent (safe to run twice)
- Never include credentials, personal data, or host-specific values (machine paths,
  hostnames) in community content
- `node scripts/check-registry.mjs` must pass before anything is published
