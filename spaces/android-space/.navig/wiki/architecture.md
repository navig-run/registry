# Space Architecture

**Space**: `android-space`
**Root**: the folder containing `.navig/` (installed: `~/.navig/spaces/android-space`)
**Last Updated**: 2026-07-10
**Maintained by**: Pixel

---

## Overview

The `android` space is a unified command hub for every Android device the operator owns
or manages — phones, tablets, TV boxes, and wearables. It provides a single namespace for
connecting to devices over ADB (USB or wireless), managing apps and APKs, keeping a live
fleet inventory, debloating and hardening privacy, mirroring and controlling screens, and
backing up / migrating data — all through the NAVIG agent framework.

The space is designed to be cloned, forked, and operated by any NAVIG user managing one
device or a whole fleet.

---

## Core Design Principles

| Principle | Description |
|---|---|
| **Cross-Platform Host** | Skills run from Windows, Linux, or macOS — `adb`/`scrcpy` are the same everywhere |
| **Registry-Driven** | All device knowledge lives in `device-registry.json` — no hardcoded serials in skills |
| **Reversible by Default** | Debloat uses `pm disable-user` (restorable); nothing touches `/system` or requires root |
| **Layered Agents** | Six specialist agents cover the full device surface without overlap |
| **Scheduled Automation** | Morning device check, nightly backup, and weekly app-update run unattended |

---

## Formation Layer

Formations group agents around operational concerns:

```
device-bridge        ← bridge + mirror + pixel (ADB connect, pair, tcpip, shell, mirror)
app-ops              ← installer + scrub       (install/uninstall/sideload/extract, permissions)
fleet-patrol         ← pixel + keeper          (inventory, battery/storage, version drift)
privacy-hardening    ← scrub + pixel           (debloat, permission audit, tracker blocking)
backup-restore       ← keeper + installer      (adb backup, media pull, migration)
```

---

## Agent Layer

| Agent | Domain | Inbox |
|---|---|---|
| `pixel` | Fleet inventory | `#fleet` |
| `bridge` | ADB connectivity | `#bridge` |
| `installer` | Apps & APKs | `#apps` |
| `scrub` | Privacy & debloat | `#privacy` |
| `mirror` | Screen & control | `#control` |
| `keeper` | Backup & restore | `#backup` |

---

## Workflow Layer

| Workflow | Schedule | Purpose |
|---|---|---|
| `morning-device-check` | Daily 8 AM | Connect + inventory + battery + offline alert |
| `nightly-backup` | Daily 2 AM | Media pull + app backup + verify |
| `app-update-check` | Mon 9 AM | Compare installed vs. staged APKs |
| `fleet-audit` | On-demand | Full inventory + patch drift + permission posture |
| `new-device-onboard` | On-demand | Register + harden + baseline-backup a new device |
| `debloat-sweep` | On-demand | Catalog-matched reversible debloat + permission audit |

---

## Directory Structure

```
android-space\
├── .navig\
│   ├── config.yaml              ← Space configuration (adb/scrcpy paths, backup dirs)
│   ├── context.md               ← Space narrative context
│   ├── skills\                  ← Skill definitions (12)
│   ├── store\agents\            ← Agent definitions (6)
│   ├── store\formations\        ← Formation definitions (5)
│   ├── store\workflows\         ← Workflow definitions (6)
│   ├── store\prompts\           ← Reusable prompt library (8)
│   ├── store\mcp\               ← MCP server configuration
│   ├── memory\                  ← Structured memory assets (*.example.json seeds)
│   ├── inbox\                   ← Inbox routing rules (routes.example.yaml seed)
│   └── wiki\                    ← Operational wiki
│       └── history\             ← Archived fleet audits & reviews
├── devices\                     ← Local backups / media / APKs (gitignored, created on use)
├── tools\                       ← Tool packs (platform-tools, scrcpy)
├── space.manifest.json          ← NAVIG Store manifest
├── README.md                    ← Publication-quality readme
├── PREVIEW.md                   ← Store listing card
├── CHANGELOG.md                 ← Version history
├── LICENSE                      ← MIT license
└── .gitignore                   ← Space gitignore
```

---

## Data Flow

```
User Intent / Schedule Trigger
        ↓
   NAVIG Inbox (routes.yaml)
        ↓
   Agent (yaml definition)
        ↓
   Formation (context + peers)
        ↓
   Skill (adb / scrcpy execution)
        ↓
   Output → Memory / Wiki / Report
```

---

## Configuration

Key settings in `.navig/config.yaml`:

```yaml
space: android-space
adb_path: ""                    # empty = PATH, then $ANDROID_HOME/platform-tools
scrcpy_path: ""                 # empty = PATH
default_transport: "tcpip:5555"
backup_dir: "devices/backups"   # relative to the space root, or an absolute path
```

No device credentials live in this file — only paths and defaults.

---

## Getting Started

1. Install the space: `navig space install github:navig-run/registry/spaces/android-space`
2. Install Android SDK Platform-Tools and scrcpy from their official releases (on PATH, or set `ANDROID_HOME`).
3. Copy the `.navig/memory/*.example.json` seeds to their live names; set `adb_path` / `scrcpy_path` only if the tools are not on PATH
4. Onboard your first device: `navig ask "run the new-device-onboard workflow"`
5. Run the morning check: `navig ask "run the morning-device-check workflow"`
6. View the status: `navig space check android-space --no-interactive`
