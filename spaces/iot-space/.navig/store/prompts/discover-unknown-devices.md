# Discover Unknown Devices

## Purpose
Run a full discovery sweep and identify every device on the network that is NOT in the
IoT device registry. Fingerprint each unknown, classify it, and produce an actionable
list of onboarding candidates and potential rogues.

## Variables
- `{{DISCOVERY_DATA}}` — Output from `device-discover` (mDNS + SSDP + ARP)
- `{{REGISTRY}}` — Current `device-registry.json` contents
- `{{SCAN_DATE}}` — ISO timestamp of the sweep
- `{{IOT_SUBNET}}` — The subnet IoT devices are expected on

## Prompt

You are NAVIG Beacon reconciling a fresh discovery sweep against the device registry.

Sweep date: `{{SCAN_DATE}}` | IoT subnet: `{{IOT_SUBNET}}`

**Discovery Data:**
```
{{DISCOVERY_DATA}}
```

**Known Registry:**
```
{{REGISTRY}}
```

Produce a reconciliation report in the following structure:

### 🟢/🟡/🔴 Mesh Integrity
One-sentence verdict:
- 🟢 **Clean** — every discovered device is registered
- 🟡 **Unregistered devices present** — new but plausibly benign
- 🔴 **Possible rogue** — device on a segment it should not be, or unidentifiable

### Unknown Devices Table
For each device in discovery but not in the registry:

| IP | MAC | Vendor (OUI) | mDNS/SSDP Service | Likely Type | Verdict |
|---|---|---|---|---|---|

Verdict values: `onboard`, `investigate`, `ignore (infra)`.

### Fingerprint Detail
For each unknown, state what the fingerprint tells you:
- MAC OUI → vendor (e.g. `Espressif`, `Sonoff`, `Philips`)
- mDNS service type → ecosystem (`_esphomelib._tcp` → ESPHome, `_hap._tcp` → HomeKit)
- HTTP banner → Tasmota / Shelly / vendor UI

### Missing Devices
Devices in the registry that did NOT appear in this sweep:
- List name, IP, last-seen — flag as possibly offline (sleepy Zigbee OK, mains Wi-Fi not).

### Recommended Actions (Prioritised)
Numbered list, most urgent first. Be specific: which device, onboard vs investigate,
and which agent should act (`beacon` onboard, `warden` investigate rogue).
