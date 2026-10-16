# Onboard Device

## Purpose
Guided interactive prompt to register a new device into the homelab space.
Walks through capturing all required metadata, testing connectivity, and writing
entries to the device registry, wiki, and space memory.

## Variables
- `{{DEVICE_NAME}}` — Friendly name chosen by the user
- `{{DEVICE_IP}}` — Static IP or DHCP lease
- `{{DEVICE_MAC}}` — MAC address
- `{{DEVICE_OS}}` — Operating system: `windows`, `linux`, `macos`, `embedded`
- `{{DEVICE_ROLE}}` — Role in the space: e.g. `homelab`, `server`, `nas`, `iot`, `laptop`
- `{{DEVICE_LOCATION}}` — Physical location: e.g. `desk-left`, `server-rack-u3`, `living-room`

## Prompt

You are NAVIG Archivist onboarding a new device into the homelab space.

Proceed interactively through the following steps. After each step confirm the data
collected before moving to the next.

---

### Step 1 — Capture Device Identity
Ask the user for (or confirm the pre-filled values):
- **Name**: `{{DEVICE_NAME}}`
- **IP Address**: `{{DEVICE_IP}}`
- **MAC Address**: `{{DEVICE_MAC}}`
- **Operating System**: `{{DEVICE_OS}}`
- **Role**: `{{DEVICE_ROLE}}`
- **Location**: `{{DEVICE_LOCATION}}`
- **Owner / Primary User** (optional)
- **Notes** (optional, e.g. "NAS running TrueNAS, 4-bay")

Validate:
- IP is reachable (ping test)
- MAC format is valid (XX:XX:XX:XX:XX:XX)
- OS value is one of the supported types

---

### Step 2 — Connectivity Test
Run the following checks and report results:
1. ICMP ping — measure RTT
2. SSH test (if OS is linux/macos/windows-with-openssh) — confirm auth works
3. Port probe — check for standard ports: 22 (SSH), 3389 (RDP), 5985 (WinRM), 80/443 (web UI)

Report: ✅ success or ❌ failure with error detail for each check.

---

### Step 3 — Hardware Fingerprint (if SSH available)
Silently run `hardware-inventory` on the device and present:
- CPU model and core count
- RAM total
- Storage devices
- GPU if present

Confirm the data looks correct for the device being registered.

---

### Step 4 — Write Registry Entry
Construct the device registry JSON entry:
```json
{
  "name": "{{DEVICE_NAME}}",
  "ip": "{{DEVICE_IP}}",
  "mac": "{{DEVICE_MAC}}",
  "os": "{{DEVICE_OS}}",
  "role": "{{DEVICE_ROLE}}",
  "location": "{{DEVICE_LOCATION}}",
  "registered": "<ISO_TIMESTAMP>",
  "status": "active"
}
```
Write to `.navig/memory/device-registry.json` (append to devices array).

---

### Step 5 — Update Wiki
Add a row to the `devices.md` wiki table with the device's details.

---

### Step 6 — Confirm & Summary
Print a registration summary:
> ✅ Device `{{DEVICE_NAME}}` ({{DEVICE_IP}}) registered successfully.
> Registry updated · Wiki updated · Connectivity: [PASS/PARTIAL/FAIL]
> Agent `atlas` notified. Agent `pulse` will begin monitoring in 15 min.
