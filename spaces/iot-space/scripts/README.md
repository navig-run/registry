# Scripts

Automation helpers for IoT discovery and the MQTT message bus.

## Contents

| Script | Platform | Purpose | Requires Elevated |
|--------|----------|---------|-------------------|
| [discover-devices.ps1](discover-devices.ps1) | Windows | SSDP + mDNS + ARP discovery sweep | No |
| [discover-devices.sh](discover-devices.sh) | Linux/macOS | SSDP + mDNS (avahi) + ARP discovery sweep | No |
| [dump-mqtt-topics.ps1](dump-mqtt-topics.ps1) | Windows | Snapshot the live MQTT topic tree (sorted, unique) | No |
| [dump-mqtt-topics.sh](dump-mqtt-topics.sh) | Linux/macOS | Snapshot the live MQTT topic tree (sorted, unique) | No |

## Discovery

`discover-devices` sends an SSDP M-SEARCH multicast, queries common mDNS service types
(`_esphomelib._tcp`, `_hap._tcp`, `_mqtt._tcp`, `_http._tcp`), and falls back to the ARP
neighbour table. It does not modify anything — read-only reconnaissance.

```bash
# Linux / macOS
./scripts/discover-devices.sh 192.168.20.0/24

# Windows
.\scripts\discover-devices.ps1 -Range 192.168.20.0/24
```

## MQTT Topic Dump

`dump-mqtt-topics` wildcard-subscribes to `#` for a few seconds and prints the unique
set of topics seen — the fastest way to see what is actually on the bus before mapping it.

```bash
# Linux / macOS — host port seconds
./scripts/dump-mqtt-topics.sh 192.168.1.10 1883 20

# Windows
.\scripts\dump-mqtt-topics.ps1 -MqttHost 192.168.1.10 -Port 1883 -Seconds 20
```

## Naming Convention

`<verb>-<noun>.<ext>` — e.g. `discover-devices.sh`, `dump-mqtt-topics.ps1`, `flash-tasmota.sh`

## Script Header Template

```bash
#!/usr/bin/env bash
# PURPOSE:       <one-line description>
# USAGE:         ./<script-name> [args]
# PREREQUISITES: <tools required, e.g. mosquitto-clients, avahi-utils>
# REQUIRES:      <elevated | none>
```
