# Changelog — NAVIG Android Space

All notable changes to the `android` space will be documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [1.0.0] — 2026-07-10

### Added

**Skills (12)**
- `adb-connect` — connect over USB or Wi-Fi (tcpip:5555) and authorize the device
- `device-inventory` — fingerprint model, Android version, SDK, security patch, ABI, storage, battery
- `apk-install` — sideload APKs and split bundles with reinstall / grant / downgrade
- `apk-extract` — pull an installed app's APK(s) off the device (handles splits)
- `app-debloat` — reversible bloatware removal via `pm disable-user --user 0` / user-uninstall
- `permission-audit` — audit apps holding dangerous runtime permissions
- `screen-mirror` — scrcpy mirroring + control with screenshot fallback
- `logcat-capture` — capture, filter, and save device logs (dump or stream)
- `battery-report` — battery level, health, temperature, and top consumers
- `file-transfer` — push/pull files plus a media-pull preset (DCIM, Pictures, Download, Movies)
- `wireless-debug` — legacy tcpip and Android 11+ pairing setup
- `app-backup` — adb backup / restore archives (per-app or full device)

**Formations (5)**
- `device-bridge` — ADB connectivity, pairing, tcpip, shell routing, mirroring
- `app-ops` — install/uninstall/sideload/extract, permission management
- `fleet-patrol` — multi-device inventory, battery/storage, Android-version drift
- `privacy-hardening` — debloat, permission audit, tracker blocking
- `backup-restore` — adb backup, media pull, app-data export, phone migration

**Agents (6)**
- `pixel` — device cartographer / fleet inventory (fleet-patrol)
- `bridge` — ADB bridge operator (device-bridge)
- `installer` — app & APK operator (app-ops)
- `scrub` — privacy & debloat warden (privacy-hardening)
- `mirror` — screen & control operator (device-bridge)
- `keeper` — backup & restore archivist (backup-restore)

**Prompts (8)**
- `onboard-device` · `debloat-plan` · `diagnose-adb` · `app-permission-review`
- `backup-strategy` · `migrate-to-new-phone` · `logcat-triage` · `weekly-android-review`

**Workflows (6)**
- `morning-device-check` (daily) · `new-device-onboard` (on-demand) · `debloat-sweep` (on-demand)
- `nightly-backup` (nightly) · `app-update-check` (weekly) · `fleet-audit` (on-demand)

**Wiki (6 entries)**
- `architecture.md` · `devices.md` · `adb-guide.md`
- `debloat-catalog.md` · `runbooks.md` · `agent-guide.md`

**Memory files (4)**
- `space-context.json` · `device-registry.example.json` · `known-issues.json` · `goals.json`

**Tool Packs (2)**
- `tools/platform-tools/pack.yaml` — wraps `adb` + `fastboot` (Android SDK Platform-Tools)
- `tools/scrcpy/pack.yaml` — wraps `scrcpy` for screen mirroring and control

**Scripts (2)**
- `scripts/pair-wireless.ps1` — interactive Android 11+ wireless-debugging pairing helper
- `scripts/batch-debloat.ps1` — catalog-driven batch debloat runner (dry-run by default)

**Infrastructure**
- MCP config: `workstation.mcp.json` with per-agent tool allowlists, blocked/guarded ADB commands, and rate limits
- Inbox routes: `routes.yaml` with 6 channels, escalation rules, and notification settings
- `.gitignore` with sensible defaults for secrets, logs, APKs, and `.ab` backups

**Store assets**
- `space.manifest.json` — NAVIG Store manifest with all required fields
- `README.md` — publication-quality space documentation
- `PREVIEW.md` — store listing card
- `GENESIS.md` — origin and vision
- `CHANGELOG.md` — this file
- `LICENSE` — MIT
- `screenshots/` — screenshot descriptor files

---

## [Unreleased]

*Planned for future versions:*
- `fastboot-ops` skill — bootloader / recovery operations (opt-in, high-risk, gated)
- `app-analyze` skill — static inspection of an extracted APK (manifest, permissions, trackers)
- `notification-mirror` skill — surface device notifications on the desktop
- `dns-block` workflow — per-device tracker/ad DNS blocking (private DNS / hosts)
- `battery-trend` workflow — log battery health over time and surface degradation
- `restore-drill` workflow — automated quarterly backup-restore verification on a spare device
