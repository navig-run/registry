# NAVIG Registry

> The official index of installable NAVIG content — **spaces, skills, personas, blocks,
> lenses and templates.** Open source (MIT). One command to install.

```bash
# A whole workshop: agents, skills, plans and memory for one domain
navig space install github:navig-run/registry/spaces/homelab-space

# An AI skill (the agent loads it when a task matches)
navig skill install github:navig-run/registry/ai-skills/summarise-url

# A persona or any other asset
navig install add github:navig-run/registry/personas/senior-engineer
```

This repository was called `navig-run/community` until 2026-10-16. NAVIG releases from
that date on read `navig-run/registry`, and still accept specs that name the old repo.

---

## What is in here

```
registry/
  spaces/        44 spaces — 41 listable, 3 internal templates   (spaces/registry.json)
  ai-skills/     SKILL.md instruction skills the agent pulls in   (ai-skills/registry.json)
  cli-skills/    YAML command skills, by category                 (cli-skills/registry.json)
  personas/      persona.yaml + soul files                        (personas/registry.json)
  blocks/        outcomes you apply, proven by a receipt          (blocks/registry.json)
  lenses/        small browser userscripts                        (lenses/registry.json)
  library/       copy-and-adapt templates: formations, prompts, app and host configs
  examples/      worked examples: hello-app, workstation, dev-studio
  sdk/           Python and TypeScript plugin SDKs
  docs/          the standards: SKILL_STANDARD.md, BLOCK_STANDARD.md
  contributors/  contributor profiles
  community.yaml machine-readable index of every pillar
```

---

## Spaces

A **space** is a whole workshop: a folder with a `.navig/` holding the agents, skills,
workflows, plans and memory for one domain. Install one and switch to it:

```bash
navig space install github:navig-run/registry/spaces/finance-space
navig space use finance-space
```

| Status | Count | Meaning |
|---|---|---|
| `active` | 24 | Ships working agents, skills and workflows |
| `planned` | 15 | A designed scaffold; capabilities are still to be built |
| `labs` | 2 | Experimental, opt-in (multi-agent formations) |

The full list, with tiers, taglines and prices, is
[`spaces/registry.json`](spaces/registry.json); [`spaces/README.md`](spaces/README.md)
describes each space.

**What you get on install.** Every space ships a canonical `.navig/space.json`, a `LICENSE`,
and only *example* state: files under `.navig/memory/`, `.navig/inbox/` and `.navig/state/`
are `*.example.*` templates. Your own memory, inbox and state are created on first use and
stay on your machine — a later `navig space install` never overwrites them.

---

## Skills

**AI skills** (`ai-skills/<id>/SKILL.md`) are knowledge the agent pulls in: they teach it
*how* to do a kind of task, and load when a request matches their description. They are
Claude Code-compatible. **All skills are free.**

```bash
navig skill install github:navig-run/registry/ai-skills/notion
navig skill list
```

**CLI skills** (`cli-skills/<category>/<id>.yaml`) describe a set of commands for one tool
(git, docker, network, security, system health).

---

## Personas

A persona is the voice and manner the agent speaks in — `persona.yaml` plus a soul file.

```bash
navig install add github:navig-run/registry/personas/senior-engineer
```

---

## Blocks

A **block** is an installable, executable, verifiable outcome — *apply an outcome, proven by
a verified receipt.* A block composes ordered steps (`materialize · command · skill ·
prompt · instruction · block`), runs a machine check at the end, and writes a receipt.

```bash
navig install add block:navig-run/registry/blocks/db-snapshot
navig apply db-snapshot
```

Only first-party blocks from this repository are trusted during the preview. The spec and
security floor are in [docs/BLOCK_STANDARD.md](docs/BLOCK_STANDARD.md).

---

## Harbor Bay pricing

Registry entries may carry an optional `marketplace` block:

```json
"marketplace": { "pricing_model": "buy_once", "included_in_tier": "plus", "price_cents": 500, "currency": "usd" }
```

- **No `marketplace` block = free.** Skills and personas are always free.
- `pricing_model` is `free`, `tier` or `buy_once`; `buy_once` needs a positive `price_cents`.
- `included_in_tier` (`plus`, `max`, `team`, `enterprise`) is the Harbor tier that includes
  the item at no extra cost.
- Items that are `planned`, `labs` or `internal` are never sold.
- A space's `tier` (personal / work / studio / platform / community / labs) is a content
  category and has nothing to do with price.

---

## Contributing

1. Copy a template: `spaces/empty-space/`, `cli-skills/_template.yaml`, or an existing
   `ai-skills/<id>/SKILL.md`.
2. Validate: `navig skill validate <path>` for skills, `navig space doctor <path>` for spaces.
3. Run the publish gate — it must pass:

   ```bash
   node scripts/check-registry.mjs
   ```

   It refuses machine-specific paths, personal data, secrets, seeded user state,
   unparseable JSON, catalog drift and missing licenses.
4. Open a pull request. Add yourself under `contributors/` with your first merged change.

Full guide: [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Links

| | |
|---|---|
| NAVIG core (CLI + daemon) | [github.com/navig-run/core](https://github.com/navig-run/core) |
| Website | [navig.run](https://navig.run) |
| Skill standard | [docs/SKILL_STANDARD.md](docs/SKILL_STANDARD.md) |
| Block standard | [docs/BLOCK_STANDARD.md](docs/BLOCK_STANDARD.md) |
| Showcase | [SHOWCASE.md](SHOWCASE.md) |

License: MIT — see [LICENSE](LICENSE).
