<#
    DevTools-Common.ps1 - shared engine for all devtools-space skills.

    Dot-source from any skill script / the engine:
        . "$PSScriptRoot\DevTools-Common.ps1"

    Conventions (mirrors media-space):
      - ALWAYS -LiteralPath (file names contain [ ] ( ) which are PS wildcards).
      - Clean console output, NO square-bracket tags.
      - Tool guards give actionable "not installed / how to get it" messages.

    Compatible with Windows PowerShell 5.1 and PowerShell 7+. ASCII-only source.
#>

# UTF-8 so the few glyphs below render in any console.
try { [Console]::OutputEncoding = [System.Text.Encoding]::UTF8 } catch {}

# -- Console helpers (premium, no brackets) --------------------------------------
# Glyphs built from code points so the source stays ASCII (renders the same under
# Windows PowerShell 5.1 and pwsh 7+ once OutputEncoding is UTF-8, set above).
$script:G = @{
    ok   = [char]0x2713   # check
    err  = [char]0x2717   # cross
    warn = [char]0x25B2   # triangle
    step = [char]0x25B8   # play
    dot  = [char]0x00B7   # middot
    bar  = [char]0x2501   # heavy rule
    arr  = [char]0x2192   # arrow
}
function Get-Arrow { return $script:G.arr }

function Write-Step($m) { Write-Host ('   ' + $script:G.step + ' ' + $m) -ForegroundColor Cyan }
function Write-Ok($m)   { Write-Host ('   ' + $script:G.ok   + ' ' + $m) -ForegroundColor Green }
function Write-Warn($m) { Write-Host ('   ' + $script:G.warn + ' ' + $m) -ForegroundColor Yellow }
function Write-Err($m)  { Write-Host ('   ' + $script:G.err  + ' ' + $m) -ForegroundColor Red }
function Write-Info($m) { Write-Host ('     ' + $m) -ForegroundColor DarkGray }
function Write-Count($i, $n, $m) { Write-Host ('   ' + $script:G.step + ' ' + ('{0}/{1}' -f $i, $n) + '  ' + $m) -ForegroundColor Cyan }

function Write-Banner($title) {
    try { $Host.UI.RawUI.WindowTitle = 'devtools-space' + $(if ($title) { ' - ' + $title } else { '' }) } catch {}
    $rule = '  ' + (([string]$script:G.bar) * 54)
    Write-Host ''
    Write-Host $rule -ForegroundColor DarkCyan
    Write-Host ('   navig ' + $script:G.dot + ' devtools') -ForegroundColor DarkGray -NoNewline
    if ($title) { Write-Host ('   ' + $title) -ForegroundColor White } else { Write-Host '' }
    Write-Host $rule -ForegroundColor DarkCyan
}

function Read-Close { Write-Host ''; Write-Host ('     press Enter to close ' + $script:G.dot) -ForegroundColor DarkGray; [void](Read-Host) }

# -- Tool discovery --------------------------------------------------------------
# Known install dirs for tools that often are not on PATH.
$global:DevToolKnownDirs = @{
    '7z'      = @("$env:ProgramFiles\7-Zip\7z.exe", "${env:ProgramFiles(x86)}\7-Zip\7z.exe")
    '7zfm'    = @("$env:ProgramFiles\7-Zip\7zFM.exe", "${env:ProgramFiles(x86)}\7-Zip\7zFM.exe")
    'git'     = @("$env:ProgramFiles\Git\cmd\git.exe", "$env:ProgramFiles\Git\bin\git.exe")
    'yt-dlp'  = @("$env:LOCALAPPDATA\Microsoft\WinGet\Links\yt-dlp.exe")
    'docker'  = @("$env:ProgramFiles\Docker\Docker\resources\bin\docker.exe")
}
# How to get a missing tool (shown in errors).
$global:DevToolHints = @{
    '7z'     = 'Install 7-Zip: winget install 7zip.7zip'
    '7zfm'   = 'Install 7-Zip: winget install 7zip.7zip'
    'git'    = 'Install Git: winget install Git.Git'
    'yt-dlp' = 'Install yt-dlp: winget install yt-dlp.yt-dlp'
    'docker' = 'Install Docker Desktop: winget install Docker.DockerDesktop'
    'node'   = 'Install Node.js: winget install OpenJS.NodeJS'
    'npm'    = 'Install Node.js (bundles npm): winget install OpenJS.NodeJS'
}

function Find-Tool {
    # Returns the full path to the executable, or $null. Searches PATH then known dirs.
    param([Parameter(Mandatory)][string]$Name)
    $cmd = Get-Command $Name -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($cmd) { return $cmd.Source }
    $key = $Name.ToLower() -replace '\.exe$', ''
    if ($DevToolKnownDirs.ContainsKey($key)) {
        foreach ($p in $DevToolKnownDirs[$key]) { if ($p -and (Test-Path -LiteralPath $p)) { return $p } }
    }
    return $null
}

function Assert-Tool {
    # Returns the tool path or throws an actionable error.
    param([Parameter(Mandatory)][string]$Name)
    $p = Find-Tool $Name
    if ($p) { return $p }
    $key = $Name.ToLower() -replace '\.exe$', ''
    $hint = if ($DevToolHints.ContainsKey($key)) { $DevToolHints[$key] } else { "Install '$Name' and ensure it is on PATH." }
    throw "Required tool not found: $Name. $hint"
}

function Test-Tool([string]$Name) { [bool](Find-Tool $Name) }
function Find-7Zip   { Find-Tool '7z' }
function Find-7ZipFM { Find-Tool '7zfm' }

# -- Target / selection ----------------------------------------------------------
function Get-Target {
    # Normalize a context-menu target (%1 or %V). Falls back to current dir.
    param([string]$Path)
    if ($Path) { $Path = $Path.Trim('"').Trim() }
    if (-not $Path -or -not (Test-Path -LiteralPath $Path)) { return (Get-Location).Path }
    return (Resolve-Path -LiteralPath $Path).Path
}

# -- Config ----------------------------------------------------------------------
function Load-Config {
    # Reads config.json from the deploy dir (next to the engine), then the space root.
    param([string]$BinDir = $PSScriptRoot)
    $candidates = @(
        (Join-Path $BinDir 'config.json'),
        (Join-Path (Split-Path $BinDir -Parent) 'config.json'),
        (Join-Path $env:LOCALAPPDATA 'Navig\devtools\config.json')
    )
    foreach ($c in $candidates) {
        if (Test-Path -LiteralPath $c) {
            try { return (Get-Content -LiteralPath $c -Raw | ConvertFrom-Json) } catch {}
        }
    }
    return $null
}

# -- Temp dir with guaranteed cleanup --------------------------------------------
function New-TempDir {
    param([string]$Prefix = 'devtools')
    $p = Join-Path $env:TEMP ($Prefix + '_' + [guid]::NewGuid().ToString('N'))
    New-Item -ItemType Directory -Force -Path $p | Out-Null
    return $p
}

# -- Multi-select coalescing -----------------------------------------------------
# A classic shell verb uses "%1", so Explorer fires the engine ONCE PER selected
# file. These helpers coalesce those windowless invocations into ONE batch handled
# by a single visible worker window.  (Verified design ported from compress.ps1.)
$global:DevToolsTmp = Join-Path $env:TEMP 'Navig\devtools'

function Write-AuditLog($m) {
    try {
        if (-not (Test-Path -LiteralPath $DevToolsTmp)) { New-Item -ItemType Directory -Force -Path $DevToolsTmp | Out-Null }
        Add-Content -LiteralPath (Join-Path $DevToolsTmp 'devtools.log') -Value ((Get-Date -Format 'yyyy-MM-dd HH:mm:ss') + "  pid=$PID  " + $m)
    } catch {}
}

function Start-Coalesced {
    # Collector: append target to a per-command queue, elect a leader; the leader
    # debounces, drains the whole queue, and launches ONE visible worker that runs
    #   <engine> <command> --batch <listfile>
    param(
        [Parameter(Mandatory)][string]$EnginePath,
        [Parameter(Mandatory)][string]$Command,
        [Parameter(Mandatory)][string]$Target
    )
    if (-not (Test-Path -LiteralPath $DevToolsTmp)) { New-Item -ItemType Directory -Force -Path $DevToolsTmp | Out-Null }
    $safe  = ($Command -replace '[^A-Za-z0-9_]', '_')
    $queue = Join-Path $DevToolsTmp ("queue_" + $safe + ".txt")
    $qName = "Local\DT_Q_"    + $safe
    $lName = "Local\DT_LEAD_" + $safe

    $qm = New-Object System.Threading.Mutex($false, $qName)
    function _lock($m) { try { [void]$m.WaitOne() } catch [System.Threading.AbandonedMutexException] {} }

    _lock $qm
    try { Add-Content -LiteralPath $queue -Value $Target -Encoding UTF8 } finally { $qm.ReleaseMutex() }

    $createdNew = $false
    $lm = New-Object System.Threading.Mutex($true, $lName, [ref]$createdNew)
    if (-not $createdNew) {
        try { if ($lm.WaitOne(0)) { $createdNew = $true } } catch [System.Threading.AbandonedMutexException] { $createdNew = $true }
    }
    if (-not $createdNew) { return }   # another instance leads; it drains our line

    $all = New-Object System.Collections.Generic.List[string]
    do {
        Start-Sleep -Milliseconds 500
        _lock $qm
        try {
            if (Test-Path -LiteralPath $queue) {
                $lines = @(Get-Content -LiteralPath $queue -Encoding UTF8)
                Remove-Item -LiteralPath $queue -Force
            } else { $lines = @() }
        } finally { $qm.ReleaseMutex() }
        foreach ($l in $lines) { $t = $l.Trim([char]0xFEFF).Trim(); if ($t) { $all.Add($t) } }
    } while (@($lines).Count -gt 0)
    $lm.ReleaseMutex(); $lm.Dispose(); $qm.Dispose()

    $seen = @{}; $files = New-Object System.Collections.Generic.List[string]
    foreach ($f in $all) { $k = $f.ToLower(); if (-not $seen.ContainsKey($k)) { $seen[$k] = $true; $files.Add($f) } }
    if ($files.Count -eq 0) { return }

    $listFile = Join-Path $DevToolsTmp ("batch_" + $safe + "_" + ([guid]::NewGuid().ToString('N')) + ".txt")
    Set-Content -LiteralPath $listFile -Value $files -Encoding UTF8
    Write-AuditLog ("LEADER  command=$Command  batched=" + $files.Count)

    $host_exe = (Get-Process -Id $PID).Path           # relaunch the same interpreter (pwsh or powershell)
    $argLine  = '-NoProfile -ExecutionPolicy Bypass -File "' + $EnginePath + '" ' + $Command + ' --batch "' + $listFile + '"'
    Start-Process -FilePath $host_exe -ArgumentList $argLine -WindowStyle Normal
}

function Read-BatchList {
    # Worker side: read the list file written by Start-Coalesced and delete it.
    param([Parameter(Mandatory)][string]$ListFile)
    $items = @()
    if (Test-Path -LiteralPath $ListFile) {
        $items = @(Get-Content -LiteralPath $ListFile -Encoding UTF8 |
                   ForEach-Object { $_.Trim([char]0xFEFF).Trim() } |
                   Where-Object { $_ -ne '' })
        Remove-Item -LiteralPath $ListFile -Force -ErrorAction SilentlyContinue
    }
    return $items
}
