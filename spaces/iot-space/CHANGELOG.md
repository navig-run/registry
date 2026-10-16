# Changelog — NAVIG IoT Space

All notable changes to the `iot` space will be documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [1.0.0] — 2026-07-10

### Added

**Space created** — full IoT & smart-home command mesh bootstrapped from the
gold-standard space template.

**Skills (12)**
- `device-discover` — mDNS / SSDP / ARP device discovery and fingerprinting
- `mqtt-subscribe` — subscribe to topics and capture messages (mosquitto_sub)
- `mqtt-publish` — publish commands/config to a topic (mosquitto_pub), `$SYS` guarded
- `firmware-check` — read firmware versions from Tasmota / ESPHome / Shelly and flag drift
- `ota-update` — staged, dry-run-gated OTA update for Tasmota / ESPHome
- `tasmota-flash` — initial serial/OTA flash via esptool
- `energy-report` — aggregate power/energy across smart plugs from ENERGY telemetry
- `sensor-telemetry` — pull environment/health telemetry, flag low battery / offline
- `vlan-audit` — verify IoT VLAN isolation and detect boundary crossings
- `credential-audit` — probe for default credentials and anonymous MQTT
- `ha-entity-sync` — reconcile Home Assistant entities with the device registry
- `zigbee-scan` — enumerate the Zigbee/Z-Wave mesh via Zigbee2MQTT bridge topics

**Formations (5)**
- `discovery-sweep` — mDNS/SSDP/ARP discovery, fingerprint, registry (lead: beacon)
- `mqtt-ops` — broker health, topic mapping, message routing (lead: broker)
- `security-mesh` — segmentation, credential & CVE audit, intrusion watch (lead: warden)
- `firmware-fleet` — OTA rollouts, Tasmota/ESPHome flashing, version drift (lead: flux)
- `automation-loop` — scenes, schedules, triggers, HA sync (lead: automa)

**Agents (6)**
- `beacon` — device discovery cartographer (discovery-sweep)
- `broker` — message bus operator (mqtt-ops)
- `warden` — security & segmentation watcher (security-mesh)
- `flux` — firmware & OTA manager (firmware-fleet)
- `automa` — automation & scene orchestrator (automation-loop)
- `sensor` — telemetry & health monitor (discovery-sweep)

**Prompts (8)**
- `onboard-iot-device` · `discover-unknown-devices` · `mqtt-topic-map` · `firmware-update-plan`
- `security-segmentation-brief` · `energy-optimization` · `automation-design` · `weekly-iot-review`

**Workflows (6)**
- `morning-mesh-sweep` (daily) · `nightly-telemetry-sync` (nightly) · `security-review` (weekly)
- `device-onboard` (on-demand) · `firmware-audit` (on-demand) · `automation-review` (on-demand)

**Wiki (6 entries)**
- `architecture.md` · `devices.md` · `mqtt-topics.md`
- `segmentation.md` · `runbooks.md` · `agent-guide.md`

**Memory files (4)**
- `space-context.json` · `device-registry.example.json` · `known-issues.json` · `goals.json`

**Tool Packs (2)**
- `tools/mosquitto/pack.yaml` — Eclipse Mosquitto clients: sub / pub / health / tree
- `tools/esphome/pack.yaml` — ESPHome CLI: version / compile / run / logs / upload

**Scripts**
- `discover-devices.ps1` / `discover-devices.sh` — SSDP + mDNS + ARP discovery helpers
- `dump-mqtt-topics.ps1` / `dump-mqtt-topics.sh` — snapshot the live MQTT topic tree

**Tests**
- `test-device-discover.ps1` — smoke test covering ARP, SSDP multicast, mDNS, registry path

**Infrastructure**
- MCP config: `workstation.mcp.json` with per-agent tool allowlists, MQTT/firmware guards, security policy
- Inbox routes: `routes.yaml` with 6 channels, escalation rules, and notification settings
- `.gitignore` with sensible defaults for secrets, credentials, captures, and ESPHome artifacts

**Store assets**
- `space.manifest.json` — NAVIG Store manifest with all required fields
- `README.md` — publication-quality space documentation
- `PREVIEW.md` — store listing card
- `CHANGELOG.md` — this file
- `LICENSE` — MIT
- `screenshots/` — screenshot descriptor files

---

## [Unreleased]

*Planned for future versions:*
- `matter-commission` skill — commission Matter/Thread devices
- `zwave-heal` skill — trigger a Z-Wave network heal
- `camera-snapshot` skill — pull a still from RTSP/ONVIF cameras
- `automation-simulate` workflow — replay sensor events to test automations offline
- `cloud-block` workflow — enumerate and firewall-block IoT cloud phone-home endpoints
