# setup-links.ps1 — create root links into .navig/ (run once after cloning this space).
# Uses NTFS junctions (mklink /J) — NO Administrator / Developer Mode required.
# Mirrors what `navig space init` does automatically:
#   ./plans -> .navig\plans   |   ./.inbox -> .navig\inbox

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

function Link([string]$Name, [string]$Target) {
  if (Test-Path $Name) { Write-Host "  skip  $Name (exists)"; return }
  cmd /c mklink /J "$Name" "$Target" | Out-Null
  Write-Host "  ok    $Name -> $Target"
}

Write-Host "Creating root links (junctions — no admin needed)..."
Link "plans"  ".navig\plans"
Link ".inbox" ".navig\inbox"
Write-Host "Done."
