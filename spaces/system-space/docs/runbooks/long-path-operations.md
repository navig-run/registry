# Runbook — Long-path operations

Old web-hosting backups, `node_modules`, and Perl/vendor trees nest past **260 chars**
(seen: 351). `rm -rf`, `Remove-Item`, Explorer, and plain `find` choke or hang.

## Symptoms
- `ERROR 3 / ERROR 2: The system cannot find the path specified` deep in the tree.
- A delete that "runs forever" then leaves a few stubborn subdirs.
- `[IO.Directory]::Move` of the **top** folder still works (rename doesn't traverse) — so
  **trashing** is fine; it's **deleting** that needs care.

## Delete a long-path tree
```powershell
# Primary: .NET long-path recursive delete (PowerShell 7)
$target = '<drive>:\.trash\old-backup'
[IO.Directory]::Delete("\\?\$target", $true)

# If it stops on an ACL-locked file (e.g. a Linux dhclient.leases) → robocopy backup mode
$empty = New-Item -ItemType Directory -Force "$env:TEMP\__e"
robocopy $empty $target /MIR /B /R:0 /W:0 /MT:16 /NFL /NDL /NP
[IO.Directory]::Delete($target, $true)   # remove the now-empty shell
```
`system.ps1 purge <path> -Apply` wraps this (tries `\\?\` delete, falls back to `/MIR /B`).

## Copy a long-path tree
```powershell
robocopy <src> <dst> /E /MT:16 /R:1 /W:1        # robocopy handles long paths natively
# verify by file count; a few deep "2delete"/cache files may fail (/R:0 skips) — that's fine
```

## Gotchas
- `\\?\` **mangles in bash** (one backslash eaten). Do long-path work in **PowerShell**.
- Don't bother with `rm` first — go straight to `\\?\` delete or `/MIR`.
- Sizing first (`robocopy /L /BYTES`) tells you how big the job is without walking it slowly.
- Deleting frees space **depth-first**: top folders linger until emptied — watch free space,
  not folder presence, to confirm progress.
