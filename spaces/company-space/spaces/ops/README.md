# Operations

Day-to-day operational tasks, runbooks, SOPs, incident response, and recurring workflows.

This subspace belongs to `company-space`. It is the canonical location for all operational procedures — how the company runs, responds to incidents, onboards vendors, and handles recurring tasks.

---

## Structure

```
spaces/ops/
  space.manifest.json
  README.md
  docs/         ← SOPs, process documentation, vendor contracts
  ops/          ← executable runbooks and checklists
  inbox/        ← incoming incidents, requests, tasks
  out/          ← closed incidents, resolved tickets, exports
  .navig/
    space.json
    state/
    plans/
    memory/
```

---

## Runbook Categories

| Category | Location | Examples |
|----------|---------|---------|
| Incident response | `ops/` | Outage runbook, data breach response |
| Onboarding | `docs/` | New hire checklist, vendor onboarding SOP |
| Security | `ops/` | Access review checklist, key rotation runbook |
| Infrastructure | `ops/` | Deploy runbook, rollback procedure |
| Finance | `docs/` | Invoice process, expense approval |
