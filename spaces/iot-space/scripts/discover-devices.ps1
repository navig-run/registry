# PURPOSE:       Discover IoT devices on the LAN via SSDP (UPnP) + mDNS + ARP
# USAGE:         .\scripts\discover-devices.ps1 [-Range 192.168.20.0/24]
# PREREQUISITES: PowerShell 7+; nmap optional (falls back to ARP); Bonjour optional for mDNS
# REQUIRES:      none

param(
    [string]$Range = "192.168.20.0/24"
)

$ErrorActionPreference = "SilentlyContinue"
Write-Host "=== IoT Device Discovery ===" -ForegroundColor Cyan
Write-Host "Range: $Range`n"

# ── SSDP / UPnP: M-SEARCH multicast ───────────────────────────────────────────
Write-Host "[ SSDP / UPnP ]" -ForegroundColor Yellow
$msg = @(
    "M-SEARCH * HTTP/1.1",
    "HOST:239.255.255.250:1900",
    'MAN:"ssdp:discover"',
    "MX:2",
    "ST:ssdp:all", "", ""
) -join "`r`n"

$udp = New-Object System.Net.Sockets.UdpClient
$udp.Client.ReceiveTimeout = 3000
$bytes = [System.Text.Encoding]::ASCII.GetBytes($msg)
$ep = New-Object System.Net.IPEndPoint([System.Net.IPAddress]::Parse("239.255.255.250"), 1900)
[void]$udp.Send($bytes, $bytes.Length, $ep)

$seen = @{}
try {
    while ($true) {
        $remote = New-Object System.Net.IPEndPoint([System.Net.IPAddress]::Any, 0)
        $data = $udp.Receive([ref]$remote)
        $ip = $remote.Address.ToString()
        if (-not $seen.ContainsKey($ip)) {
            $seen[$ip] = $true
            $text = [System.Text.Encoding]::ASCII.GetString($data)
            $server = ($text -split "`r`n" | Where-Object { $_ -match "^SERVER:" }) -replace "^SERVER:\s*", ""
            Write-Host ("  {0,-16} {1}" -f $ip, $server)
        }
    }
} catch {}
$udp.Close()
Write-Host "  SSDP devices: $($seen.Count)`n"

# ── mDNS (best effort via Resolve-DnsName for common IoT service types) ────────
Write-Host "[ mDNS ]" -ForegroundColor Yellow
$types = @("_http._tcp","_hap._tcp","_esphomelib._tcp","_mqtt._tcp")
foreach ($t in $types) {
    $r = Resolve-DnsName -Name "$t.local" -Type PTR -ErrorAction SilentlyContinue
    if ($r) { $r | ForEach-Object { Write-Host ("  {0,-24} {1}" -f $t, $_.NameHost) } }
}
Write-Host ""

# ── ARP fallback ──────────────────────────────────────────────────────────────
Write-Host "[ ARP neighbours ]" -ForegroundColor Yellow
arp -a | Where-Object { $_ -match "^\s+\d" } | ForEach-Object {
    $p = ($_ -split '\s+') | Where-Object { $_ }
    Write-Host ("  {0,-16} {1}" -f $p[0], $p[1])
}

Write-Host "`nDiscovery complete." -ForegroundColor Green
