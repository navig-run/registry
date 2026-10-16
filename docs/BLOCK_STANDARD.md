# BLOCK_STANDARD — Authoring Guide

A **Block** is an installable, executable, **verifiable outcome** — *apply an outcome, proven by a
verified receipt*. Where a Skill teaches the agent *how*, a Block *does the thing* end to end and
then runs a machine check and writes a receipt. Run one with `navig apply <id>`.

A Block is a folder containing a `BLOCK.md` whose **YAML frontmatter is the machine spec** (typed
inputs, ordered steps, a verify, provenance) and whose **markdown body is the human how-to article**
(also the `SKILL.md` body foreign agents read — every installed Block emits a skill shim, so Blocks
ride Skill discovery).

The authoritative contract is `navig-core` at `navig/blocks/loader.py` (`validate_block`), summarised
in `blocks/schema.yaml`. This guide is the human-facing version of the same rules; where they ever
disagree, the loader wins.

---

## Anatomy of a `BLOCK.md`

```markdown
---
# ── Identity (required) ──────────────────────────────────────────────────────
id: my-block          # kebab-case, MUST equal the folder name
spec_version: 1       # only 1 is accepted; unknown versions are rejected loudly
name: My Block        # human title
version: 1.0.0        # semver
category: ops         # ops | dev | data | content | security | …
license: MIT
description: One sentence naming the VERIFIED OUTCOME (what exists/is true when it finishes).
author: your-handle
tags: [backup, ssh]
allowed-tools: Bash   # Claude-Code compatibility hint for the generated skill shim
target: local         # only 'local' during the preview — remote is a later stage

# ── Inputs (typed variables the operator supplies) ───────────────────────────
inputs:
  - key: host
    type: string      # string | int | number | boolean | path | enum | secret
    label: Database host (a configured navig host)
    required: true
    default: production
  - key: environment
    type: enum
    values: [staging, production]   # required for enum
    default: staging
  - key: api_token
    type: secret      # NEVER interpolated into argv/content — see the security floor
    vault: my_service_token         # hint: which vault key backs it

# ── requires (fail-fast preconditions) ───────────────────────────────────────
requires:
  tools: [navig]      # binaries that must be on PATH; navig block doctor checks these
  plugins: []         # navig plugins that must be installed
  permissions: []     # capabilities the operator must have granted
  detect: []          # stack-detection hints (e.g. a file that must be present)

# ── Steps (ordered; the runner executes them top to bottom) ──────────────────
steps:
  - id: set-host
    kind: command                   # materialize | command | skill | prompt | instruction | block
    safety: safe                    # descriptive only — the runner computes real risk from capabilities
    capabilities: [exec:navig]      # REQUIRED on command steps
    network: none                   # none | required
    argv: [navig, host, use, "{{inputs.host}}"]   # argv list — NEVER a shell string

  - id: dump
    kind: command
    safety: destructive
    capabilities: [remote, exec:navig]
    network: required
    argv: [navig, db, dump, "{{inputs.db_name}}", "-o", "{{inputs.output_file}}"]
    # deliver a secret as an env var — the ONLY way a secret may reach a step:
    secret_env: { MY_TOKEN: inputs.api_token }
    # capture a value out of stdout into an output key:
    capture: { dump_id: "backup id: (\\S+)" }

# ── verify (the machine success criterion — the "proof") ─────────────────────
verify:
  kind: file_exists                 # none | file_exists | command
  level: self-check                 # self-check | external-check
  path: "{{workdir}}/{{inputs.local_dir}}/{{inputs.output_file}}"

# ── outputs / receipt (provenance) ───────────────────────────────────────────
outputs:
  - key: dump_id
    type: string
    from: dump                      # the step that captured it
receipt:
  redact: []                        # extra values to redact from the receipt beyond secrets
---
# Snapshot a remote database to your workspace     ← the human how-to starts here

Explain, in plain words, what applying this block DOES and what the verified
outcome is. This body is also the SKILL.md a foreign agent reads.

## Steps
1. **set-host** — point navig at `host`.
2. **dump** — export the database *(destructive — needs `--approve dump`)*.

## Apply
\`\`\`
navig apply my-block --input host=production --approve dump
\`\`\`
```

---

## Fields

| Field | Required | Notes |
|---|---|---|
| `id` | ✅ | kebab-case; **must equal the folder name** |
| `spec_version` | ✅ | must be `1` |
| `name` · `version` · `category` · `license` | ✅ | version is semver |
| `description` | — | one sentence naming the **verified outcome** — this is what sells the block |
| `target` | — | defaults to `local`; **only `local` is accepted** in the preview |
| `inputs` | — | typed; see below |
| `requires` | — | `tools[] · plugins[] · permissions[] · detect[]` — checked by `navig block doctor` |
| `steps` | — | ordered; each has a unique `id` |
| `verify` | — | the machine proof; defaults to `kind: none` (records that no check exists) |
| `outputs` | — | `{key, type, from}` — values captured from steps |
| `receipt` | — | `redact[]` extra values; `sign` is Stage 3 |
| `marketplace` | — | **present only when paid** — its absence means free (see the funnel below) |

### Input types
`string · int · number · boolean · path · enum · secret`. Extra keys: `pattern` (regex for string),
`values` (**required** for enum), `must_exist` (for path), `default`, `vault` (hint for secret).

### Step kinds
| Kind | Does | Key fields |
|---|---|---|
| `materialize` | write a file into the workdir | `dest` (required) + `src` **or** `content` |
| `command` | run a program | `argv` (required, a **list**), `capabilities` (required), `network`, `secret_env`, `capture` |
| `skill` | run an installed skill | `skill` (id) |
| `prompt` / `instruction` | hand text to the agent | `text` |
| `block` | compose another block | `use` (target id) + `inputs` |

### verify kinds
`none` (no machine check — honest, but weakest) · `file_exists` (needs `path`) · `command` (needs
`argv`; assert with `expect: {exit_code, output_contains, output_regex}`). `level: external-check`
means the proof comes from a system outside this machine (a deploy that a remote healthcheck confirms);
`self-check` means the machine verified its own local result.

### Template tokens
`{{inputs.x}}` · `{{outputs.x}}` · `{{workdir}}` · `{{config_dir}}`. Every `{{inputs.*}}`/`{{outputs.*}}`
token **must be declared** or validation fails. `{{workdir}}` and `{{config_dir}}` are always available.
`{{vault.*}}` is a **hard error** anywhere — secrets never travel as template tokens.

---

## Security floor (enforced at apply time by `validate_block`)

These are not style suggestions — a block that violates any of them **will not run**:

1. **`command` steps take `argv[]`, never a shell string.** `argv: [navig, db, dump, "{{inputs.db}}"]`,
   not `argv: "navig db dump {{inputs.db}}"`. Shell is never invoked, so there is no injection surface.
2. **Secrets flow ONLY via `secret_env`.** A `secret` input must never appear in `argv`, in
   materialized `content`, or as `{{vault.x}}`. Deliver it as an env var:
   `secret_env: { MY_TOKEN: inputs.api_token }`.
3. **Every `command` step must declare `capabilities`.** The runner computes the **effective risk**
   from capabilities (e.g. `remote`, `delete`, `exec:navig`), *not* from the self-asserted `safety`
   label — so a step that lies `safety: safe` while declaring `delete` is still gated as destructive.
4. **Destructive steps require a named `--approve <step-id>`.** A blanket `--yes` is **not** enough for
   a step whose capabilities are destructive; the operator must approve that step by id.
5. **Materialized writes are confined to the workdir / config dir.** A `materialize` `dest` outside
   them is refused.
6. **`target` must be `local`.** Remote blocks are a later stage.

Run `navig block verify <path>` — it reports hard errors (the floor above) **and** advisory lint
(e.g. a step that runs a binary not listed in `requires.tools`, which would otherwise fail at apply
time with "command not found" instead of a fail-fast install hint).

---

## The receipt — why a block beats a script

Every apply writes a **receipt**: a terminal artifact binding *what ran* to *what was proven* — the
block digest, runner version, the verification level and evidence, redacted inputs/outputs, and any
child-block receipts. That is the difference between "I ran some commands" and "here is proof the
outcome is real". Secrets are redacted automatically; add anything else sensitive to `receipt.redact`.

---

## The funnel — Skills are free, Blocks are the paid tip

Skills carry **no** `marketplace` block — they are the free front door. Blocks are where verified
outcomes + trust + support live, so a Block *may* carry a `marketplace` block:

```yaml
marketplace:
  pricing_model: buy_once     # free | tier | buy_once
  included_in_tier: plus      # plus | max | team | enterprise
  price_cents: 1900
  currency: usd
```

**No `marketplace` block = free.** Never price a Skill. During the preview, Blocks install first-party
only.

---

## Quickstart — add a block

```bash
# 1. Fork + clone
git clone https://github.com/navig-run/registry
cd community

# 2. Scaffold a valid, runnable starter block (writes a complete BLOCK.md)
navig block new my-block --into blocks
#    or copy the reference block:  cp -r blocks/db-snapshot blocks/my-block
#    (either way: the folder name MUST equal the id)

# 3. Author BLOCK.md against this guide. The floor, in one breath:
#    argv lists (never shell) · secrets via secret_env · capabilities on every command
#    · a real verify · target: local

# 4. Validate the security floor + lint
navig block verify blocks/my-block/BLOCK.md

# 5. Dry-run, then apply for real
navig apply my-block --dry-run
navig apply my-block --input host=staging --approve <destructive-step-id>

# 6. Register it + commit
#    add an entry to blocks/registry.json, then:
git add blocks/my-block/ blocks/registry.json
git commit -m "feat(block): add my-block — <the verified outcome>"
git push
```

Reference block to copy from: [`blocks/db-snapshot/BLOCK.md`](../blocks/db-snapshot/BLOCK.md) — a
complete, floor-compliant example (typed inputs, a destructive step gated by `--approve`, a
`file_exists` verify that confirms the dump actually landed).

---

## Validation

```bash
navig block verify blocks/<id>/BLOCK.md    # hard errors (floor) + advisory lint
navig block doctor blocks/<id>/BLOCK.md    # are the required tools/plugins present?
navig apply <id> --dry-run                 # resolve inputs + plan steps without running them
```

A block that `navig block verify` rejects will not be accepted — the same check runs at apply time.
