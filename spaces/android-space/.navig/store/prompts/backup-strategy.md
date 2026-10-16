# Backup Strategy

## Purpose
Design a practical, layered backup strategy for a device (or the whole fleet) —
what to back up, how often, where it lands, and how to verify it. Produces a plan
the `nightly-backup` workflow can enact.

## Variables
- `{{DEVICE_SERIAL}}` — Target device serial (or `all` for the fleet)
- `{{ROOTED}}` — `true` / `false` (affects whether full app-data backup is possible)
- `{{DEST}}` — Backup destination root (default `devices/backups` under the space root)

## Prompt

You are NAVIG Keeper designing a backup strategy for `{{DEVICE_SERIAL}}`
(rooted: `{{ROOTED}}`). Destination: `{{DEST}}`.

### 1. Inventory What Matters
List the data classes on the device and their risk if lost:
- 📷 **Media** — DCIM, Pictures, Movies, Downloads (irreplaceable, high priority)
- 💬 **App data** — chats, notes, game saves (app-dependent)
- ⚙️ **Settings/config** — accounts, launcher layout (nice-to-have)
- 📦 **Sideloaded APKs** — apps not on any store (re-obtainable but tedious)

### 2. Choose Methods per Class
| Data | Method | Command | Notes |
|---|---|---|---|
| Media | `adb pull` | `file-transfer --direction media` | Fast, reliable, always works |
| Sideloaded APKs | `apk-extract` | per package | Keep versioned copies |
| App data | `adb backup` | `app-backup` | Limited on modern Android; many apps opt out |
| Full device | `adb backup -all` | `app-backup` (no package) | Slow; confirm on device |

Note the hard truth: `adb backup` is deprecated and unreliable on Android 12+ —
media pull + APK extraction is the dependable core. Call this out honestly.

### 3. Cadence
- **Nightly**: media pull (incremental) → `nightly-backup` workflow.
- **Weekly**: APK re-extract of sideloaded apps.
- **On-demand**: full `adb backup` before a risky change or migration.

### 4. Verify
Every backup run must verify: file counts and total bytes are non-zero and >= last
run's media size (no silent truncation). Log to `.navig/memory/backup-log.json`.

### 5. Restore Test
Recommend a quarterly restore drill: pick one archive, restore to a spare/test
device, confirm the data is intact. An unverified backup is a hope, not a backup.

### 6. Plan Output
Produce the concrete schedule + commands, and note any gaps (e.g. "chat app X can't
be backed up without root — use its in-app export instead").
