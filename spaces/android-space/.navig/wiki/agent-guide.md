# Agent Guide — android space

> Who they are, what they own, how to invoke them.
> This guide is the authoritative reference for all agents in the `android` space.

---

## Overview

The `android` space runs six specialized agents, each owning a distinct operational domain.
They collaborate through formations and communicate via inbox channels.

| Agent | Role | Formation | Inbox Channel |
|-------|------|-----------|----------------|
| **pixel** | Device cartographer / fleet inventory | `fleet-patrol` | `#fleet` |
| **bridge** | ADB bridge operator | `device-bridge` | `#bridge` |
| **installer** | App & APK operator | `app-ops` | `#apps` |
| **scrub** | Privacy & debloat warden | `privacy-hardening` | `#privacy` |
| **mirror** | Screen & control operator | `device-bridge` | `#control` |
| **keeper** | Backup & restore archivist | `backup-restore` | `#backup` |

---

## pixel — Device Cartographer

**Role**: Maintains the living inventory of every device — model, Android version, serial,
battery, storage. Pixel knows what's in the fleet, what's online, and what's drifting
behind on security patches.

**Assigned formation**: `fleet-patrol`

**Triggers**:
- New device serial detected
- Device missing from `adb devices`
- Battery/storage crosses a threshold
- Fleet inventory requested

**Capabilities**:
- Run `device-inventory` and `battery-report` across the fleet
- Update `devices.md` and `device-registry.json`
- Track Android-version / security-patch drift

**Inbox channel**: `#fleet`

**Example invocations**:
```
# Inventory every connected device and update the registry
navig agent run pixel --task "Inventory all connected devices and update the registry"

# Show battery + storage health for one device
navig agent run pixel --task "Battery and storage report for serial 3A091FD"
```

---

## bridge — ADB Bridge Operator

**Role**: Owns the connection layer — USB and wireless debugging, pairing, tcpip
transport, and routing shell commands to the right serial. When a device needs to be
reached, bridge opens and holds the channel.

**Assigned formation**: `device-bridge`

**Triggers**:
- Connection requested
- Device shows `unauthorized` / `offline`
- Wireless pairing requested

**Capabilities**:
- Run `adb-connect` and `wireless-debug`
- Switch a USB device to tcpip; recover the adb daemon
- Route `adb -s <serial>` for multi-device setups

**Inbox channel**: `#bridge`

**Example invocations**:
```
# Connect over USB
navig agent run bridge --task "Connect to the plugged-in device"

# Diagnose a device that won't authorize
navig agent run bridge --task "Diagnose the ADB connection"
```

---

## installer — App & APK Operator

**Role**: Owns the software lifecycle — install, uninstall, sideload, split-APK bundles,
APK extraction, and runtime permission grants.

**Assigned formation**: `app-ops`

**Triggers**:
- App install / uninstall / sideload requested
- APK extraction requested
- Permission grant/revoke requested

**Capabilities**:
- Run `apk-install` and `apk-extract`
- `adb install -r -g`, `install-multiple` for splits
- Grant / revoke runtime permissions

**Inbox channel**: `#apps`

**Example invocations**:
```
# Sideload an APK
navig agent run installer --task "Install ~/Downloads/app-release.apk"

# Extract an installed app's APK
navig agent run installer --task "Extract com.example.app to disk"
```

---

## scrub — Privacy & Debloat Warden

**Role**: Strips devices to what the operator actually uses — reversible bloatware
removal and dangerous-permission audits, without breaking the phone.

**Assigned formation**: `privacy-hardening`

**Triggers**:
- Debloat sweep requested
- Permission audit requested
- Over-privileged app detected

**Capabilities**:
- Run `app-debloat` against the safe catalog (`pm disable-user --user 0`)
- Run `permission-audit` — apps holding CAMERA / MIC / LOCATION / SMS
- Restore anything it disabled

**Inbox channel**: `#privacy`

**Example invocations**:
```
# Build a debloat plan
navig agent run scrub --task "Build a reversible debloat plan"

# Which apps can use the microphone?
navig agent run scrub --task "Audit microphone permission across all apps"
```

---

## mirror — Screen & Control Operator

**Role**: Projects any device's display to the desktop and drives it — scrcpy mirroring,
input injection, screenshots, and screen recording.

**Assigned formation**: `device-bridge`

**Triggers**:
- Mirroring / control requested
- Screenshot or recording requested
- Headless input automation requested

**Capabilities**:
- Run `screen-mirror` (scrcpy) with tuned bitrate/size/fps
- Inject `adb shell input` (tap, swipe, text, keyevent)
- Capture screenshots (`screencap`) and recordings (`screenrecord`)

**Inbox channel**: `#control`

**Example invocations**:
```
# Mirror the connected device
navig agent run mirror --task "Mirror the device at 1024px"

# Take a screenshot and pull it
navig agent run mirror --task "Screenshot the current screen"
```

---

## keeper — Backup & Restore Archivist

**Role**: Ensures nothing on a device is ever lost — media pulls, adb backups, integrity
verification, and phone-to-phone migration.

**Assigned formation**: `backup-restore`

**Triggers**:
- Nightly backup schedule
- Backup / restore requested
- New-phone migration requested

**Capabilities**:
- Run `app-backup` and `file-transfer` (media preset)
- Verify backup integrity; restore `.ab` archives
- Drive migration to a new phone

**Inbox channel**: `#backup`

**Example invocations**:
```
# Pull all media from the device
navig agent run keeper --task "Back up all photos and videos"

# Plan a migration to a new phone
navig agent run keeper --task "Plan a migration to a new phone"
```
