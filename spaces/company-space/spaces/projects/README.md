# Projects

Active company projects — specs, milestones, decisions, and delivery tracking.

This subspace belongs to `company-space`. Every active project lives here as a doc, folder, or structured set of files. Finished projects move to `out/`.

---

## Structure

```
spaces/projects/
  README.md
  docs/         ← project specs, ADRs, design docs, briefs
  ops/          ← project delivery runbooks and checklists
  inbox/        ← incoming: new project requests, scoping docs
  out/          ← delivered: shipped projects, closed milestones
  .navig/
    space.json
    space.manifest.json
    state/
    plans/      ← active sprint, milestones, backlog
    memory/     ← project history and context for AI
```

---

## Project Intake Convention

When a new project lands:
1. Drop spec/brief in `inbox/`
2. Review and scope → promote to `docs/<project-name>/`
3. Create milestone plan in `.navig/plans/`
4. Track delivery in `ops/`
5. On completion: archive to `out/<project-name>/`

---

## ADR Convention

Architecture Decision Records live in `docs/<project-name>/decisions/`. Format:
- `001-decision-title.md`
- Fields: Status, Context, Decision, Consequences
