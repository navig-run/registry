# GENESIS — IoT Space

## Why This Exists

A smart home is a living mesh — dozens of plugs, bulbs, sensors, cameras, hubs, and controllers, speaking Wi-Fi, Zigbee, Z-Wave, Matter, and BLE, all talking at once. IoT Space is the command mesh that keeps it coherent, secure, and under control.

Without it: devices go undocumented, the MQTT bus becomes a mystery, firmware rots with unpatched CVEs, cheap gadgets phone home from inside the trusted network, and automations fire in ways nobody can explain.

## What It Does

IoT Space manages every layer of the smart-home stack:
- **Discovery & fingerprinting** — mDNS, SSDP, ARP, and the Zigbee mesh; a living device registry
- **MQTT message bus** — broker health, topic mapping, publish/subscribe routing
- **Firmware & OTA** — version tracking, Tasmota/ESPHome flashing, staged rollouts
- **Segmentation & security** — VLAN isolation, default-credential & CVE audits, rogue detection
- **Telemetry** — energy, environment, battery, uptime, offline detection
- **Automation** — scenes, schedules, triggers, Home Assistant entity sync

## Core Agents

| Agent | Role |
|-------|------|
| `beacon` | Discovers and fingerprints every device on the mesh |
| `broker` | Operates the MQTT bus — topic map, publish/subscribe |
| `warden` | Enforces segmentation; audits credentials and CVEs |
| `flux` | Tracks firmware and runs staged OTA rollouts |
| `automa` | Orchestrates scenes, schedules, and HA entity sync |
| `sensor` | Monitors telemetry, energy, battery, and offline devices |

## Primary Formations

- **`discovery-sweep`** — Discovery, fingerprinting, and registry maintenance
- **`mqtt-ops`** — Broker health, topic mapping, message routing
- **`security-mesh`** — Segmentation, credential & CVE audits, intrusion watch
- **`firmware-fleet`** — Version drift, OTA rollouts, Tasmota/ESPHome flashing
- **`automation-loop`** — Scenes, schedules, triggers, Home Assistant sync

## Origin

Built for smart-home operators and IoT tinkerers who want their mesh of devices to be as well-managed, segmented, and secure as a professional deployment — not a pile of unpatched gadgets on the flat home network.

---
*Space ID: `iot` · Runtime: `navig-space-2` · Tier: work*
