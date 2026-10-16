# System space — Preview

```
$ navig space use system-space

  SYSTEM  ·  OS & filesystem operator
  ────────────────────────────────────────────────
  agents      inspector · organizer · mover · converter
  formations  organize-pipeline · safe-migration
  engine      bin/system.ps1 — inventory · size · broken · dupes
              move · migrate · trash · purge · reclaim
  doctrine    never hard-delete · verify by count · same-vol rename
              long-path \\?\ · purpose+size classify

  PS> .\bin\system.ps1 inventory "<drive>:\Downloads"
    1,204 files · 18 dirs · 42.6 GB · 3 zero-byte
  PS> .\bin\system.ps1 size      "<drive>:\Backups"
    10,706,065 files · 311 GB   (robocopy /L — 4s)
  PS> .\bin\system.ps1 migrate   "<drive>:\Projects\my-app" -To "<other-drive>:\projects\my-app"
    [DRY-RUN] copy, verify by count, then trash original  (add -Apply to execute)
  PS> .\bin\system.ps1 purge     "<drive>:\.trash\old-backup" -Apply
    purged (long-path safe)
```

Illustrative output — your numbers will differ.
