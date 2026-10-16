# NAVIG Skill Smoke Test — device-discover
# Usage:    .\tests\test-device-discover.ps1
# Usage:    pwsh tests/test-device-discover.ps1
# Purpose:  Validates that the device-discover skill's building blocks (SSDP multicast,
#           mDNS lookup, ARP table) execute without errors and return usable output.
# Platform: Windows (PowerShell 7+ / pwsh)

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

Write-Host "`n=== device-discover skill smoke test ===" -ForegroundColor Cyan
Write-Host "Host: $env:COMPUTERNAME  |  Date: $(Get-Date -Format 'yyyy-MM-dd HH:mm')`n"

# ── Test 1: ARP neighbour table is readable ───────────────────────────────────
Write-Host "[ 1 ] ARP neighbour discovery"
$arpOut = Assert-NoError "arp -a" { arp -a | Out-String }
Assert-Match "ARP table has entries" $arpOut '\d+\.\d+\.\d+\.\d+'

# ── Test 2: SSDP M-SEARCH socket can be constructed & sent ─────────────────────
Write-Host "`n[ 2 ] SSDP M-SEARCH multicast"
$ssdpOut = Assert-NoError "SSDP send" {
    $udp = New-Object System.Net.Sockets.UdpClient
    $udp.Client.ReceiveTimeout = 1000
    $msg = "M-SEARCH * HTTP/1.1`r`nHOST:239.255.255.250:1900`r`nMAN:`"ssdp:discover`"`r`nMX:1`r`nST:ssdp:all`r`n`r`n"
    $bytes = [System.Text.Encoding]::ASCII.GetBytes($msg)
    $ep = New-Object System.Net.IPEndPoint([System.Net.IPAddress]::Parse("239.255.255.250"), 1900)
    $sent = $udp.Send($bytes, $bytes.Length, $ep)
    $udp.Close()
    "sent=$sent bytes"
}
Assert-Match "SSDP packet sent" $ssdpOut 'sent=\d+'

# ── Test 3: mDNS lookup runs (may return nothing on a quiet LAN, must not throw) ─
Write-Host "`n[ 3 ] mDNS PTR lookup"
$null = Assert-NoError "Resolve-DnsName _http._tcp.local" {
    Resolve-DnsName -Name "_http._tcp.local" -Type PTR -ErrorAction SilentlyContinue | Out-String
}

# ── Test 4: registry path is well-formed for merge output ─────────────────────
Write-Host "`n[ 4 ] Registry output path"
$regPath = ".navig/memory/device-registry.json"
$exPath  = ".navig/memory/device-registry.example.json"
$pathOut = Assert-NoError "example registry exists" {
    if (Test-Path $exPath) { "example_present=true" } else { "example_present=false" }
}
Assert-Match "example registry present" $pathOut 'example_present=true'

# ── Summary ───────────────────────────────────────────────────────────────────
Write-Host "`n=== RESULTS ===" -ForegroundColor Cyan
Write-Host "Passed : $PASS" -ForegroundColor Green
if ($FAIL -gt 0) {
    Write-Host "Failed : $FAIL" -ForegroundColor Red
    exit 1
} else {
    Write-Host "Failed : 0" -ForegroundColor Green
    Write-Host "`nAll device-discover smoke tests passed." -ForegroundColor Green
    exit 0
}
