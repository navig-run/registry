# PURPOSE:       Interactive Android 11+ wireless-debugging pairing helper (also supports legacy tcpip).
# USAGE:         .\pair-wireless.ps1                 # Android 11+ pairing flow
#                .\pair-wireless.ps1 -Tcpip -DeviceHost 192.168.1.42   # legacy tcpip (device on USB)
# PREREQUISITES: adb on PATH (or under $ANDROID_HOME\platform-tools)
# REQUIRES:      none

[CmdletBinding()]
param(
    [switch]$Tcpip,
    [string]$DeviceHost = "",
    [int]$ConnectPort = 5555
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

Write-Host "=== Android Wireless Debug Helper ===" -ForegroundColor Cyan
& $adb start-server | Out-Null

if ($Tcpip) {
    # ── Legacy tcpip path: device must be on USB ─────────────────────────────
    Write-Host "`n[tcpip mode] Ensure the device is connected via USB and authorized." -ForegroundColor Yellow
    & $adb devices -l
    Write-Host "`nSwitching device to tcpip:$ConnectPort ..." -ForegroundColor Cyan
    & $adb tcpip $ConnectPort

    if (-not $DeviceHost) {
        Write-Host "Detecting device IP (wlan0) ..." -ForegroundColor Cyan
        $route = & $adb shell ip route 2>$null | Select-String "wlan0"
        if ($route) { $DeviceHost = ($route.ToString() -replace '.*src\s+(\S+).*', '$1') }
    }
    if (-not $DeviceHost) { $DeviceHost = Read-Host "Enter the device IP" }

    Start-Sleep -Seconds 2
    Write-Host "Connecting to ${DeviceHost}:$ConnectPort ..." -ForegroundColor Cyan
    & $adb connect "${DeviceHost}:$ConnectPort"
}
else {
    # ── Android 11+ pairing path: no cable needed ────────────────────────────
    Write-Host "`n[pairing mode] On the device:" -ForegroundColor Yellow
    Write-Host "  Developer options -> Wireless debugging -> 'Pair device with pairing code'" -ForegroundColor Yellow
    Write-Host "  Note BOTH numbers shown: the pairing 'IP:port' and the (different) debug port.`n"

    $pairEndpoint = Read-Host "Enter pairing endpoint (IP:pairPort, e.g. 192.168.1.42:37105)"
    $pairCode     = Read-Host "Enter the 6-digit pairing code"

    Write-Host "`nPairing ..." -ForegroundColor Cyan
    & $adb pair $pairEndpoint $pairCode

    $connectEndpoint = Read-Host "`nEnter the connect endpoint (IP:debugPort shown under 'Wireless debugging')"
    Write-Host "Connecting ..." -ForegroundColor Cyan
    & $adb connect $connectEndpoint
}

Write-Host "`n=== Devices ===" -ForegroundColor Cyan
& $adb devices -l
