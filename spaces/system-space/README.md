# System — OS & Filesystem Operator Space

A navig space that **knows Windows and the filesystem deeply** and uses that knowledge
to **inventory, move, migrate, dedupe-check and clean up files — safely, at any scale.**
Born from real bulk operations (multi-TB drive migrations, long-path backup purges,
lock-breaking, size-based library classification).

## What it does

The engine `bin/system.ps1` implements these verbs today:

| Capability | Engine verb |
|---|---|
| Inventory / sizing / audit | `inventory`, `size`, `broken`, `dupes` |
| Safe move / migrate | `move`, `migrate`, `trash` |
| Long-path delete | `purge` |
| Reclaim / clean up | `reclaim` |

Purpose-based classification lives in `tools/classify-by-purpose.ps1`. The agents
(`inspector`, `organizer`, `mover`, `converter`) and formations (`organize-pipeline`,
`safe-migration`) in `.navig/store/` drive these verbs. Packaged navig skills for each
capability are planned — see [`.navig/skills/README.md`](.navig/skills/README.md).

## Quick start

```powershell
# inventory a folder (read-only)
.\bin\system.ps1 inventory "<drive>:\Downloads"

# fast size of a huge tree (no copy)
.\bin\system.ps1 size "<drive>:\Backups"

# safe migrate: copy -> verify -> trash original (dry-run first, then -Apply)
.\bin\system.ps1 migrate "<drive>:\Projects\my-app" -To "<other-drive>:\projects\my-app"

# long-path safe purge
.\bin\system.ps1 purge "<drive>:\.trash\old-backup"
```

## Safety, always

- **Never hard-deletes** — everything goes to a recoverable `.trash` + `restore-log.tsv`.
- **Dry-run by default** for move/migrate/trash/purge/reclaim — add `-Apply` to execute.
- **Verifies by file count / bytes**, never by "the folder exists".
- See [`docs/runbooks/safe-move-and-delete.md`](docs/runbooks/safe-move-and-delete.md).

## Layout

```
system-space/
├─ bin/        system.ps1 (dispatcher) + System-Common.ps1 (helpers)
├─ tools/      standalone organizers (file classifiers, manifest builders)
├─ docs/       reference (windows-filesystem.md) + runbooks + prompts
├─ tests/      smoke tests
└─ .navig/     config.yaml · context.md · skills · store (agents, formations)
```

— Read [`.navig/context.md`](.navig/context.md) for the operating doctrine.
