# NAVIG Skill Smoke Test — adb-connect
# Usage:    .\tests\test-adb-connect.ps1
# Purpose:  Validates that adb is reachable and that the adb-connect skill steps
#           execute without errors and return expected output patterns.
# Platform: Windows (PowerShell 7+ / pwsh — required for script-scoped functions)

$ErrorActionPreference = "Stop"
$PASS = 0; $FAIL = 0

function Assert-Match {
    param([string]$Label, [string]$Output, [string]$Pattern)
    if ($Output -match $Pattern) {
        Write-Host "  [PASS] $Label" -ForegroundColor Green
        $script:PASS++
    } else {
        Write-Host "  [FAIL] $Label — expected pattern: $Pattern" -ForegroundColor Red
        $script:FAIL++
    }
}

function Assert-NoError {
    param([string]$Label, [scriptblock]$Block)
    try {
        $out = & $Block 2>&1 | Out-String
        Write-Host "  [PASS] $Label (no exception)" -ForegroundColor Green
        $script:PASS++
        return $out
    } catch {
        Write-Host "  [FAIL] $Label — $_" -ForegroundColor Red
        $script:FAIL++
        return ""
    }
}

Write-Host "`n=== adb-connect skill smoke test ===" -ForegroundColor Cyan
Write-Host "Host: $env:COMPUTERNAME  |  Date: $(Get-Date -Format 'yyyy-MM-dd HH:mm')`n"

# ── Test 1: adb binary is resolvable ─────────────────────────────────────────
Write-Host "[ 1 ] adb availability"
$adb = Get-Command adb -ErrorAction SilentlyContinue
if (-not $adb) {
    $sdk = if ($env:ANDROID_HOME) { $env:ANDROID_HOME } else { $env:ANDROID_SDK_ROOT }
    $fallback = if ($sdk) { Join-Path $sdk 'platform-tools/adb.exe' } else { '' }
    if ($fallback -and (Test-Path -LiteralPath $fallback)) { $adb = $fallback } else { $adb = $null }
}
if ($adb) {
    Write-Host "  [PASS] adb found: $($adb.Source ?? $adb)" -ForegroundColor Green
    $PASS++
} else {
    Write-Host "  [FAIL] adb not found — install Android SDK Platform-Tools from developer.android.com" -ForegroundColor Red
    $FAIL++
    Write-Host "`nCannot continue without adb. Aborting.`n" -ForegroundColor Yellow
    Write-Host "=== RESULT: $PASS passed, $FAIL failed ===" -ForegroundColor Cyan
    exit 1
}

$adbBin = if ($adb -is [string]) { $adb } else { $adb.Source }

# ── Test 2: adb version reports cleanly ──────────────────────────────────────
Write-Host "`n[ 2 ] adb version"
$verOut = Assert-NoError "adb version" { & $adbBin version | Out-String }
Assert-Match "Version string present" $verOut 'Android Debug Bridge|version'

# ── Test 3: adb server starts ────────────────────────────────────────────────
Write-Host "`n[ 3 ] adb start-server"
$startOut = Assert-NoError "adb start-server" { & $adbBin start-server 2>&1 | Out-String }

# ── Test 4: adb devices lists (may be empty — that's OK) ──────────────────────
Write-Host "`n[ 4 ] adb devices -l"
$devOut = Assert-NoError "adb devices -l" { & $adbBin devices -l | Out-String }
Assert-Match "Header present" $devOut 'List of devices attached'
if ($devOut -match "device\s") {
    Write-Host "  [INFO] At least one device is connected." -ForegroundColor Cyan
} else {
    Write-Host "  [INFO] No device connected — connect one and re-run for a full test." -ForegroundColor Yellow
}

# ── Summary ──────────────────────────────────────────────────────────────────
Write-Host "`n=== RESULT: $PASS passed, $FAIL failed ===" -ForegroundColor Cyan
if ($FAIL -gt 0) { exit 1 } else { exit 0 }
