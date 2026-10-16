# GENESIS — Android Space

## Why This Exists

Phones are the most personal computers we own — and the hardest to manage at arm's length.
Bloatware ships preinstalled, apps hoard permissions, photos never leave the device, and
every OEM does connectivity slightly differently. Android Space is the command center that
makes a phone (or a whole fleet of them) as manageable as any other machine you run.

Without it: devices drift on security patches, bloatware and trackers pile up, backups are
a manual chore that never happens, and moving to a new phone is a lost weekend.

## What It Does

Android Space manages every layer of the Android device lifecycle:
- **Connectivity** — ADB over USB and wireless debugging (tcpip + Android 11+ pairing)
- **Fleet inventory** — model, Android version, security patch, battery, storage per device
- **App operations** — install, uninstall, sideload, split-APK bundles, APK extraction
- **Privacy hardening** — reversible debloat and dangerous-permission auditing
- **Screen & control** — scrcpy mirroring, input injection, screenshots, recording
- **Data safety** — media pull, adb backup/restore, phone-to-phone migration

## Core Agents

| Agent | Role |
|-------|------|
| `pixel` | Maps and maintains the device fleet inventory |
| `bridge` | ADB connectivity, pairing, wireless debugging |
| `installer` | App and APK install / uninstall / sideload / extract |
| `scrub` | Reversible debloat and privacy hardening |
| `mirror` | Screen mirroring, input injection, capture |
| `keeper` | Backup, restore, and phone migration |

## Primary Formations

- **`device-bridge`** — ADB connectivity, pairing, shell routing, mirroring
- **`app-ops`** — install/uninstall/sideload/extract, permission management
- **`fleet-patrol`** — multi-device inventory and health tracking
- **`privacy-hardening`** — debloat, permission audit, tracker blocking
- **`backup-restore`** — adb backup, media pull, phone migration

## Origin

Built for anyone who manages more than one Android device — power users, testers, and
self-hosters — who want their phones as well-managed, private, and backed-up as the rest
of their infrastructure.

---
*Space ID: `android` · Runtime: `navig-space-2` · Tier: work*
