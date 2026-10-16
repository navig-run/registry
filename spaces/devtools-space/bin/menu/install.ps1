<#
    install.ps1 - register the devtools context menu under HKCU (no admin).

    Reads ..\menu.manifest.json, deploys the engine to %LOCALAPPDATA%\Navig\devtools
    (so the menu survives the repo moving), and writes one HKCU verb per item.

      install.ps1            deploy + register
      install.ps1 -Dev       register against the repo bin\ (live edits, no copy)
      install.ps1 -DryRun    print what would be written, change nothing
      install.ps1 -List      show what is currently registered
#>
param([switch]$Dev, [switch]$DryRun, [switch]$List)

$SpaceBin  = Split-Path $PSScriptRoot -Parent
$SpaceRoot = Split-Path $SpaceBin -Parent
. (Join-Path $SpaceBin 'DevTools-Common.ps1')

$manifest = Get-Content -LiteralPath (Join-Path $SpaceBin 'menu.manifest.json') -Raw | ConvertFrom-Json
$HKCU = [Microsoft.Win32.Registry]::CurrentUser

if ($List) {
    Write-Banner 'devtools menu - currently registered (HKCU)'
    foreach ($g in $manifest.groups) {
        foreach ($class in $g.classes) {
            $p = "Software\Classes\$class\shell\$($g.key)"
            $k = $HKCU.OpenSubKey($p)
            if ($k) { Write-Ok ("{0,-22} {1}" -f ($class + '\' + $g.key), $k.GetValue('MUIVerb')); $k.Close() }
            else    { Write-Info ("{0,-22} (not installed)" -f ($class + '\' + $g.key)) }
        }
    }
    return
}

# --- interpreter (prefer pwsh 7+, fall back to Windows PowerShell) ---
$interp = (Get-Command pwsh -ErrorAction SilentlyContinue).Source
if (-not $interp) { $interp = (Get-Command powershell -ErrorAction SilentlyContinue).Source }
if (-not $interp) { throw 'No PowerShell interpreter found.' }

# --- deploy the engine (unless -Dev) ---
$deployDir = [Environment]::ExpandEnvironmentVariables($manifest.deployDir)
$engineDir = if ($Dev) { $SpaceBin } else { $deployDir }
$enginePath = Join-Path $engineDir $manifest.engine
$vbsPath    = Join-Path $engineDir $manifest.launcher

Write-Banner ('devtools menu install' + $(if ($Dev) { ' (dev / from repo)' } elseif ($DryRun) { ' (dry-run)' } else { '' }))
Write-Info "interpreter : $interp"
Write-Info "engine      : $enginePath"

if (-not $Dev -and -not $DryRun) {
    New-Item -ItemType Directory -Force -Path $deployDir | Out-Null
    foreach ($f in @($manifest.engine, 'DevTools-Common.ps1', $manifest.launcher, 'menu.manifest.json')) {
        Copy-Item -LiteralPath (Join-Path $SpaceBin $f) -Destination $deployDir -Force
    }
    $cfgEx = Join-Path $SpaceRoot 'config.example.json'
    if (Test-Path -LiteralPath $cfgEx) { Copy-Item -LiteralPath $cfgEx -Destination $deployDir -Force }
    $cfg = Join-Path $SpaceRoot 'config.json'
    if (Test-Path -LiteralPath $cfg) { Copy-Item -LiteralPath $cfg -Destination $deployDir -Force }
    Write-Ok "deployed to : $deployDir"
}

function New-Verb($subpath, [hashtable]$values) {
    $k = $HKCU.CreateSubKey($subpath)
    foreach ($n in $values.Keys) { $k.SetValue($n, [string]$values[$n], [Microsoft.Win32.RegistryValueKind]::String) }
    $k.Close()
}
function Build-Command($item, $argTok) {
    if ($item.exec) { return '"' + [Environment]::ExpandEnvironmentVariables($item.exec) + '" "' + $argTok + '"' }
    if ($item.launch -eq 'coalesce') {
        return 'wscript.exe "' + $vbsPath + '" "' + $interp + '" "' + $enginePath + '" "' + $item.command + '" "' + $argTok + '"'
    }
    return '"' + $interp + '" -NoProfile -ExecutionPolicy Bypass -File "' + $enginePath + '" ' + $item.command + ' --target "' + $argTok + '"'
}

$count = 0
foreach ($g in $manifest.groups) {
    $icon = [Environment]::ExpandEnvironmentVariables($g.icon)
    foreach ($class in $g.classes) {
        $argTok    = if ($class -match 'Background$') { '%V' } else { '%1' }
        $groupPath = "Software\Classes\$class\shell\$($g.key)"
        if (-not $DryRun) { try { $HKCU.DeleteSubKeyTree($groupPath, $false) } catch {} }   # idempotent

        # Flat verb: a group with its own command is a single action (no submenu).
        if ($g.command -or $g.exec) {
            $cmd = Build-Command $g $argTok
            if ($DryRun) { Write-Host ("      {0,-30} {1}" -f ($groupPath + "  '" + $g.label + "'"), $cmd) -ForegroundColor DarkGray }
            else {
                New-Verb $groupPath @{ 'MUIVerb' = $g.label; 'Icon' = $icon }
                New-Verb "$groupPath\command" @{ '' = $cmd }
            }
            $count++
            continue
        }

        if ($DryRun) {
            Write-Info "$groupPath   '$($g.label)'  ($class arg=$argTok)"
        } else {
            New-Verb $groupPath @{ 'MUIVerb' = $g.label; 'SubCommands' = ''; 'Icon' = $icon }
        }
        foreach ($it in $g.items) {
            $cmd = Build-Command $it $argTok
            $itemPath = "$groupPath\shell\$($it.key)"
            if ($DryRun) {
                Write-Host ("      {0,-22} {1}" -f $it.label, $cmd) -ForegroundColor DarkGray
            } else {
                $itemIcon = if ($it.icon) { [Environment]::ExpandEnvironmentVariables($it.icon) } else { $icon }
                New-Verb $itemPath @{ 'MUIVerb' = $it.label; 'Icon' = $itemIcon }
                New-Verb "$itemPath\command" @{ '' = $cmd }
            }
            $count++
        }
    }
}

if ($DryRun) { Write-Warn "Dry-run: nothing written ($count items)." }
else { Write-Ok "Registered $count menu item(s). Right-click a file or folder to use them." }
