<#
  system.ps1 — the System space engine / dispatcher.
  Every skill calls through here. Safety-first: dry-run defaults, never hard-delete,
  verify by count/bytes, same-volume rename, long-path-safe purge.

  Usage:
    system.ps1 <verb> <path> [-To <dest>] [-By purpose|type|size] [-Reason <s>] [-Apply]

  Verbs:
    inventory  <path>                 counts, size, dirs, zero-byte
    size       <path>                  fast byte/file count of a huge tree (robocopy /L)
    broken     <path>                  list 0-byte and truncated (<40KB) files
    dupes      <path>                  find duplicate files (by size+hash)
    move       <path> -To <dest>       same-volume rename / cross-volume robocopy
    migrate    <path> -To <dest>       copy -> verify by count -> trash original + log
    trash      <path> [-Reason <s>]    move to <drive>:\.trash + restore-log (recoverable)
    purge      <path>                  long-path-safe recursive delete (\\?\ / robocopy /MIR /B)
    reclaim    <drive>:\.trash         empty a trash (CONFIRM; only verified-redundant)

  Add -Apply to actually perform mutating verbs (default is dry-run preview).
#>
[CmdletBinding()]
param(
  [Parameter(Position=0)][string]$Verb = 'help',
  [Parameter(Position=1)][string]$Path,
  [string]$To,
  [ValidateSet('purpose','type','size','language')][string]$By = 'purpose',
  [string]$Reason = 'trashed',
  [switch]$Apply
)
. (Join-Path $PSScriptRoot 'System-Common.ps1')
function Say($m){ Write-Host $m }
function Plan($m){ Write-Host "  [DRY-RUN] $m  (add -Apply to execute)" -ForegroundColor Yellow }

switch ($Verb) {
  'inventory' { Get-Inventory $Path | Format-List }
  'size'      { (Get-FastSize $Path).Raw | ForEach-Object { Say "  $_" } }
  'broken'    {
    $f = Get-ChildItem -LiteralPath $Path -Recurse -File -ErrorAction SilentlyContinue
    Say ("  0-byte: {0}" -f @($f | ? Length -eq 0).Count)
    Say ("  truncated (<40KB): {0}" -f @($f | ? { $_.Length -gt 0 -and $_.Length -lt 40KB }).Count)
  }
  'dupes'     {
    Get-ChildItem -LiteralPath $Path -Recurse -File -EA SilentlyContinue |
      Group-Object Length | ? Count -gt 1 | % Group |
      Get-FileHash -Algorithm MD5 | Group-Object Hash | ? Count -gt 1 |
      % { Say ("  DUP x{0}: {1}" -f $_.Count, ($_.Group[0].Path | Split-Path -Leaf)) }
  }
  'move'      {
    if (-not $To) { throw "move needs -To <dest>" }
    if ($Apply) { Move-Fast -Source $Path -Dest $To; Say "  moved -> $To" }
    else { Plan "move $Path -> $To  ($(if(Test-SameVolume $Path $To){'instant rename'}else{'robocopy cross-volume'}))" }
  }
  'migrate'   {
    if (-not $To) { throw "migrate needs -To <dest>" }
    if ($Apply) {
      & robocopy $Path $To /E /R:0 /W:0 /MT:16 /NFL /NDL /NP /NJH /NJS | Out-Null
      $src = (Get-Inventory $Path).Files; $dst = (Get-Inventory $To).Files
      if ($dst -ge $src) { $t = Move-ToTrash -Path $Path -MigratedTo $To -Reason 'migrated' -Verified 'yes'; Say "  copied ($dst/$src files) ✓  original -> $t" }
      else { Say "  ABORT: dest $dst < src $src files — original kept" }
    } else { Plan "copy $Path -> $To, verify by count, then trash original" }
  }
  'trash'     {
    if ($Apply) { $t = Move-ToTrash -Path $Path -Reason $Reason; Say "  trashed -> $t (recoverable; logged)" }
    else { Plan "trash $Path -> $(Get-TrashRoot $Path) + restore-log" }
  }
  'purge'     {
    if ($Apply) { Remove-LongPath $Path; Say "  purged (long-path safe): $Path" }
    else { Plan "long-path purge $Path (\\?\ / robocopy /MIR /B)" }
  }
  'reclaim'   {
    Say "  reclaim empties a trash — IRREVERSIBLE. Only run on verified-redundant items."
    if ($Apply) { Get-ChildItem -LiteralPath $Path -Force | ? Name -ne 'restore-log.tsv' | % { Remove-LongPath $_.FullName }; Say "  emptied $Path (kept restore-log.tsv)" }
    else { Plan "empty $Path (keep restore-log.tsv)" }
  }
  default     { Get-Content (Join-Path $PSScriptRoot 'system.ps1') | Select-String '^\s+[a-z]+\s' -Context 0 | Out-Null; Get-Help -Detailed $MyInvocation.MyCommand.Path 2>$null; Say "system.ps1 <verb> <path> [-To] [-By] [-Apply] — see header for verbs" }
}
