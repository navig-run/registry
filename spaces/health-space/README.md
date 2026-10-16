# Health

Physical and mental health tracking — metrics, protocols, logs, and routines.

A standalone personal space (it pairs well with `human-space`). It holds everything related to body and mind: workout logs, sleep data, mental health check-ins, supplement stacks, protocols, and health-related reference docs.

---

## Structure

```
health-space/
  space.manifest.json
  README.md
  LICENSE
  .gitignore    ← keeps your health data out of git (inbox/, out/, memory, state)
  docs/         ← reference: protocols, research notes, clinician docs
  ops/          ← runbooks: morning routine, check-in protocol, lab prep
  inbox/        ← drop zone: symptoms, screenshots, links to process (ignored by git)
  out/          ← exports: lab results, reports, summaries (ignored by git)
  .navig/
    space.json  ← canonical manifest
    state/
    plans/
    memory/     ← *.example.json seeds (copy to <name>.json on first use)
    inbox/      ← routes.example.yaml (copy to routes.yaml)
```

---

## Suggested Content

| Folder | Examples |
|--------|---------|
| `docs/` | Protocol docs, supplement references, sleep hygiene notes |
| `ops/` | Morning routine runbook, check-in checklist, lab appointment checklist |
| `inbox/` | Links to articles, symptoms log, screenshots of health apps |
| `out/` | Exported lab results, monthly summaries |
| `.navig/memory/` | Long-term health context for AI queries |

---

## Privacy

Health data is sensitive. The shipped `.gitignore` keeps `inbox/`, `out/`, `docs/private/`,
`.navig/memory/` (except the example seeds), `.navig/inbox/` and `.navig/state/` out of
version control — keep it if you put this space under git. Scans of lab results and
prescriptions belong in the encrypted cabinet: `navig cabinet add <file> --category medical`.

## Status

**Planned.** This space ships its structure, runbooks, plans and wiki, but no agents,
skills or workflows yet — the roles in `.navig/wiki/agent-guide.md` are a design, not
shipped definitions. For working health tracking today, use `human-space`
(wellness-tracker: log-health-metric, log-mood, sleep-analysis).
