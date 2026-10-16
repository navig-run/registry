# Windows / Filesystem — operator cheat-sheet

## Move & copy
```powershell
# Same volume → instant O(1) rename (no traversal; long-path immune)
[IO.Directory]::Move('<drive>:\X', '<drive>:\.trash\X')
[IO.File]::Move('<drive>:\a.txt', '<drive>:\b.txt')

# Cross volume → robocopy (Move-Item slow-copies junctions — avoid)
robocopy <src> <dst> /E /R:0 /W:0 /MT:16 /NFL /NDL /NP        # mirror tree, fast, no hang
robocopy <src> <dst> /E /MOVE                                  # copy then delete src (same-vol = slow copy!)
robocopy <src> <dst> /E /XD node_modules .git vendor dist      # exclude heavy/regenerable dirs
```

## Fast sizing (no copy) — beats du / Get-ChildItem -Recurse on huge trees
```powershell
robocopy <path> <throwaway> /L /E /BYTES /NFL /NDL /NP /NJH   # read the Files:/Bytes: summary
```

## Long paths (>260 chars)
```powershell
# delete (rm / Remove-Item / Explorer all fail)
[IO.Directory]::Delete('\\?\<drive>:\.trash\old-backup', $true)   # .NET long-path recursive delete
robocopy <empty-dir> <target> /MIR /R:0 /W:0 /MT:16          # mirror empty → purge (long-path native)
robocopy <empty-dir> <target> /MIR /B                         # + /B backup mode: bypass ACL-locked files
# NB: \\?\ gets mangled in bash — do these from PowerShell.
```

## Locks ("Access denied" on a move/rename)
```powershell
Get-Process find,robocopy,rm | Stop-Process -Force            # kill stray handle holders (esp. leftover find.exe)
# also: close Explorer windows on the drive; Defender/Search-indexer scans hold handles too
# retry the move with a few-second backoff
```

## Hostile filenames (spaces, () [] «» • emoji Cyrillic fullwidth)
```powershell
Get-ChildItem -LiteralPath $dir | Where-Object Name -match 'pattern'   # PowerShell: Unicode-correct -match
Move-Item -LiteralPath $src -Destination $dst                          # always -LiteralPath
```
```bash
find "$dir" -maxdepth 1 -printf '%f\n' | while IFS= read -r f; do … ; done   # never  for f in $(ls)
find "$dir" -print0 | xargs -0 …
# grep -i does NOT case-fold Cyrillic reliably → match exact case or use PowerShell -match
```

## Bash + robocopy (MSYS mangles switches and \\?\)
```bash
MSYS_NO_PATHCONV=1 MSYS2_ARG_CONV_EXCL='*' robocopy '<drive>:\src' '<drive>:\dst' /MIR /R:0 /W:0
```

## Junk & type by size
```bash
find <dir> -type f -size 0                 # 0-byte = dead/empty download
find <dir> -type f ! -size 0 -size -40k    # truncated stub (~1-2s) = broken partial
# size separates SFX/voice/samples (<300KB) from songs (3-8MB) where filenames can't
find <dir> -type f -printf '%s\t%f\n' | sort -n | head   # smallest first = clips/SFX/broken
```

## Drives / volumes
```powershell
Get-PSDrive -PSProvider FileSystem | Select Name,@{n='FreeGB';e={[math]::Round($_.Free/1GB,1)}}
[IO.Path]::GetPathRoot($path)               # which volume a path is on (same-vol test)
fsutil reparsepoint query <path>            # detect junctions/symlinks/reparse points
```

## ACLs / ownership (when even /B isn't enough)
```powershell
takeown /F <path> /R /D Y
icacls <path> /grant "$env:USERNAME:F" /T
```

## The exit codes that look like failures but aren't
- **robocopy** exit `1`=copied, `2`=extra, `4`=mismatch, `8`=fail, `16`=fatal (it's a bitmask;
  `3`=1+2 fine, `11`=1+2+8 means "done with some failures"). Only `>=8` has real failures.
