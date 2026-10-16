# Human Space — Personal Ops

Runbooks and checklists for personal life automation. Keep procedures here so they're repeatable, not reinvented.

---

## Weekly Review Checklist

```
[ ] Process .navig/inbox/ (triage all items)
[ ] Review .navig/plans/ — mark completed tasks, update phases
[ ] Check spaces/health/ — log metrics if not auto-captured
[ ] Check spaces/growth/ — log progress on active habits/courses
```

---

## Inbox Triage Protocol

1. Open `.navig/inbox/`
2. For each item: categorize → move to the correct folder under `spaces/`
3. Items with no clear home → `docs/` with a date prefix
4. Run: `navig wiki inbox process` for AI-assisted sorting

---

## Backup Runbook

Set your backup location once, e.g. `navig config set backup.root <your-backup-dir>`
(below shown as `<backup-root>`).

1. Back up `.navig/memory/` → cloud or `<backup-root>/human/`
2. Back up `docs/` → same
3. Back up `.navig/plans/` → same
4. Local data areas (`spaces/health`, `spaces/growth`, `spaces/bureau`): same
5. Documents (IDs, medical, insurance): `navig cabinet backup -o <backup-root>/human/cabinet`
   — one encrypted file with its own passphrase; `navig cabinet verify` first if in doubt

---

## Habit Automation Hooks

Store habit-tracking automation scripts here as `.ps1` or `.sh` files. Pair with `.navig/plans/` for scheduling.

Example:
```
ops/
  daily-review.ps1
  weekly-review.ps1
  habit-log.sh
```
