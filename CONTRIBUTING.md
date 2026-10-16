# Contributing to the NAVIG registry

Welcome. This is the shared knowledge base of the NAVIG ecosystem.
Every skill, prompt, and formation here is peer-reviewed before it merges.

---

## What you can contribute

| Contribution | Where | PR label |
|---|---|---|
| New CLI skill (YAML, `navig skill run`) | `cli-skills/<category>/my-skill.yaml` | `skill` |
| New AI skill (SKILL.md, agent context) | `ai-skills/<id>/SKILL.md` | `skill` |
| New formation | `library/formations/my-formation.yaml` | `formation` |
| New prompt template | `library/prompts/my-prompt.md` | `prompt` |
| New app template | `library/apps/my-app.yaml` | `library` |
| New host template | `library/hosts/my-host.yaml` | `library` |
| New example | `examples/<my-example>/` | `example` |
| New space | `spaces/<id>-space/` | `space` |
| New persona | `personas/<id>/soul.yaml` (+ `soul.md`) | `persona` |
| New block (BLOCK.md, `navig apply`) | `blocks/<id>/BLOCK.md` | `block` |
| Contributor profile | `contributors/<handle>.yaml` | `community` |
| Docs / fix | Anywhere | `docs` / `fix` |

---

## Quickstart — add a skill

```bash
# 1. Fork + clone
git clone https://github.com/navig-run/registry
cd registry

# 2. Copy the skill template
cp cli-skills/_template.yaml cli-skills/<category>/my-skill.yaml

# 3. Fill it in (see SKILL_STANDARD.md for the full spec)
#    Required: name, description, category, version, license
#    Required: at least one commands[] entry
#    Required: at least one examples[] entry
#    Required: agent_hints.when_to_use + output_format

# 4. Validate
navig skill validate cli-skills/<category>/my-skill.yaml

# 5. Test it
navig skill run my-skill:<command>

# 6. Commit + PR
git add cli-skills/<category>/my-skill.yaml
git commit -m "feat(skill): add my-skill — one-line summary"
git push
```

## Quickstart — add a space

```bash
# 1. Start from the canonical skeleton (see spaces/empty-space and spaces/example-space)
navig space init my-space --path spaces/my-space --no-links
cd spaces/my-space

# 2. Fill in .navig/space.json — the canonical manifest:
#    id (= folder name), name, version, tier, status, description,
#    author, license, and only the agents/skills/workflows/formations that exist on disk
# 3. Add a LICENSE (MIT, "Copyright (c) <year> NAVIG contributors" for registry spaces)
# 4. Ship seeds, not state: .navig/memory|inbox|state hold only README.md,
#    .gitkeep or *.example.* files

# 5. Validate
navig space doctor . --no-interactive
cd ../.. && node scripts/check-registry.mjs   # the publish gate: privacy, state, license, identity

# 6. Add a README.md with Install + Use + What It Does sections
# 7. Commit + PR
```

## Quickstart — add a block

A **block** is a verifiable outcome you `navig apply`. See
[BLOCK_STANDARD.md](docs/BLOCK_STANDARD.md) for the full spec and the security floor.

```bash
# 1. Scaffold a valid, runnable starter block
navig block new my-block --into blocks

# 2. Author BLOCK.md (see BLOCK_STANDARD.md). The floor, in one breath:
#    command steps use argv[] (never a shell string) · secrets flow only via
#    secret_env · every command step declares capabilities · a real verify · target: local

# 3. Validate the security floor + lint (this same check runs at apply time)
navig block verify blocks/my-block/BLOCK.md

# 4. Dry-run, then apply for real
navig apply my-block --dry-run
navig apply my-block --input <k>=<v> --approve <destructive-step-id>

# 5. Register it in blocks/registry.json, then commit + PR
git add blocks/my-block/ blocks/registry.json
git commit -m "feat(block): add my-block — <the verified outcome>"
```

---

## Review criteria

PRs are reviewed for:

| Criterion | What we check |
|-----------|---------------|
| **Correctness** | Does it do what it says? Do examples actually work? |
| **Safety** | Are destructive operations marked and guarded? |
| **Clarity** | Would a stranger understand the description in 10 seconds? |
| **Standards** | Skills: [SKILL_STANDARD.md](docs/SKILL_STANDARD.md) · Blocks: [BLOCK_STANDARD.md](docs/BLOCK_STANDARD.md) |
| **No hardcoded secrets** | No IPs, passwords, or tokens — use `{{vault.key_name}}` |

Most PRs are reviewed within 48 h.

---

## Commit message format

```
feat(skill): add git-ops — branch, log, cleanup for any git repo
feat(formation): add dev-studio — coder + reviewer + deployer agents
feat(prompt): add weekly-review — goals, wins, blockers
fix(skill): network-scan — handle missing nmap gracefully
docs: update SKILL_STANDARD with vault_keys example
```

---

## Pull request template

```
## What this adds
Brief: one paragraph.

## Tested on
- Ubuntu 24.04, NAVIG 2.5
- macOS 14, NAVIG 2.5
- Windows 11, NAVIG 2.5 (where applicable)

## Checklist
- [ ] navig skill validate passes
- [ ] At least one examples[] entry
- [ ] agent_hints.when_to_use filled in
- [ ] No hardcoded IPs / passwords / tokens
- [ ] Destructive commands marked risk: destructive
```

---

## SDK Development

The Plugin SDK source lives in `sdk/`:

| Component  | Path                | Publish target     |
|------------|---------------------|--------------------|
| Python SDK | `sdk/python/`       | PyPI `navig-sdk`   |
| TS SDK     | `sdk/typescript/`   | npm `navig-sdk`    |

### Python SDK

```bash
cd sdk/python

# Run tests (no install required — conftest.py handles sys.path)
python -m pytest tests/ -q

# Install editable for manual testing
pip install -e .
```

### TypeScript SDK

```bash
cd sdk/typescript
npm install

# Type-check (must exit 0)
npx tsc --noEmit

# Build dist/
npm run build
```

### Version bumping

Both SDKs share the same version — update these three files together:

| File                               | Field     |
|------------------------------------|-----------|
| `sdk/typescript/package.json`      | `version` |
| `sdk/python/pyproject.toml`        | `version` |
| `community.yaml`                   | `version` |

---

## Local development

```bash
# Validate all CLI skills
find cli-skills -name '*.yaml' | xargs -I{} navig skill validate {}

# Run the publish gate (privacy, seeded state, licenses, identity, JSON)
node scripts/check-registry.mjs

# Install a space from your fork to test it end to end
navig space install github:<your-handle>/registry/spaces/<id>@<branch> --dry-run

# Register as a contributor
cp _template.yaml contributors/<your-handle>.yaml
# Fill in your details, then add to your PR
```

---

## Code of conduct

Be kind. This is a community of builders working in the open.

*We follow the [Contributor Covenant](https://www.contributor-covenant.org/version/2/1/code_of_conduct/).*

