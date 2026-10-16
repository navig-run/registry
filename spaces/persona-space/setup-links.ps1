# setup-links.ps1 — Create optional root symlinks into .navig/
# Run once after cloning or creating a space from the empty-space skeleton.
# Requires: Windows Developer Mode enabled OR PowerShell running as Administrator.
#
# These are convenience shortcuts only. The space works without them.
# Symlinks: inbox → .navig\inbox | docs → .navig\inbox\docs | plans → .navig\plans

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

function Create-Link {
  param([string]$Name, [string]$Target)
  $full = Join-Path $PSScriptRoot $Name
  if (Test-Path $full) {
    Write-Host "  skip  $Name (already exists)"
  } else {
    New-Item -ItemType SymbolicLink -Path $full -Target (Join-Path $PSScriptRoot $Target) | Out-Null
    Write-Host "  ok    $Name -> $Target"
  }
}

Write-Host "Creating root symlinks..."
Create-Link "inbox" ".navig\inbox"
Create-Link "docs"  ".navig\inbox\docs"
Create-Link "plans" ".navig\plans"
Write-Host "Done."
