# PURPOSE:       Snapshot the live MQTT topic tree and print a sorted, unique topic list
# USAGE:         .\scripts\dump-mqtt-topics.ps1 [-Host 192.168.1.10] [-Port 1883] [-Seconds 20]
# PREREQUISITES: Eclipse Mosquitto clients (mosquitto_sub.exe on PATH)
# REQUIRES:      none

param(
    [string]$MqttHost = "192.168.1.10",
    [int]$Port = 1883,
    [int]$Seconds = 20
)

$sub = Get-Command mosquitto_sub -ErrorAction SilentlyContinue
if (-not $sub) {
    Write-Error "mosquitto_sub not found — install with 'winget install EclipseFoundation.Mosquitto'"
    exit 2
}

Write-Host "=== MQTT Topic Dump ===" -ForegroundColor Cyan
Write-Host "Broker: ${MqttHost}:${Port}  |  Listening ${Seconds}s`n"

# -v prints "<topic> <payload>"; keep the topic column, sort unique
$lines = & mosquitto_sub -h $MqttHost -p $Port -t '#' -v -W $Seconds 2>$null
$topics = $lines | ForEach-Object { ($_ -split '\s+', 2)[0] } | Sort-Object -Unique

$topics | ForEach-Object { Write-Host "  $_" }
$out = Join-Path $env:TEMP "iot-topics.txt"
$topics | Set-Content -Path $out

Write-Host "`nUnique topics: $($topics.Count)" -ForegroundColor Green
Write-Host "Saved to $out"
