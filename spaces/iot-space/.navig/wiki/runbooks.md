# Runbooks Index — iot space

> Operational runbooks linking skills, workflows, and agent responsibilities.
> Last updated: 2026-07-10

---

## Quick Reference

| Situation | Runbook | Primary Agent | Skills Used |
|-----------|---------|---------------|-------------|
| New device arrived | [Device Onboarding](#device-onboarding) | beacon | device-discover, firmware-check |
| Unknown device on mesh | [Rogue Triage](#rogue-triage) | warden | device-discover, vlan-audit |
| Device gone silent | [Offline Device](#offline-device) | sensor | sensor-telemetry, mqtt-subscribe |
| Firmware behind | [Firmware Rollout](#firmware-rollout) | flux | firmware-check, ota-update |
| Default credentials | [Credential Hardening](#credential-hardening) | warden | credential-audit |
| Segment leak | [Segmentation Response](#segmentation-response) | warden | vlan-audit |
| New automation | [Automation Build](#automation-build) | automa | ha-entity-sync, mqtt-publish |
| Pair a Zigbee device | [Zigbee Pairing](#zigbee-pairing) | beacon | zigbee-scan |
| Weekly review | [Weekly Review](#weekly-review) | all agents | all skills |

---

## Device Onboarding

**Trigger**: New IoT device added to the space.

**Step 1 — Run interactive onboarding workflow**
```
navig ask "run the device-onboard workflow"
```

**Step 2 — Fingerprint**
```
navig skill run device-discover --range <device-ip>/32 --method all
```

**Step 3 — Confirm MQTT topic**
```
navig skill run mqtt-subscribe --topic <base-topic>/# --count 3
```

**Resolution criteria**: Device in registry, reachable, topic mapped, wiki updated.

---

## Rogue Triage

**Trigger**: Discovery finds a device not in the registry.

**Step 1 — Sweep and diff**
```
navig skill run device-discover --range 192.168.20.0/24 --method all
navig agent run beacon --task "Discover and classify unknown devices"
```

**Step 2 — Check segment membership**
```
navig skill run vlan-audit
```

**Step 3 — Decide**: onboard (`beacon`) or investigate/quarantine (`warden`).

**Resolution criteria**: Every device on the mesh is either registered or quarantined.

---

## Offline Device

**Trigger**: A previously-active device stops publishing telemetry.

**Step 1 — Confirm silence**
```
navig skill run sensor-telemetry --topic tele/<device>/# --duration 20
```

**Step 2 — Probe reachability**
```
navig skill run mqtt-subscribe --topic stat/<device>/# --count 1 --duration 10
```

**Step 3 — If mains Wi-Fi and truly offline** — check power/AP; log to known-issues.
Sleepy Zigbee/BLE devices reporting on interval are NOT offline.

**Resolution criteria**: Device publishing again, or root cause documented.

---

## Firmware Rollout

**Trigger**: `firmware-check` finds version drift or a CVE.

**Step 1 — Inventory (dry)**
```
navig skill run firmware-check --target all
navig agent run flux --task "Create a firmware update plan"
```

**Step 2 — OTA in waves (dry-run each first)**
```
navig skill run ota-update --target <device> --platform tasmota
navig skill run ota-update --target <device> --platform tasmota --dry_run false
```

**Step 3 — Verify**
```
navig skill run mqtt-subscribe --topic tele/<device>/STATE --count 1 --duration 60
```

**Resolution criteria**: Devices on target firmware, all rejoined and publishing.

---

## Credential Hardening

**Trigger**: `credential-audit` accepts a default username/password.

**Step 1 — Audit**
```
navig skill run credential-audit --target <device>
```

**Step 2 — Rotate** — set a strong password in the device UI (operator action), then
re-audit to confirm the default is rejected.

**Resolution criteria**: All default pairs rejected; anonymous MQTT disabled.

---

## Segmentation Response

**Trigger**: `vlan-audit` finds a device crossing its VLAN boundary.

**Step 1 — Confirm the leak**
```
navig skill run vlan-audit
```

**Step 2 — Contain** — tighten the firewall rule for that device/segment (operator
action), then re-audit.

**Step 3 — Document** in `segmentation.md` and `known-issues.json`.

**Resolution criteria**: Isolation probe fails (as intended); no device crosses the boundary.

---

## Automation Build

**Trigger**: Operator wants a new scene, schedule, or trigger.

**Step 1 — Sync entities**
```
navig skill run ha-entity-sync
```

**Step 2 — Design**
```
navig agent run automa --task "Design an automation for <plain-language request>"
```

**Step 3 — Dry-run then enable**
```
navig agent run automa --task "Dry-run the new automation, then enable if it passes"
```

**Resolution criteria**: Automation passes dry-run, resolves to real devices, enabled.

---

## Zigbee Pairing

**Trigger**: Adding a new Zigbee (or Z-Wave) device.

**Step 1 — Open the network**
```
navig skill run zigbee-scan --permit_join true
```

**Step 2 — Pair the device** (put it in pairing mode within the 120s window).

**Step 3 — Confirm and register**
```
navig skill run zigbee-scan
navig ask "run the device-onboard workflow"
```

**Resolution criteria**: Device appears in the mesh list and is registered.

---

## Weekly Review

**Trigger**: Every Sunday or on demand.

```
navig ask "run the security-review workflow"
navig agent run sensor --task "Prepare the weekly IoT review"
```

Collects reports from all agents and writes a wiki entry at `.navig/wiki/history/iot-review-<date>.md`.

**Resolution criteria**: Wiki entry written, critical issues acknowledged, `known-issues.json` updated.
