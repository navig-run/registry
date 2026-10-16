# Onboard IoT Device

## Purpose
Guided interactive prompt to register a new IoT / smart-home device into the iot space.
Walks through capturing device metadata, fingerprinting, MQTT reachability, optional
firmware flashing, and writing entries to the device registry, wiki, and space memory.

## Variables
- `{{DEVICE_NAME}}` — Friendly name chosen by the user (e.g. `plug-office`)
- `{{DEVICE_IP}}` — Static IP on the IoT VLAN or DHCP lease
- `{{DEVICE_MAC}}` — MAC address
- `{{DEVICE_PROTOCOL}}` — Protocol: `wifi`, `zigbee`, `zwave`, `matter`, `ble`
- `{{DEVICE_TYPE}}` — Class: `plug`, `bulb`, `sensor`, `camera`, `hub`, `controller`, `meter`
- `{{DEVICE_FIRMWARE}}` — Ecosystem: `tasmota`, `esphome`, `shelly`, `zigbee2mqtt`, `vendor`
- `{{DEVICE_MQTT_TOPIC}}` — Base topic (e.g. `cmnd/plug-office`)
- `{{DEVICE_LOCATION}}` — Room / location

## Prompt

You are NAVIG Beacon onboarding a new IoT device into the iot space.

Proceed interactively through the following steps. After each step confirm the data
collected before moving to the next.

---

### Step 1 — Capture Device Identity
Ask the user for (or confirm the pre-filled values):
- **Name**: `{{DEVICE_NAME}}`
- **IP Address**: `{{DEVICE_IP}}`
- **MAC Address**: `{{DEVICE_MAC}}`
- **Protocol**: `{{DEVICE_PROTOCOL}}`
- **Type**: `{{DEVICE_TYPE}}`
- **Firmware ecosystem**: `{{DEVICE_FIRMWARE}}`
- **MQTT base topic**: `{{DEVICE_MQTT_TOPIC}}` (optional)
- **Location**: `{{DEVICE_LOCATION}}`
- **Notes** (optional, e.g. "Sonoff S31, 16A energy monitoring")

Validate:
- IP is reachable (ping) — or note it is a sleepy battery device
- MAC format is valid (XX:XX:XX:XX:XX:XX) and OUI resolves to a known IoT vendor
- Protocol and type values are from the supported sets

---

### Step 2 — Fingerprint & Reachability
Run the following checks and report results:
1. mDNS / SSDP / ARP fingerprint (`device-discover` on the /32)
2. HTTP UI probe — is `http://{{DEVICE_IP}}/` a Tasmota/ESPHome/Shelly UI?
3. MQTT probe — subscribe to `{{DEVICE_MQTT_TOPIC}}/#` and confirm the device talks

Report: ✅ success or ❌ failure with detail for each check.

---

### Step 3 — Firmware Check (if HTTP reachable)
Run `firmware-check` on the device and present:
- Installed firmware version
- Latest available version for that ecosystem
- Whether an OTA update is recommended now (defer flashing to `flux`)

---

### Step 4 — Write Registry Entry
Construct the device registry JSON entry:
```json
{
  "name": "{{DEVICE_NAME}}",
  "ip": "{{DEVICE_IP}}",
  "mac": "{{DEVICE_MAC}}",
  "protocol": "{{DEVICE_PROTOCOL}}",
  "type": "{{DEVICE_TYPE}}",
  "firmware": "{{DEVICE_FIRMWARE}}",
  "mqtt_topic": "{{DEVICE_MQTT_TOPIC}}",
  "location": "{{DEVICE_LOCATION}}",
  "vlan": 20,
  "registered": "<ISO_TIMESTAMP>",
  "status": "active"
}
```
Write to `.navig/memory/device-registry.json` (append to devices array).

---

### Step 5 — Update Wiki
Add a row to the `devices.md` wiki table, and register the device's topic in `mqtt-topics.md`.

---

### Step 6 — Confirm & Summary
Print a registration summary:
> ✅ Device `{{DEVICE_NAME}}` ({{DEVICE_IP}}) registered successfully.
> Registry updated · Wiki updated · MQTT topic mapped · Firmware: [CURRENT/DRIFT].
> Agent `beacon` notified. Agent `sensor` will begin monitoring telemetry shortly.
