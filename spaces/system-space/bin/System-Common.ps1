<#
  System-Common.ps1 — shared helpers for the System space engine.
  Encodes the safety rules: never hard-delete, verify by count/bytes, same-volume rename,
  long-path-safe delete, literal paths. Dot-source from bin/system.ps1.
#>
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Get-DriveRoot([string]$Path) { return ([IO.Path]::GetPathRoot((Resolve-Path -LiteralPath $Path).Path)) }

function Get-TrashRoot([string]$Path) {
  # per-drive recoverable trash at the drive root
  $root = Get-DriveRoot $Path
  $trash = Join-Path $root '.trash'
  if (-not (Test-Path -LiteralPath $trash)) { New-Item -ItemType Directory -Force $trash | Out-Null }
  return $trash
}

function Write-RestoreLog {
  param([string]$Trash,[string]$Item,[string]$Original,[string]$TrashPath,[string]$MigratedTo='-',[string]$Reason='',[string]$Verified='no')
  $log = Join-Path $Trash 'restore-log.tsv'
  if (-not (Test-Path -LiteralPath $log)) { "when`titem`toriginal_path`ttrash_path`tmigrated_to`treason`tverified" | Out-File $log -Encoding utf8 }
  ("{0}`t{1}`t{2}`t{3}`t{4}`t{5}`t{6}" -f (Get-Date -Format 'yyyy-MM-dd'),$Item,$Original,$TrashPath,$MigratedTo,$Reason,$Verified) |
    Out-File $log -Append -Encoding utf8
}

function Test-SameVolume([string]$A,[string]$B) { return ((Get-DriveRoot $A) -ieq (Get-DriveRoot (Split-Path $B -Parent))) }

function Move-Fast {
  # Same-volume = instant rename (no traversal, long-path immune). Cross-volume = robocopy.
  param([Parameter(Mandatory)][string]$Source,[Parameter(Mandatory)][string]$Dest)
  $parent = Split-Path $Dest -Parent
  if ($parent -and -not (Test-Path -LiteralPath $parent)) { New-Item -ItemType Directory -Force $parent | Out-Null }
  if (Test-Path -LiteralPath $Dest) { throw "dest exists: $Dest" }
  if (Test-SameVolume $Source $Dest) {
    [IO.Directory]::Move($Source, $Dest)      # O(1) rename
  } else {
    & robocopy $Source $Dest /E /R:0 /W:0 /MT:16 /NFL /NDL /NP /NJH /NJS | Out-Null
    Remove-LongPath $Source                   # original removed only after copy
  }
}

function Move-ToTrash {
  # Never hard-delete: rename into <drive>:\.trash and log it.
  param([Parameter(Mandatory)][string]$Path,[string]$MigratedTo='-',[string]$Reason='trashed',[string]$Verified='no')
  $trash = Get-TrashRoot $Path
  $name  = Split-Path $Path -Leaf
  $dest  = Join-Path $trash $name
  $i = 1; while (Test-Path -LiteralPath $dest) { $dest = Join-Path $trash ("{0}-{1}" -f $name,$i); $i++ }
  if (Test-SameVolume $Path $dest) { [IO.Directory]::Move($Path,$dest) }
  else { & robocopy $Path $dest /E /R:0 /W:0 /MT:16 /NFL /NDL /NP /NJH /NJS | Out-Null; Remove-LongPath $Path }
  Write-RestoreLog -Trash $trash -Item $name -Original $Path -TrashPath $dest -MigratedTo $MigratedTo -Reason $Reason -Verified $Verified
  return $dest
}

function Remove-LongPath {
  # Long-path-safe recursive delete (>260 chars). Falls back to robocopy /MIR (+ /B for ACL).
  param([Parameter(Mandatory)][string]$Path)
  if (-not (Test-Path -LiteralPath $Path)) { return }
  try   { [IO.Directory]::Delete("\\?\$Path", $true) }
  catch {
    $empty = Join-Path ([IO.Path]::GetTempPath()) ("__e_{0}" -f ([guid]::NewGuid().ToString('N')))
    New-Item -ItemType Directory -Force $empty | Out-Null
    & robocopy $empty $Path /MIR /B /R:0 /W:0 /MT:16 /NFL /NDL /NP /NJH /NJS | Out-Null
    [IO.Directory]::Delete($empty, $true)
    if (Test-Path -LiteralPath $Path) { [IO.Directory]::Delete($Path, $true) }
  }
}

function Get-FastSize {
  # Fast size of a huge tree without copying: robocopy /L summary.
  param([Parameter(Mandatory)][string]$Path)
  $null = & robocopy $Path "$env:TEMP\__sz_nul" /L /E /BYTES /NFL /NDL /NP /NJH 2>$null
  $out  = & robocopy $Path "$env:TEMP\__sz_nul" /L /E /BYTES /NFL /NDL /NP /NJH
  $files = ($out | Select-String '^\s*Files\s*:\s*(\d+)').Matches.Groups[1].Value
  $bytes = ($out | Select-String '^\s*Bytes\s*:\s*([\d\.]+)\s*(\w)?').Matches
  [pscustomobject]@{ Path=$Path; Files=$files; Raw=($out | Select-String '^\s*(Dirs|Files|Bytes)\s*:').Line }
}

function Get-Inventory {
  param([Parameter(Mandatory)][string]$Path)
  $files = @(Get-ChildItem -LiteralPath $Path -Recurse -File -ErrorAction SilentlyContinue)
  $zero  = @($files | Where-Object Length -eq 0).Count
  $bytes = ($files | Measure-Object Length -Sum).Sum
  [pscustomobject]@{
    Path  = $Path
    Files = $files.Count
    Dirs  = @(Get-ChildItem -LiteralPath $Path -Recurse -Directory -ErrorAction SilentlyContinue).Count
    GB    = [math]::Round(([double]$bytes)/1GB,2)
    ZeroByte = $zero
  }
}

function Stop-FsLocks {
  # Break common handle holders before a move/rename ("Access denied").
  foreach ($n in 'find','robocopy','rm') { Get-Process $n -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue }
}
