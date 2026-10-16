# Agent Guide — iot space

> Who they are, what they own, how to invoke them.
> This guide is the authoritative reference for all agents in the `iot` space.

---

## Overview

The `iot` space runs six specialized agents, each owning a distinct operational domain.
They collaborate through formations and communicate via inbox channels.

| Agent | Role | Formation | Inbox Channel |
|-------|------|-----------|----------------|
| **beacon** | Device discovery cartographer | `discovery-sweep` | `#discovery` |
| **broker** | Message bus operator | `mqtt-ops` | `#mqtt` |
| **warden** | Security & segmentation watcher | `security-mesh` | `#security` |
| **flux** | Firmware & OTA manager | `firmware-fleet` | `#firmware` |
| **automa** | Automation & scene orchestrator | `automation-loop` | `#automation` |
| **sensor** | Telemetry & health monitor | `discovery-sweep` | `#telemetry` |

---

## beacon — Device Discovery Cartographer

**Role**: Maintains the living map of every device on the mesh. Beacon knows every plug,
bulb, sensor, and hub — its protocol, address, and fingerprint. When a device joins or
disappears, beacon is the first to know.

**Assigned formation**: `discovery-sweep`

**Triggers**:
- New device detected via mDNS / SSDP / ARP
- Discovery sweep requested
- Zigbee/Z-Wave coordinator reports a new pairing
- Device missing from a sweep that was previously present

**Capabilities**:
- Run `device-discover` across mDNS, SSDP, and ARP
- Run `zigbee-scan` to enumerate the Zigbee/Z-Wave mesh
- Fingerprint by MAC OUI, mDNS service type, HTTP banner
- Update `devices.md` and `device-registry.json`

**Inbox channel**: `#discovery`

**Example invocations**:
```
navig agent run beacon --task "Discover all devices on 192.168.20.0/24 and update the registry"
navig agent run beacon --task "Enumerate the Zigbee mesh via the coordinator"
navig agent run beacon --task "Discover and classify unknown devices"
```

---

## broker — Message Bus Operator

**Role**: Owns the MQTT message bus. Broker keeps the broker healthy, maps every topic,
and routes publish/subscribe traffic between devices, Home Assistant, and automations.

**Assigned formation**: `mqtt-ops`

**Triggers**:
- Broker restart detected (uptime reset)
- Device topic goes silent past its expected interval
- New unmapped topic appears on the bus
- Command needs publishing to a device

**Capabilities**:
- Run `mqtt-subscribe` on any topic filter (incl. wildcards)
- Run `mqtt-publish` to send commands / config
- Map the live topic tree via `$SYS` and wildcard subscriptions
- Update `mqtt-topics.md`

**Inbox channel**: `#mqtt`

**Example invocations**:
```
navig agent run broker --task "Map the entire live topic tree"
navig agent run broker --task "Subscribe to tele/# for 30 seconds and summarise"
navig agent run broker --task "Create an MQTT topic map"
```

---

## warden — Security & Segmentation Watcher

**Role**: Guardian of the mesh. Warden enforces VLAN isolation, hunts default
credentials, checks firmware against CVEs, and watches for rogue devices and cloud
phone-home traffic. It alerts — it never acts destructively without approval.

**Assigned formation**: `security-mesh`

**Triggers**:
- Device found crossing its VLAN boundary
- Default credentials accepted
- Firmware matches a known CVE
- Unexpected outbound connection detected

**Capabilities**:
- Run `vlan-audit`, `credential-audit`, and CVE checks
- Detect rogue / unregistered devices
- Write to `known-issues.json` with severity tagging
- Generate segmentation security briefs

**Inbox channel**: `#security`

**Example invocations**:
```
navig agent run warden --task "Create a security segmentation brief"
navig agent run warden --task "Verify VLAN isolation across the mesh"
navig agent run warden --task "Audit all devices for default credentials"
```

---

## flux — Firmware & OTA Manager

**Role**: Manages firmware across the whole fleet. Flux tracks installed versions,
diffs against releases, flashes Tasmota and ESPHome, and orchestrates staged OTA
rollouts — never flashing blind.

**Assigned formation**: `firmware-fleet`

**Triggers**:
- `firmware-check` finds a device behind the latest release
- A CVE requires an urgent update
- A new device needs initial flashing

**Capabilities**:
- Run `firmware-check`, `ota-update`, `tasmota-flash`
- Compile and deploy ESPHome configs
- Verify post-flash health and roll back on failure
- Record firmware versions in the registry

**Inbox channel**: `#firmware`

**Example invocations**:
```
navig agent run flux --task "Check firmware versions across the whole fleet"
navig agent run flux --task "Create a firmware update plan"
navig agent run flux --task "OTA-update plug-office (dry-run first)"
```

---

## automa — Automation & Scene Orchestrator

**Role**: Orchestrates the behaviour of the smart home — scenes, schedules, triggers,
and the entity graph. Automa keeps Home Assistant entities in sync with the registry
and turns operator intent into working automations.

**Assigned formation**: `automation-loop`

**Triggers**:
- New device that should join a scene
- Home Assistant entity list changes
- Scheduled scene time reached
- Operator requests a new automation

**Capabilities**:
- Run `ha-entity-sync` to reconcile HA entities with the registry
- Design and validate scenes and schedules
- Publish scene commands via `broker`
- Dry-run automations before enabling

**Inbox channel**: `#automation`

**Example invocations**:
```
navig agent run automa --task "Sync Home Assistant entities to the registry"
navig agent run automa --task "Design an automation for lights on at sunset in the living room"
navig agent run automa --task "Dry-run the bedtime scene"
```

---

## sensor — Telemetry & Health Monitor

**Role**: The diagnostic eye. Sensor watches energy and environment readings, battery
levels, uptime, and signal strength across every device, and alerts before a battery
dies or a device drops off.

**Assigned formation**: `discovery-sweep`

**Triggers**:
- Device telemetry stops arriving past its interval
- Battery drops below threshold
- Energy reading spikes or drops abnormally
- Nightly telemetry sync cycle

**Capabilities**:
- Run `sensor-telemetry` and `energy-report`
- Track battery levels and predict replacement
- Detect offline devices and degrading links
- Write health snapshots to memory

**Inbox channel**: `#telemetry`

**Example invocations**:
```
navig agent run sensor --task "Pull live telemetry from all devices"
navig agent run sensor --task "Recommend energy optimizations"
navig agent run sensor --task "List devices with battery below 20%"
```
