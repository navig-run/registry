# NAVIG IoT Space

> **Command mesh for every IoT & smart-home device you own.**
> Fork it, point it at your broker, run it. Zero manual setup.

---

## Overview

The **iot** space is a complete NAVIG smart-home management environment designed for
operators who run a mesh of connected devices — plugs, bulbs, sensors, cameras, hubs,
and controllers — across Wi-Fi, Zigbee, Z-Wave, Matter, and BLE. It ships with
everything wired up: skills, agents, formations, automated workflows, a prompt library,
wiki starter kit, and operational memory files.

This is a **community reference space** — the canonical example of how a serious
smart-home NAVIG space is structured. Fork it, point it at your MQTT broker and IoT
VLAN, and you are operational in under 10 minutes.

---

## Architecture

```
iot-space/
├── .navig/
│   ├── config.yaml           — space configuration (broker, VLAN, HA)
│   ├── context.md            — space narrative context
│   ├── skills/               — 12 cross-platform skills
│   ├── store/
│   │   ├── agents/           — 6 specialized agents
│   │   ├── formations/       — 5 operational formations
│   │   ├── prompts/          — 8 production-ready prompts
│   │   ├── workflows/        — 6 workflow playbooks
│   │   └── mcp/              — MCP server configuration
│   ├── wiki/                 — 7 starter wiki entries
│   ├── memory/               — example memory files (*.example.json)
│   └── inbox/                — inbox routing rules (routes.example.yaml)
├── tools/                    — mosquitto + esphome tool packs
├── space.manifest.json       — NAVIG Store manifest
├── README.md                 — this file
├── PREVIEW.md                — store listing card
├── CHANGELOG.md              — version history
└── LICENSE                   — MIT
```

### Network Layout (default)

```
Internet
    │
[Router/Gateway]  192.168.1.1
    │
    ├── [Trusted LAN]  192.168.1.0/24
    │     ├── mqtt-broker      192.168.1.10   Mosquitto + Home Assistant
    │     └── [your PCs]
    │
    └── [IoT VLAN 20]  192.168.20.0/24   ← isolated, no route INTO trusted LAN
          ├── plug-office      192.168.20.31  Tasmota
          ├── sensor-hall      (Zigbee)       via Zigbee2MQTT
          └── [your devices]   192.168.20.x   (register via device-onboard workflow)
```

---

## Skills

| Skill | Description | Platforms |
|-------|-------------|-----------|
| `device-discover` | Discover devices via mDNS / SSDP / ARP | All |
| `mqtt-subscribe` | Subscribe to topics and capture messages | All |
| `mqtt-publish` | Publish commands/config to a topic | All |
| `firmware-check` | Read firmware versions and flag drift | All |
| `ota-update` | Staged OTA update for Tasmota / ESPHome | All |
| `tasmota-flash` | Initial serial/OTA flash of ESP devices | All |
| `energy-report` | Summarize power/energy across smart plugs | All |
| `sensor-telemetry` | Pull environment/health telemetry | All |
| `vlan-audit` | Verify IoT VLAN isolation holds | All |
| `credential-audit` | Probe for default/factory credentials | All |
| `ha-entity-sync` | Reconcile HA entities with the registry | All |
| `zigbee-scan` | Enumerate the Zigbee/Z-Wave mesh | All |

---

## Formations

| Formation | Agents | Purpose |
|-----------|--------|---------|
| `discovery-sweep` | beacon, sensor, warden | mDNS/SSDP/ARP discovery, fingerprint, registry |
| `mqtt-ops` | broker, automa | Broker health, topic map, message routing |
| `security-mesh` | warden, beacon | Segmentation, credential & CVE audit, rogue watch |
| `firmware-fleet` | flux, sensor | OTA rollouts, Tasmota/ESPHome flashing, version drift |
| `automation-loop` | automa, broker | Scenes, schedules, triggers, HA sync |

---

## Agent Roster

| Agent | Role | Formation | Inbox |
|-------|------|-----------|-------|
| **beacon** | Device discovery cartographer | discovery-sweep | `#discovery` |
| **broker** | Message bus operator | mqtt-ops | `#mqtt` |
| **warden** | Security & segmentation watcher | security-mesh | `#security` |
| **flux** | Firmware & OTA manager | firmware-fleet | `#firmware` |
| **automa** | Automation & scene orchestrator | automation-loop | `#automation` |
| **sensor** | Telemetry & health monitor | discovery-sweep | `#telemetry` |

---

## Prompt Library

| Prompt | Purpose |
|--------|---------|
| `onboard-iot-device` | Guided new device registration |
| `discover-unknown-devices` | Reconcile a sweep against the registry |
| `mqtt-topic-map` | Turn a bus capture into a topic map |
| `firmware-update-plan` | Staged OTA rollout plan |
| `security-segmentation-brief` | Segmentation + creds + CVE + rogue brief |
| `energy-optimization` | Find consumers and propose savings |
| `automation-design` | Turn a request into a validated automation |
| `weekly-iot-review` | Weekly mesh review with checklist |

---

## Workflows

| Workflow | Schedule | Description |
|----------|----------|-------------|
| `morning-mesh-sweep` | Daily 07:00 | Discovery → telemetry → offline check → segmentation glance |
| `device-onboard` | On-demand | Interactive new device registration flow |
| `firmware-audit` | On-demand | Version drift + CVE + staged rollout plan |
| `nightly-telemetry-sync` | Nightly 01:00 | Telemetry + energy snapshot + low-battery alerts |
| `security-review` | Weekly Sun 03:00 | VLAN + creds + CVE + rogue detection |
| `automation-review` | On-demand | HA entity sync + scene dry-run + drift |

---

## Quickstart Guide

### 1. Install NAVIG

See [navig.run/install](https://navig.run/install).

### 2. Install the space

```
navig space install github:navig-run/registry/spaces/iot-space
navig space use iot-space
```

### 3. Seed and customize for your environment

The space ships example state only. Copy each example to its live name, then edit it:

```
.navig/memory/space-context.example.json      → space-context.json      (mqtt, primary_network, home_assistant)
.navig/memory/device-registry.example.json    → device-registry.json    (replace the two example devices)
.navig/memory/iot-port-baseline.example.json  → iot-port-baseline.json  (ports each device class may expose)
.navig/memory/known-issues.example.json       → known-issues.json
.navig/memory/goals.example.json              → goals.json
.navig/inbox/routes.example.yaml              → routes.yaml
```

Then set `mqtt_host`, `iot_subnet`, `iot_vlan` and `ha_url` in `.navig/config.yaml`.

### 4. Run your first discovery

```
navig skill run device-discover --range 192.168.20.0/24
```

### 5. Onboard your first device and start the morning mesh sweep

Workflows in `.navig/store/workflows/` are playbooks the space's agents follow:

```
navig ask "run the device-onboard workflow"
navig ask "run the morning-mesh-sweep workflow"
```

---

## Sharing

The `.gitignore` in this space excludes:
- Secrets, vault data, and MQTT/HA credentials
- Local log files and MQTT captures
- Your live memory files and inbox routes (only the `*.example.*` seeds are committed)
- ESPHome build artifacts and `secrets.yaml`

Everything else (skills, agents, formations, workflows, prompts, wiki structure,
example memory) is safe to commit and share.

---

## Requirements

| Tool | Required | Purpose |
|------|----------|---------|
| NAVIG | ✅ Required | Core runtime |
| mosquitto-clients | ✅ Required | `mqtt-subscribe` / `mqtt-publish` / telemetry |
| esphome | Optional | ESPHome flashing (`ota-update`, `tasmota-flash`) |
| esptool | Optional | Initial serial flashing |
| nmap | Optional | `device-discover` / `vlan-audit` (falls back to ARP) |
| avahi-utils / Bonjour | Optional | mDNS discovery |

---

## Contributing

This is a community reference space. Improvements, additional skills, and agent
enhancements are welcome — open a pull request at
[github.com/navig-run/registry](https://github.com/navig-run/registry).

---

## License

MIT — see [LICENSE](LICENSE)
