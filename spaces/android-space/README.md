# NAVIG Android Space

> **Command hub for every Android device you own or manage.**
> Fork it, connect a device, run it. Zero manual setup.

---

## Overview

The **android** space is a complete NAVIG environment for managing Android devices —
phones, tablets, TV boxes, and wearables — from a single desktop, whether you run
Windows, Linux, or macOS. It ships with everything wired up: skills, agents, formations,
automated workflows, a prompt library, wiki starter kit, and operational memory files.

It covers the full device lifecycle: **connect** over ADB (USB or wireless), **inventory**
the fleet, **install / sideload / extract** apps and APKs, **debloat and harden** privacy,
**mirror and control** the screen, and **back up / migrate** data.

This is a **community reference space** — the canonical example of a serious personal
Android management space. Fork it, connect your first device, and you are operational in
under 10 minutes.

---

## Architecture

```
android-space/
├── .navig/
│   ├── config.yaml           — space configuration (adb/scrcpy paths, backup dirs)
│   ├── context.md            — space narrative context
│   ├── store/agents/         — 6 specialized agents
│   ├── store/formations/     — 5 operational formations
│   ├── store/prompts/        — 8 production-ready prompts
│   ├── store/workflows/      — 6 automated workflows
│   ├── store/mcp/            — MCP server configuration
│   ├── skills/               — 12 ADB / scrcpy skills
│   ├── wiki/                 — 7 starter wiki entries
│   ├── memory/               — example memory files (*.example.json)
│   └── inbox/                — inbox routing rules (routes.example.yaml)
├── tools/                    — tool packs (platform-tools, scrcpy)
├── space.manifest.json       — NAVIG Store manifest
├── README.md                 — this file
├── PREVIEW.md                — store listing card
├── CHANGELOG.md              — version history
└── LICENSE                   — MIT
```

### Device Layout (default)

```
Desktop host (Windows / Linux / macOS)
    │  adb + scrcpy
    ├── USB ─────────── phone / tablet (USB debugging)
    └── Wi-Fi (tcpip) ── phone         192.168.1.42:5555
                         [your devices]  (register via new-device-onboard)
```

---

## Skills

| Skill | Description | Platforms |
|-------|-------------|-----------|
| `adb-connect` | Connect over USB or Wi-Fi and authorize the device | All |
| `device-inventory` | Fingerprint model, Android version, patch, battery, storage | All |
| `apk-install` | Sideload APKs / split bundles with reinstall + grant | All |
| `apk-extract` | Pull an installed app's APK(s) off the device | All |
| `app-debloat` | Reversible bloatware removal via `pm disable-user` | All |
| `permission-audit` | Audit apps holding dangerous runtime permissions | All |
| `screen-mirror` | Mirror + control the screen with scrcpy | All |
| `logcat-capture` | Capture, filter, and save device logs | All |
| `battery-report` | Battery level, health, temperature, top consumers | All |
| `file-transfer` | Push/pull files and a media-pull preset | All |
| `wireless-debug` | tcpip and Android 11+ pairing setup | All |
| `app-backup` | adb backup / restore archives | All |

---

## Formations

| Formation | Agents | Purpose |
|-----------|--------|---------|
| `device-bridge` | bridge, mirror, pixel | ADB connect, pair, tcpip, shell routing, mirroring |
| `app-ops` | installer, scrub | Install/uninstall/sideload/extract, permissions |
| `fleet-patrol` | pixel, keeper | Inventory, battery/storage, version drift |
| `privacy-hardening` | scrub, pixel | Debloat, permission audit, tracker blocking |
| `backup-restore` | keeper, installer | adb backup, media pull, phone migration |

---

## Agent Roster

| Agent | Role | Formation | Inbox |
|-------|------|-----------|-------|
| **pixel** | Device cartographer / fleet inventory | fleet-patrol | `#fleet` |
| **bridge** | ADB bridge operator | device-bridge | `#bridge` |
| **installer** | App & APK operator | app-ops | `#apps` |
| **scrub** | Privacy & debloat warden | privacy-hardening | `#privacy` |
| **mirror** | Screen & control operator | device-bridge | `#control` |
| **keeper** | Backup & restore archivist | backup-restore | `#backup` |

---

## Prompt Library

| Prompt | Purpose |
|--------|---------|
| `onboard-device` | Guided new-device registration & hardening |
| `debloat-plan` | Safe, reversible debloat plan for a device |
| `diagnose-adb` | Troubleshoot connection / unauthorized / offline |
| `app-permission-review` | Human-readable privacy review + revoke list |
| `backup-strategy` | Layered backup plan the nightly workflow enacts |
| `migrate-to-new-phone` | Full phone-to-phone migration with parity checks |
| `logcat-triage` | Turn a raw logcat dump into a crash diagnosis |
| `weekly-android-review` | Weekly fleet review with checklist |

---

## Workflows

| Workflow | Schedule | Description |
|----------|----------|-------------|
| `morning-device-check` | Daily 08:00 | Connect → inventory → battery → offline alert |
| `new-device-onboard` | On-demand | Register + harden + baseline-backup a new device |
| `debloat-sweep` | On-demand | Catalog-matched reversible debloat + permission audit |
| `nightly-backup` | Nightly 02:00 | Media pull + app backup + verify |
| `app-update-check` | Weekly Mon 09:00 | Compare installed vs. staged APKs |
| `fleet-audit` | On-demand | Full inventory + patch drift + permission posture |

---

## Quickstart Guide

### 1. Install NAVIG

See [navig.run/install](https://navig.run/install).

### 2. Install the space

```
navig space install github:navig-run/registry/spaces/android-space
navig space use android-space
```

### 3. Install the tooling

```
# Install Android SDK Platform-Tools (adb + fastboot) from developer.android.com.
# Install scrcpy from its official GitHub release.
# Put both on your PATH, or set ANDROID_HOME (adb is looked up in $ANDROID_HOME/platform-tools),
# or set adb_path / scrcpy_path in .navig/config.yaml.
```

### 4. Seed and customize for your environment

The space ships example state only. Copy each example to its live name, then edit it:

```
.navig/memory/device-registry.example.json → device-registry.json (replace the two example devices)
.navig/memory/space-context.example.json   → space-context.json
.navig/memory/known-issues.example.json    → known-issues.json
.navig/memory/goals.example.json           → goals.json
.navig/inbox/routes.example.yaml           → routes.yaml
```

Backup, media and APK folders default to `devices/backups`, `devices/media` and
`devices/apks` under the space root — change `backup_dir`, `media_pull_dir` and `apk_dir`
in `.navig/config.yaml` to put them elsewhere.

### 5. Connect your first device

```
navig skill run adb-connect        # accept the RSA prompt on the device
```

### 6. Onboard it and start the morning check

Workflows in `.navig/store/workflows/` are playbooks the space's agents follow:

```
navig ask "run the new-device-onboard workflow"
navig ask "run the morning-device-check workflow"
```

---

## Sharing

The `.gitignore` in this space excludes:
- Secrets and vault data
- Local log files
- Your live memory files and inbox routes (only the `*.example.*` seeds are committed)
- The `devices/` data folder, APK / `.ab` backup artifacts and MCP audit logs

Everything else (skills, agents, formations, workflows, prompts, wiki structure, example
memory) is safe to commit and share.

---

## Requirements

| Tool | Required | Purpose |
|------|----------|---------|
| NAVIG | ✅ Required | Core runtime |
| platform-tools (adb) | ✅ Required | Every skill runs on `adb` |
| fastboot | Optional | Bootloader/recovery ops (opt-in, high-risk) |
| scrcpy | Optional | `screen-mirror` (falls back to a single screenshot) |
| USB data cable | ✅ Required (once) | First connection / tcpip enablement |

---

## Contributing

This is a community reference space. Improvements, additional skills, and agent
enhancements are welcome — open a pull request at [github.com/navig-run/registry](https://github.com/navig-run/registry).

---

## License

MIT — see [LICENSE](LICENSE)
