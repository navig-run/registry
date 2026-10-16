---
name: folder-intelligence
description: >
  Investigate any project folder and produce a decision dossier — not a file listing. Answers the five
  questions a folder should answer at a glance: what is this, is it valuable, is it safe, is it finished,
  what do I do with it next. Detects real age vs fake freshness (a changed lockfile/cache/log is NOT
  activity), classifies the project type and lifecycle stage, scores strategic value / technical health /
  revival difficulty / archive safety, runs a secret + risk scan, estimates revival effort, and ends with
  a keep / revive / freeze / move-to-dormant / archive / delete-candidate decision plus a folder label.
  Use when the user says "what is this folder?", "investigate this app", "tell me if this project is dead",
  "is this worth keeping?", "prepare this for dormant/apps", "find old projects", "what should I do with
  this repo?", "scan this folder but tell me useful info", or "create a report about this folder". Read-only
  by default — inspects, never modifies/moves/deletes/installs unless the user explicitly asks. On Windows
  use the PowerShell command set; the POSIX set is the fallback (see references/commands.md). Pairs with
  project-migration (this decides; that relocates the survivors).
category: system
tags: [audit, investigation, dormant, archive, filesystem, git, triage]
safety: safe
platforms: [linux, macos, windows]
user_invocable: true
---

# folder-intelligence — turn a folder into a decision

The job is **not** to print a tree. It is to investigate first, then hand the user a verdict they can act
on in ten seconds and still trust six months later. Every report ends in exactly one decision:
**keep · revive · freeze · move to dormant · archive · delete-candidate · needs-deeper-audit.**

## Hard rules

1. **Read-only unless asked.** Never delete, move, rename, install, migrate, format, or run a mutating
   script during an investigation. Prefer inspection over execution. If the user wants a *move* after the
   verdict, hand off to the `project-migration` skill — don't improvise `mv`/`robocopy`.
2. **Never print a secret value.** If you find an API key, token, password, or `.env` with real values,
   report *that a secret exists and where (filename only)* — never the value. Recommend rotation + `.env`.
3. **Investigate before you conclude.** No verdict from the folder name alone. Open the manifests, the
   README, the git log, the timestamps, a sample of source. Base every claim on something you actually saw.
4. **Real activity ≠ fake freshness.** A recently-touched lockfile, `dist/`, `.next/`, cache, log, or
   `node_modules` is NOT progress. Judge activity from **source + docs + git commits**, and say so
   explicitly when a folder only *looks* fresh.
5. **Don't scan noise.** Exclude `node_modules vendor dist build .next .nuxt .cache .git target coverage
   logs tmp` and cap depth (`maxdepth 3`) so a huge tree doesn't drown the signal.
6. **Confidence, not bluff.** Label identity/type/value calls **High / Medium / Low** and say what would
   raise the confidence. Unknown timestamps → say "Unknown", never guess a date.

## Investigation procedure

Run the safe read-only commands in [references/commands.md](references/commands.md) (PowerShell first,
POSIX fallback), then work the checklist. Skip cheaply — not every folder needs every probe.

1. **Identity** — name, probable product name, type (app / prototype / library / CLI / design assets /
   config / dump / archive), domain, main user-facing function, and front-end vs back-end vs full-stack.
   Signals: README, `package.json` / `pyproject.toml` / `Cargo.toml` / `composer.json`, `tauri.conf.json`,
   `vite.config.*`, `next.config.*`, `docker-compose.yml`, `Makefile`, route/title/logo/screenshot names.
2. **Age & activity** — first/last meaningful change, git first/last commit, file-age distribution. Then
   classify: **Fresh** (≤30d) · **Warm** (≤90d) · **Cooling** (≤6mo) · **Dormant** (6–18mo) · **Ancient**
   (>18mo) · **Unknown** (no reliable git/timestamps). Separate real work from fake freshness (rule 4).
3. **Project type** — one label + **confidence** + why. See the rubric in
   [references/rubrics.md](references/rubrics.md).
4. **Tech stack** — languages, frameworks, package managers, build tools, DB/storage, auth, APIs,
   targets (web/desktop/mobile/CLI), deploy platform, tests, styling/design system, state, backend shape.
5. **Important files** — find the ~5–15 that matter, grouped by meaning (entry points · config · data/model
   · UI/core · business logic · build/deploy · tests · docs · assets). For each, one plain sentence on
   *why it matters*. Do not list everything.
6. **Architecture in plain words** — user flow → data flow → main modules → what starts it, stores data,
   renders UI, talks to external services. Non-technical first, technical second.
7. **Completeness** — 0 / 20 / 40 / 60 / 80 / 100%: what works, what's missing, what blocks launch, what's
   cosmetic vs real functionality.
8. **Risk scan** — secrets (rule 2), hardcoded keys, dangerous scripts, stale deps, missing lockfile, no
   tests, unclear build, duplicated source-of-truth, dead routes/imports, missing `.env.example`, large
   files committed by mistake, prod data stored locally, inconsistent architecture, old framework versions.
9. **Dead / duplicated / orphaned** — dead files, duplicate components, unused folders, old experiments,
   generated junk, unclear files — each tagged: `Keep · Move to .dev · Archive · Delete after confirmation ·
   Merge · Refactor`.
10. **Score & decide** — strategic value / technical health / revival difficulty / archive safety (1–10
    each, one line why); revival estimate (1h / 1 day / 1 week / full rewrite / not worth it); then the
    single decision + a folder label + a clean destination path if relevant. Rubrics in
    [references/rubrics.md](references/rubrics.md).

## Required output format

Always produce the report in this structure (fill every section; keep prose tight):

```markdown
# Folder Intelligence Report — <folder name>

## TL;DR
One or two direct sentences: what it is, its state, and the decision.
Project DNA: <one sentence — e.g. "A half-finished Tauri note app with strong UI but no persistence.">

## 1. Identity
- Folder name · Probable project name · Type · Purpose · Confidence: High/Med/Low (why)

## 2. Age & activity
- First activity · Last meaningful activity · Git first commit · Git last commit · Recently-changed files
- Dormancy status: Fresh/Warm/Cooling/Dormant/Ancient/Unknown
- Real vs fake freshness: <is it truly active or only cache/lockfile/build churn?>

## 3. What this project does
Plain words.

## 4. Tech stack
Languages · Frontend · Backend · DB/storage · Build · Package manager · Deploy/desktop/mobile · Tests · Styling

## 5. Most important files
| File | Importance | Why it matters |
|---|---:|---|

## 6. Architecture in plain words
How the parts talk to each other.

## 7. Completeness
Estimated % · What works · What's missing · What blocks production · What's only cosmetic

## 8. Risks & red flags
| Risk | Severity | Evidence (filename only for secrets) | Recommended action |
|---|---:|---|---|

## 9. Dead / duplicated / orphaned
- <item> → Keep / Move to .dev / Archive / Delete after confirmation / Merge / Refactor

## 10. Useful discoveries
Reusable components, assets, docs/specs/prompts, business logic, patterns, promising unfinished features worth extracting.

## 11. Scores
- Strategic value: X/10 — why
- Technical health: X/10 — why
- Revival difficulty: X/10 — why
- Archive safety: X/10 — why
- Revival estimate: 1h / 1 day / 1 week / full rewrite / not worth reviving

## 12. Decision
One of: Keep active · Revive · Freeze · Move to dormant · Archive · Delete candidate · Needs deeper audit — and why.
Suggested label: active / soon-dormant / dormant-app / archive / trash-candidate / revive-candidate / asset-library / prototype
Suggested destination: <path, if relevant>

## 13. Best next actions
3–7 concrete, ordered steps.

## 14. In plain words
What was found · what this folder is for · why it may be useful · what should happen next.
```

When the decision is **Archive**, also offer to drop an `ARCHIVE_NOTE.md` using the template in
[references/rubrics.md](references/rubrics.md) — but only write it if the user says yes (rule 1).

## Final behaviour

Be direct, don't over-explain, don't dump raw trees unless asked. The report must survive time: a user
who has forgotten everything should reopen it in six months and immediately know what the folder is and
what to do with it.
