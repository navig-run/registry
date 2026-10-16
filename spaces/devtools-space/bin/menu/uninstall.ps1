<#
    uninstall.ps1 - remove the devtools context menu from HKCU (no admin).

      uninstall.ps1               remove all registered menu groups
      uninstall.ps1 -Purge        also delete the deployed engine folder
#>
param([switch]$Purge)

$SpaceBin = Split-Path $PSScriptRoot -Parent
. (Join-Path $SpaceBin 'DevTools-Common.ps1')

$manifest = Get-Content -LiteralPath (Join-Path $SpaceBin 'menu.manifest.json') -Raw | ConvertFrom-Json
$HKCU = [Microsoft.Win32.Registry]::CurrentUser

Write-Banner 'devtools menu uninstall'
$removed = 0
foreach ($g in $manifest.groups) {
    foreach ($class in $g.classes) {
        $p = "Software\Classes\$class\shell\$($g.key)"
        if ($HKCU.OpenSubKey($p)) {
            try { $HKCU.DeleteSubKeyTree($p, $false); $removed++; Write-Info "removed $p" } catch { Write-Warn "could not remove $p : $_" }
        }
    }
}
Write-Ok "Removed $removed menu group(s)."

if ($Purge) {
    $deployDir = [Environment]::ExpandEnvironmentVariables($manifest.deployDir)
    if (Test-Path -LiteralPath $deployDir) {
        Remove-Item -LiteralPath $deployDir -Recurse -Force -ErrorAction SilentlyContinue
        Write-Ok "Deleted deployed engine: $deployDir"
    }
}
