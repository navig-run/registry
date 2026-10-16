# PURPOSE:       Catalog-driven batch debloat — reversibly disable a list of packages for user 0.
# USAGE:         .\batch-debloat.ps1 -PackageFile packages.txt          # dry-run (default)
#                .\batch-debloat.ps1 -Packages "com.a,com.b" -Execute   # actually disable
#                .\batch-debloat.ps1 -PackageFile packages.txt -Restore -Execute  # undo
# PREREQUISITES: adb on PATH (or under $ANDROID_HOME\platform-tools); a device connected + authorized.
# REQUIRES:      none  (per-user disable — no root, nothing touches /system)

[CmdletBinding()]
param(
    [string]$PackageFile = "",
    [string]$Packages = "",
    [string]$Serial = "",
    [switch]$Restore,
    [switch]$Execute
)

$ErrorActionPreference = "Stop"

# Resolve adb
$adb = (Get-Command adb -ErrorAction SilentlyContinue)?.Source
if (-not $adb) {
    $sdk = if ($env:ANDROID_HOME) { $env:ANDROID_HOME } else { $env:ANDROID_SDK_ROOT }
    $fallback = if ($sdk) { Join-Path $sdk 'platform-tools/adb.exe' } else { '' }
    if ($fallback -and (Test-Path -LiteralPath $fallback)) { $adb = $fallback }
    else { Write-Error "adb not found. Install Android SDK Platform-Tools from developer.android.com"; exit 1 }
}
$sel = if ($Serial) { @("-s", $Serial) } else { @() }

# Build the package list
$list = @()
if ($PackageFile) {
    if (-not (Test-Path $PackageFile)) { Write-Error "Package file not found: $PackageFile"; exit 1 }
    $list += Get-Content $PackageFile | Where-Object { $_ -and $_ -notmatch '^\s*#' } | ForEach-Object { $_.Trim() }
}
if ($Packages) { $list += ($Packages -split ',') | ForEach-Object { $_.Trim() } | Where-Object { $_ } }
$list = $list | Select-Object -Unique
if (-not $list) { Write-Error "No packages given. Use -PackageFile or -Packages."; exit 1 }

$mode = if ($Restore) { "RESTORE" } else { "DISABLE" }
$run  = if ($Execute) { "EXECUTE" } else { "DRY-RUN" }
Write-Host "=== Batch Debloat ($mode / $run) ===" -ForegroundColor Cyan
Write-Host "Target: $(if ($Serial) { $Serial } else { 'default device' })  |  Packages: $($list.Count)`n"

# Confirm a device is present
& $adb $sel get-state 2>$null | Out-Null

$ok = 0; $fail = 0
foreach ($pkg in $list) {
    if ($Restore) {
        $cmd = @("shell", "cmd", "package", "install-existing", $pkg)
        $desc = "restore $pkg"
    } else {
        $cmd = @("shell", "pm", "disable-user", "--user", "0", $pkg)
        $desc = "disable $pkg"
    }

    if (-not $Execute) {
        Write-Host "  [DRY-RUN] adb $($sel -join ' ') $($cmd -join ' ')" -ForegroundColor Yellow
        continue
    }

    try {
        $out = & $adb $sel $cmd 2>&1 | Out-String
        if ($out -match "new state|installed|Success|Enabled") {
            Write-Host "  [OK]   $desc" -ForegroundColor Green; $ok++
        } else {
            Write-Host "  [WARN] $desc -> $($out.Trim())" -ForegroundColor Yellow; $ok++
        }
    } catch {
        Write-Host "  [FAIL] $desc -> $_" -ForegroundColor Red; $fail++
    }
}

if ($Execute) {
    Write-Host "`n=== Done: $ok ok, $fail failed ===" -ForegroundColor Cyan
    if (-not $Restore) {
        Write-Host "Restore anytime with: .\batch-debloat.ps1 -PackageFile <same> -Restore -Execute" -ForegroundColor Cyan
    }
} else {
    Write-Host "`nDry-run only. Re-run with -Execute to apply." -ForegroundColor Yellow
}
