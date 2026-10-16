# folder-intelligence — classification & scoring rubrics

Compact decision aids for steps 2–3 and 10. Every call carries a **confidence** and a one-line *why*.

## Project-type rubric (step 3)

Pick exactly one, then justify with evidence you actually saw.

| Type | Tells |
|------|-------|
| **Production app** | real users implied, CI/CD, tests, deploy config, semver releases, changelog |
| **Prototype** | works partially, no tests, TODO-heavy, single author, "wip" commits |
| **Experiment** | one narrow idea, throwaway naming, no docs, abandoned after a spike |
| **Template / starter** | generic names ("my-app"), placeholder copy, unmodified scaffold |
| **Library / package** | exports an API, `main`/`exports`/`[lib]`, published or publishable, no app entry |
| **Design asset folder** | images/figma/exports, no or trivial code |
| **Config / tooling** | dotfiles, scripts, CI, no product surface |
| **Dump / mixed** | unrelated things in one folder, no single purpose |
| **Abandoned project** | had real ambition, dead >18mo, unfinished, no owner signal |
| **Archive candidate** | complete-ish but inactive, safe to freeze |
| **Unknown** | not enough signal — say what's missing |

## Age / dormancy (step 2)

Fresh ≤30d · Warm ≤90d · Cooling ≤6mo · Dormant 6–18mo · Ancient >18mo · Unknown (no git/timestamps).
Judge from **source + docs + commits**, never from lockfile/build/cache/log churn (that's fake freshness).

Dormancy decision (step 12) maps activity + value:

- **Active** — recent meaningful commits/files + clear purpose.
- **Soon dormant** — useful but stalled, unfinished, or ownerless.
- **Dormant** — old but still valuable/understandable.
- **Archive** — safe to keep, not worth active attention.
- **Delete candidate** — duplicate, generated, broken, or no clear value.
- **Revive candidate** — old but strategically valuable and technically salvageable.

## Completeness scale (step 7)

`0%` empty/skeleton · `20%` rough idea · `40%` prototype · `60%` usable but incomplete ·
`80%` near-production · `100%` production-ready. Distinguish *what works* from *what's cosmetic*.

## The four scores (step 10) — 1–10, one line each

- **Strategic value** — does the concept fit where the product/portfolio is going? Unique idea? Reusable IP?
- **Technical health** — code quality, tests, docs, dependency freshness, build clarity, architecture consistency.
- **Revival difficulty** — how hard to get it running & shippable again (deps, dead code, missing pieces). *Higher = harder.*
- **Archive safety** — how safe to freeze as-is (after the secret check). *Higher = safer.*

## Revival estimate (step 10)

`Revive in 1 hour` · `Revive in 1 day` · `Revive in 1 week` · `Needs full rewrite` · `Not worth reviving`.
Anchor it in the concrete gaps you found, not a vibe.

## Heat map (optional, when it clarifies)

Tag folders: **Hot** (core code) · **Warm** (useful support) · **Cold** (old/unclear) ·
**Trash-risk** (generated/useless) · **Sensitive** (secrets/config/private data).

## Suggested labels & destinations (step 12)

Label: `active · soon-dormant · dormant-app · archive · trash-candidate · revive-candidate ·
asset-library · prototype`. Suggest a destination only when a move is the recommendation, phrased
against the user's own project layout — e.g. `<projects-root>/apps/...` (active),
`<projects-root>/dormant/apps/...` (dormant), `<projects-root>/archive/...` (archive),
`<projects-root>/.dev/...` (junk). Ask where their projects root is; never assume a drive or
folder. The actual move is the `project-migration` skill's job, not this one.

## ARCHIVE_NOTE.md template (write only if the user says yes)

When the decision is **Archive** and the user approves, drop this at the folder root so a future reader
can revive it cold:

```markdown
# Archive Note — <project>

## What this is
<one-paragraph description>

## Why archived
<reason — dormant / superseded / experiment concluded / low value>

## Last known state
<what worked, what didn't, completeness %>

## How to revive
<exact commands to install + run, and the first thing to fix>

## Important files
<the 3–8 files that matter and why>

## Secrets / risks
<any secret to rotate — filename only, never the value>
```

## README stub template (offer when a folder has no README)

```markdown
# <project>

**Status:** <active / prototype / dormant / archived> · **Completeness:** ~<X>%

## What it is
<one sentence>

## Run it
<install + run commands>

## Where things live
<entry point · data layer · config>

## Known gaps
<what's missing / what blocks production>
```
