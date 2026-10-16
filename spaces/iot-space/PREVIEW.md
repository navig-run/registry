# NAVIG IoT Space

**Command mesh for every IoT & smart-home device you own.**

---

## What It Is

A production-grade NAVIG space for discovering, driving, securing, and automating every
smart-home device — plugs, bulbs, sensors, cameras, hubs, and controllers across
**Wi-Fi, Zigbee, Z-Wave, Matter, and BLE** — through the MQTT message bus and Home
Assistant. Fork it, point it at your broker and IoT VLAN, and you're operational in
under 10 minutes.

---

## Key Features

- **12 cross-platform skills** — device discovery, MQTT sub/pub, firmware check, OTA update, Tasmota flash, energy report, sensor telemetry, VLAN audit, credential audit, HA entity sync, Zigbee scan
- **6 specialized agents** — beacon (discovery), broker (MQTT bus), warden (security), flux (firmware), automa (automation), sensor (telemetry)
- **6 automated workflows** — morning mesh sweep, device onboarding, firmware audit, nightly telemetry sync, weekly security review, automation review
- **8 production prompts** — onboard device, discover unknowns, MQTT topic map, firmware plan, segmentation brief, energy optimization, automation design, weekly review
- **Full wiki starter kit** — architecture, device registry, MQTT topic map, segmentation plan, runbooks, agent guide

---

## Usage Example

```bash
# Activate the space
navig space use iot

# Discover every device on the IoT VLAN
navig skill run device-discover --range 192.168.20.0/24

# Full morning mesh sweep (discovery + telemetry + segmentation)
navig ask "run the morning-mesh-sweep workflow"

# Onboard a new device interactively
navig ask "run the device-onboard workflow"

# Get a segmentation security brief
navig agent run warden --task "Create a security segmentation brief"
```

---

**Platform**: Windows · Linux · macOS
**Category**: IoT · Smart Home · Automation
**Version**: 1.0.0
**License**: MIT
