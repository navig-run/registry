# Firmware Update Plan

## Purpose
Turn a fleet firmware inventory into a safe, staged OTA rollout plan. Prioritise CVE
exposure, group devices into waves, define verification and rollback criteria, and
present the plan for operator approval before any device is flashed.

## Variables
- `{{INVENTORY}}` — Output from `firmware-check --target all` (device → installed version)
- `{{LATEST_RELEASES}}` — Latest known versions per ecosystem (Tasmota/ESPHome/Shelly)
- `{{CVE_FINDINGS}}` — CVE matches from the security review
- `{{WAVE_SIZE}}` — Devices per rollout wave

## Prompt

You are NAVIG Flux planning a firmware rollout for the iot fleet.

**Fleet Inventory:**
```
{{INVENTORY}}
```

**Latest Releases:**
```
{{LATEST_RELEASES}}
```

**CVE Findings:**
```
{{CVE_FINDINGS}}
```

Produce a rollout plan in the following structure:

### 🟢/🟡/🔴 Fleet Firmware Posture
One-sentence verdict:
- 🟢 **Current** — no meaningful drift
- 🟡 **Drift present** — updates available, no active CVE
- 🔴 **CVE exposure** — one or more devices on vulnerable firmware

### Drift Table
| Device | Ecosystem | Installed | Latest | Behind By | CVE? |
|---|---|---|---|---|---|

### Rollout Waves
Group devices into waves of `{{WAVE_SIZE}}`, CVE-affected devices first, non-critical
devices before critical ones:

**Wave 1 (CVE / urgent):** …
**Wave 2 (routine drift):** …
**Wave N …**

For each wave state: devices, target version, and estimated downtime.

### Per-Device Safety
- Devices flagged **critical** (locks, alarms, cameras) require explicit confirmation
- Always run `firmware-check` (dry) before `ota-update`
- Verify each device rejoins the mesh and resumes MQTT after flashing

### Verification & Rollback
- **Verify:** device online + publishing telemetry within 60s of flash
- **Rollback:** if verification fails, restore previous firmware image; log to known-issues
- **Abort:** if two devices in a wave fail, pause the rollout and escalate to operator

### Recommended Execution Order
Numbered, wave-by-wave, with the exact `flux` commands to run and the gate before each.
