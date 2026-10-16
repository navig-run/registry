---
space: android-space
version: 1.0.0
created: 2026-07-10
---

# Space: android

## Purpose
Command hub for every Android device you own or manage — a single operator surface for
ADB connectivity, app & APK operations, fleet inventory, debloat/privacy hardening,
screen mirroring, and backup/restore. One namespace for every phone and tablet in play.

## Scope
- Devices: phones, tablets, Android TV boxes, wearables (adb-reachable)
- Connectivity: USB debugging, wireless debugging (tcpip / Android 11+ pairing)
- Apps: install, uninstall, sideload, split-APK bundles, permission management
- Privacy: reversible debloat (pm disable-user), dangerous-permission audits
- Control: scrcpy mirroring, input injection, screenshots, screen recording
- Data: media pull, adb backup/restore, phone-to-phone migration
- OEMs: Google, Samsung, Xiaomi, OnePlus, and other Android 10+ devices

## Active Agents
pixel · bridge · installer · scrub · mirror · keeper

## Active Formations
device-bridge · app-ops · fleet-patrol · privacy-hardening · backup-restore

## Key Paths
- Space root:      the folder containing this .navig/ (installed: ~/.navig/spaces/android-space)
- Config:          .navig/config.yaml (adb_path / scrcpy_path empty = resolve from PATH or $ANDROID_HOME)
- Device registry: .navig/memory/device-registry.json (copy from device-registry.example.json)
- Backups / Media / APKs: config keys backup_dir · media_pull_dir · apk_dir (default devices/…)
- Wiki:            .navig/wiki/
