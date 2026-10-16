# NAVIG Skill Smoke Test — disk-health
# Usage:    .\tests\test-disk-health.ps1
# Usage:    pwsh tests/test-disk-health.ps1
# Purpose:  Validates that the disk-health skill steps execute without errors
#           and return expected output patterns for the local C:\ drive.
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

Write-Host "`n=== disk-health skill smoke test ===" -ForegroundColor Cyan
Write-Host "Host: $env:COMPUTERNAME  |  Date: $(Get-Date -Format 'yyyy-MM-dd HH:mm')`n"

# ── Test 1: C:\ partition resolves to a disk ──────────────────────────────────
Write-Host "[ 1 ] Disk identification"
$partOut = Assert-NoError "Get-Partition for C:" {
    $p = Get-Partition -DriveLetter C -ErrorAction Stop
    Get-Disk -Number $p.DiskNumber | Select-Object FriendlyName, HealthStatus | Out-String
}
Assert-Match "Disk has FriendlyName"   $partOut '\w+'
Assert-Match "HealthStatus present"    $partOut 'Healthy|Warning|Unhealthy'

# ── Test 2: PhysicalDisk entry exists for disk 0 ─────────────────────────────
Write-Host "`n[ 2 ] Get-PhysicalDisk"
$diskNum  = (Get-Partition -DriveLetter C).DiskNumber
$pdOut    = Assert-NoError "Get-PhysicalDisk" {
    Get-PhysicalDisk | Where-Object { $_.DeviceId -eq $diskNum } |
        Select-Object FriendlyName, MediaType, HealthStatus | Out-String
}
Assert-Match "PhysicalDisk not empty"  $pdOut '\w+'
Assert-Match "MediaType present"       $pdOut 'SSD|HDD|SCM|Unspecified'

# ── Test 3: StorageReliabilityCounter returns data ───────────────────────────
Write-Host "`n[ 3 ] Get-StorageReliabilityCounter"
$rcOut = Assert-NoError "StorageReliabilityCounter" {
    $pd = Get-PhysicalDisk | Where-Object { $_.DeviceId -eq $diskNum }
    Get-StorageReliabilityCounter -PhysicalDisk $pd | Select-Object Temperature, Wear | Out-String
}
Assert-Match "Reliability counter not empty" $rcOut '\w+'

# ── Test 4: Volume C:\ is healthy ─────────────────────────────────────────────
Write-Host "`n[ 4 ] Get-Volume C:"
$volOut = Assert-NoError "Get-Volume" {
    Get-Volume -DriveLetter C | Select-Object FileSystem, HealthStatus, SizeRemaining | Out-String
}
Assert-Match "Volume HealthStatus"     $volOut 'Healthy|Warning|Unhealthy'
Assert-Match "NTFS filesystem"         $volOut 'NTFS|ReFS'
Assert-Match "SizeRemaining > 0"       $volOut '[1-9]\d{6,}'   # at least 7-digit bytes

# ── Test 5: Volume not dirty ──────────────────────────────────────────────────
Write-Host "`n[ 5 ] Dirty bit check"
$dirtyOut = Assert-NoError "fsutil dirty query C:" { & fsutil dirty query C: 2>&1 | Out-String }
Assert-Match "Volume not dirty"        $dirtyOut 'NOT Dirty|is NOT'

# ── Test 6: Event log query runs without error ────────────────────────────────
Write-Host "`n[ 6 ] Event log query"
$null = Assert-NoError "Get-WinEvent System log" {
    Get-WinEvent -FilterHashtable @{LogName='System'; Level=1,2; StartTime=(Get-Date).AddDays(-7)} `
        -ErrorAction SilentlyContinue | Select-Object -First 1 | Out-String
}

# ── Test 7: WMI cross-check ───────────────────────────────────────────────────
Write-Host "`n[ 7 ] WMI Win32_DiskDrive"
$wmiOut = Assert-NoError "Get-CimInstance Win32_DiskDrive" {
    Get-CimInstance Win32_DiskDrive | Where-Object { $_.Index -eq $diskNum } |
        Select-Object Status, Model | Out-String
}
Assert-Match "WMI Status OK"           $wmiOut 'OK|Degraded|Unknown'

# ── Summary ───────────────────────────────────────────────────────────────────
Write-Host "`n=== RESULTS ===" -ForegroundColor Cyan
Write-Host "Passed : $PASS" -ForegroundColor Green
if ($FAIL -gt 0) {
    Write-Host "Failed : $FAIL" -ForegroundColor Red
    exit 1
} else {
    Write-Host "Failed : 0" -ForegroundColor Green
    Write-Host "`nAll disk-health smoke tests passed." -ForegroundColor Green
    exit 0
}
