# Space Architecture

**Space**: `iot-space`
**Root**: the folder containing `.navig/` (installed: `~/.navig/spaces/iot-space`)
**Last Updated**: 2026-07-10
**Maintained by**: Beacon

---

## Overview

The `iot` space is a unified command mesh for every IoT and smart-home device —
plugs, bulbs, sensors, cameras, hubs, and controllers across Wi-Fi, Zigbee, Z-Wave,
Matter, and BLE. It provides a single namespace for discovering, driving, securing,
and automating heterogeneous devices through the MQTT message bus, Home Assistant, and
the NAVIG agent framework.

The space is designed to be cloned, forked, and operated by anyone running a smart home
or a small IoT deployment who wants professional-grade discovery, segmentation, firmware
control, and automation.

---

## Core Design Principles

| Principle | Description |
|---|---|
| **Bus-Centric** | MQTT is the backbone — every device state and command flows through the broker |
| **Registry-Driven** | All device knowledge lives in `device-registry.json` — no hardcoded IPs anywhere |
| **Segmented by Default** | IoT devices are untrusted and isolated on their own VLAN |
| **Self-Documenting** | Every event writes to memory; every significant change updates the wiki |
| **Layered Agents** | Six specialist agents cover discovery, bus, security, firmware, automation, and telemetry without overlap |
| **Scheduled Automation** | Morning mesh sweep, nightly telemetry sync, and weekly security review run unattended |

---

## Formation Layer

Formations group agents around operational concerns:

```
discovery-sweep     ← beacon + sensor + warden (mDNS/SSDP/ARP, fingerprint, registry)
mqtt-ops            ← broker + automa (broker health, topic map, routing)
security-mesh       ← warden + beacon (segmentation, creds, CVE, rogue watch)
firmware-fleet      ← flux + sensor (version drift, OTA, Tasmota/ESPHome flashing)
automation-loop     ← automa + broker (scenes, schedules, HA entity sync)
```

---

## Agent Layer

| Agent | Domain | Inbox |
|---|---|---|
| `beacon` | Device discovery cartographer | `#discovery` |
| `broker` | Message bus operator | `#mqtt` |
| `warden` | Security & segmentation | `#security` |
| `flux` | Firmware & OTA | `#firmware` |
| `automa` | Automation & scenes | `#automation` |
| `sensor` | Telemetry & health | `#telemetry` |

---

## Workflow Layer

| Workflow | Schedule | Purpose |
|---|---|---|
| `morning-mesh-sweep` | Daily 07:00 | Discovery + telemetry + offline + segmentation glance |
| `nightly-telemetry-sync` | Daily 01:00 | Telemetry + energy snapshot + low-battery alerts |
| `security-review` | Sunday 03:00 | VLAN + creds + CVE + rogue detection |
| `firmware-audit` | On-demand | Version drift + CVE + staged rollout plan |
| `device-onboard` | On-demand | Register a new device interactively |
| `automation-review` | On-demand | HA entity sync + scene dry-run + drift |

---

## Directory Structure

```
iot-space\
├── .navig\
│   ├── config.yaml              ← Space configuration
│   ├── context.md               ← Space narrative context
│   ├── skills\                  ← Skill definitions (12)
│   ├── store\
│   │   ├── agents\              ← Agent definitions (6)
│   │   ├── formations\          ← Formation definitions (5)
│   │   ├── workflows\           ← Workflow definitions (6)
│   │   ├── prompts\             ← Reusable prompt library (8)
│   │   └── mcp\                 ← MCP server configuration
│   ├── memory\                  ← Structured memory assets (*.example.json seeds)
│   ├── inbox\                   ← Inbox routing rules (routes.example.yaml seed)
│   └── wiki\                    ← Operational wiki
│       └── history\             ← Archived weekly reviews
├── tools\                       ← mosquitto + esphome tool packs
├── space.manifest.json          ← NAVIG Store manifest
├── README.md                    ← Publication-quality readme
├── PREVIEW.md                   ← Store listing card
├── CHANGELOG.md                 ← Version history
├── LICENSE                      ← MIT license
└── .gitignore                   ← Space gitignore
```

---

## Data Flow

```
User Intent / Schedule Trigger
        ↓
   NAVIG Inbox (routes.yaml)
        ↓
   Agent (yaml definition)
        ↓
   Formation (context + peers)
        ↓
   Skill (cross-platform execution — MQTT / HTTP / discovery)
        ↓
   Output → Memory / Wiki / Report
```

---

## Configuration

Key settings in `.navig/config.yaml`:

```yaml
space: iot-space
mqtt_host: "192.168.1.10"           # UPDATE to your broker
mqtt_port: 1883
iot_subnet: "192.168.20.0/24"       # UPDATE to your IoT VLAN subnet
iot_vlan: 20
ha_url: "http://192.168.1.10:8123"  # UPDATE to your Home Assistant
mosquitto_bin: ""                   # empty = resolve mosquitto_sub/pub from PATH
```

All device and broker credentials are stored in the space vault — never in this file.

---

## Getting Started

1. Install the space: `navig space install github:navig-run/registry/spaces/iot-space`
2. Copy the `.navig/memory/*.example.json` seeds to their live names; set your broker in
   `.navig/config.yaml` → `mqtt_host`
3. Set your IoT subnet/VLAN: `iot_subnet`, `iot_vlan`
4. Register your first device: `navig ask "run the device-onboard workflow"`
5. Run the morning mesh sweep: `navig ask "run the morning-mesh-sweep workflow"`
6. View the status: `navig space check iot-space --no-interactive`
