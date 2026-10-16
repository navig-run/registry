# setup-links.ps1 — create optional root-level symlinks for quick access
# Run from the space root: powershell setup-links.ps1

$spaceRoot = Split-Path -Parent $MyInvocation.MyCommand.Path

function Create-Link($target, $link) {
  $fullLink = Join-Path $spaceRoot $link
  $fullTarget = Join-Path $spaceRoot $target
  if (Test-Path $fullLink) {
    Write-Host "  skip  $link (already exists)"
  } else {
    New-Item -ItemType SymbolicLink -Path $fullLink -Target $fullTarget | Out-Null
    Write-Host "  link  $link -> $target"
  }
}

Write-Host "Social Circle -- setting up symlinks in space root..."
Create-Link ".navig/inbox"  "inbox"
Create-Link ".navig/plans"  "plans"
Create-Link ".navig/memory" "memory"
Write-Host "done."
