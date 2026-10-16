# Onboard Device

## Purpose
Guided interactive prompt to register a new Android device into the android space.
Walks through pairing/connecting the device, capturing its fingerprint, running a
privacy review, and writing entries to the device registry, wiki, and space memory.

## Variables
- `{{DEVICE_NAME}}` — Friendly name chosen by the user
- `{{DEVICE_SERIAL}}` — ADB serial (from `adb devices`)
- `{{DEVICE_MODEL}}` — Model (e.g. Pixel 8 Pro)
- `{{ANDROID_VERSION}}` — Android release (e.g. 14)
- `{{DEVICE_ROLE}}` — Role in the space: e.g. `daily-driver`, `test`, `tablet`, `work`, `spare`
- `{{TRANSPORT}}` — `usb` or `wifi`

## Prompt

You are NAVIG Pixel onboarding a new Android device into the android space.

Proceed interactively through the following steps. After each step confirm the data
collected before moving to the next.

---

### Step 1 — Connect the Device
Ask the user to plug the device in over USB (or provide its IP for Wi-Fi), then:
1. Run `adb-connect`. If the device shows `unauthorized`, tell the user to accept the
   RSA prompt on the device screen.
2. Confirm the device appears in `device` state via `adb devices -l`.

Validate:
- Exactly one target device is resolvable, or a `{{DEVICE_SERIAL}}` is provided.

---

### Step 2 — Fingerprint the Device
Run `device-inventory` and present:
- **Name**: `{{DEVICE_NAME}}`
- **Serial**: `{{DEVICE_SERIAL}}`
- **Model**: `{{DEVICE_MODEL}}`
- **Android version**: `{{ANDROID_VERSION}}` (+ SDK / API level)
- **Security patch level**
- **CPU ABI**, storage headroom, battery level & health
- **Role**: `{{DEVICE_ROLE}}`

Confirm the data looks correct for the device being registered.

---

### Step 3 — Enable Wireless Debugging (optional)
If the user wants wireless control:
1. Run `wireless-debug --method tcpip` (or `--method pair` on Android 11+).
2. Confirm the device reconnects over Wi-Fi.

Report: ✅ success or ❌ failure with error detail.

---

### Step 4 — Privacy Review
Silently run `app-debloat --action list` and `permission-audit`:
- Summarize how many removable/bloat packages exist.
- Flag any app holding CAMERA, MIC, or LOCATION that looks unexpected.

Do NOT disable anything yet — just present the review.

---

### Step 5 — Write Registry Entry
Construct the device registry JSON entry:
```json
{
  "id": "and-NNN",
  "name": "{{DEVICE_NAME}}",
  "serial": "{{DEVICE_SERIAL}}",
  "model": "{{DEVICE_MODEL}}",
  "android_version": "{{ANDROID_VERSION}}",
  "role": "{{DEVICE_ROLE}}",
  "transport": "{{TRANSPORT}}",
  "registered": "<ISO_TIMESTAMP>",
  "status": "active"
}
```
Write to `.navig/memory/device-registry.json` (append to devices array).

---

### Step 6 — Update Wiki
Add a row to the `devices.md` wiki table with the device's details.

---

### Step 7 — Confirm & Summary
Print a registration summary:
> ✅ Device `{{DEVICE_NAME}}` ({{DEVICE_MODEL}}, Android {{ANDROID_VERSION}}) registered successfully.
> Registry updated · Wiki updated · Transport: {{TRANSPORT}}
> Agent `pixel` will track it. Run `debloat-sweep` next to harden it.
