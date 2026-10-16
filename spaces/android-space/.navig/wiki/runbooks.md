# Runbooks Index — android space

> Operational runbooks linking skills, workflows, and agent responsibilities.
> Last updated: 2026-07-10

---

## Quick Reference

| Situation | Runbook | Primary Agent | Skills Used |
|-----------|---------|---------------|-------------|
| Device won't connect | [ADB Triage](#adb-triage) | bridge | adb-connect, wireless-debug |
| New device arrived | [Device Onboarding](#device-onboarding) | pixel + bridge | adb-connect, device-inventory |
| Too much bloatware | [Debloat](#debloat) | scrub | app-debloat, permission-audit |
| App crashing | [App Crash Triage](#app-crash-triage) | bridge | logcat-capture |
| Sideload an app | [Sideload APK](#sideload-apk) | installer | apk-install |
| Battery draining fast | [Battery Investigation](#battery-investigation) | pixel | battery-report |
| Need photos off the phone | [Media Backup](#media-backup) | keeper | file-transfer |
| Switching phones | [Phone Migration](#phone-migration) | keeper + installer | app-backup, apk-extract |

---

## ADB Triage

**Trigger**: Device shows `unauthorized`, `offline`, or `no devices found`.

**Step 1 — Restart the daemon**
```
navig skill run adb-connect --restart_server true
```

**Step 2 — If `unauthorized`**: unlock the device, accept the "Allow USB debugging?" prompt (tick "Always allow").

**Step 3 — If still nothing**: try another **data** cable/port; confirm USB mode is File Transfer (MTP); check the ADB driver (Windows Device Manager).

**Step 4 — Wireless dropped**
```
navig skill run wireless-debug --method tcpip --host <device-ip>
```

**Resolution criteria**: Device shows `device` state in `adb devices -l`. See `diagnose-adb` prompt for the full tree.

---

## Device Onboarding

**Trigger**: New phone or tablet added to the fleet.

**Step 1 — Run the onboarding workflow**
```
navig ask "run the new-device-onboard workflow"
```

**Step 2 — Fingerprint**
```
navig skill run device-inventory
```

**Step 3 — Enable wireless (optional)**
```
navig skill run wireless-debug --method tcpip --host <device-ip>
```

**Resolution criteria**: Device in `device-registry.json`, appears in `devices.md`, reachable by serial, assigned a role.

---

## Debloat

**Trigger**: New device, or a privacy sweep is due.

**Step 1 — List what's removable**
```
navig skill run app-debloat --action list
```

**Step 2 — Build a plan** (see `debloat-plan` prompt), matched against `debloat-catalog.md`.

**Step 3 — Disable (dry-run first, then execute)**
```
navig skill run app-debloat --package <pkg>                 # dry-run
navig skill run app-debloat --package <pkg> --dry_run false # execute
```

**Step 4 — Audit permissions**
```
navig skill run permission-audit
```

**Resolution criteria**: Bloat disabled (reversibly), over-privileged apps logged in `known-issues.json`. Nothing from the 🔴 list touched.

---

## App Crash Triage

**Trigger**: An app crashes, ANRs, or misbehaves.

**Step 1 — Capture the crash**
```
navig skill run logcat-capture --clear_first true --package <pkg> --priority E --mode stream
# reproduce the crash, then stop
```

**Step 2 — Triage** using the `logcat-triage` prompt: find `FATAL EXCEPTION` / `ANR in`, attribute to a package, identify root cause.

**Resolution criteria**: Root cause identified (app bug / permission / OOM / environment) and next step given.

---

## Sideload APK

**Trigger**: Install an app that isn't on a store.

**Step 1 — Install**
```
navig skill run apk-install --apk_path <path-to.apk>
```

**Step 2 — Split bundle?**
```
navig skill run apk-install --apk_path <folder-of-splits> --grant_perms true
```

**Resolution criteria**: Package appears in `pm list packages -3` and launches.

---

## Battery Investigation

**Trigger**: A device's battery drains abnormally or runs hot.

**Step 1 — Report**
```
navig skill run battery-report --top_apps 10
```

**Step 2 — Review** top consumers; check temperature and health code.

**Resolution criteria**: Offending app identified or health flagged in `known-issues.json`.

---

## Media Backup

**Trigger**: Pull photos/videos/downloads off a device.

**Step 1 — Media pull**
```
navig skill run file-transfer --direction media --dest devices/media
```

**Step 2 — Verify** the pulled byte count is non-zero and >= expected.

**Resolution criteria**: Media present under `devices/media`, verified by keeper.

---

## Phone Migration

**Trigger**: Moving from an old phone to a new one.

**Step 1 — Follow the migration prompt**
```
navig agent run keeper --task "Plan a migration to a new phone"
```

**Step 2 — Back up old** (media pull + APK extract + app-backup), **restore to new** (apk-install + push media).

**Step 3 — Verify parity** (app count, media count, key apps launch).

**Resolution criteria**: New device matches old; parity table all ✅; old device signed out before reset.
