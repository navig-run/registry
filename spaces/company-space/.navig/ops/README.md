# Company Root Ops

Root-level operational runbooks for the company space. For subspace-specific ops, see `spaces/ops/ops/README.md`.

---

## Deploy Checklist

```
[ ] Review open items in inbox/
[ ] Confirm active project status in spaces/projects/
[ ] Check ops subspace for any scheduled runbook triggers
[ ] Review .navig/plans/ for current phase status
[ ] Clear out/ of stale deliverables (archive anything >30 days)
```

---

## Incident Response (Quick Reference)

1. **Identify** — what is failing, what is the blast radius?
2. **Communicate** — notify affected parties immediately
3. **Contain** — stop the bleeding before fixing the root cause
4. **Resolve** — apply fix; document in `spaces/ops/docs/`
5. **Post-mortem** — write a brief in `spaces/ops/inbox/` for processing

Detailed runbook: `spaces/ops/ops/README.md`

---

## Vendor & Contact List

Store in `docs/vendors.md` (create as needed). Keep phone numbers, contract terms, and escalation contacts here — not in email.

---

## Recurring Workflows

| Cadence | Workflow |
|---------|---------|
| Weekly | Review `inbox/`, update project status |
| Monthly | Update `.navig/memory/` with company context |
| Quarterly | Review `plans/` and `.navig/plans/` against OKRs |

---

*Add company-specific automation scripts here as `.ps1` / `.sh` / `.yaml` files.*
