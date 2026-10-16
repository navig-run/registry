# Operations Runbooks

Executable runbooks and checklists for the operations subspace.

---

## Incident Response Runbook

```
[ ] Identify scope and severity (P1 / P2 / P3)
[ ] Notify: (add contact list here)
[ ] Contain: isolate affected component
[ ] Investigate: pull logs, confirm root cause
[ ] Resolve: apply fix or workaround
[ ] Communicate: send update to affected parties
[ ] Post-mortem: write brief → inbox/ for processing
[ ] Close: move to out/ with resolution summary
```

---

## Access Review Checklist (Quarterly)

```
[ ] Audit active user accounts
[ ] Remove departed team members
[ ] Rotate shared credentials
[ ] Review third-party app permissions
[ ] Update docs/access-policy.md if anything changed
```

---

## Deploy Runbook

1. Confirm build passes (CI green)
2. Review diff with team
3. Deploy to staging — smoke test
4. Deploy to production — monitor for 30 min
5. Entry in `out/` with deploy timestamp and version

---

*Add environment-specific scripts here as `.sh` / `.ps1` / `.yaml` files.*
