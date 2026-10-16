# Migrate to New Phone

## Purpose
Drive a full phone-to-phone migration: inventory the old device, back up its data,
reinstall apps on the new device, restore data and media, and verify parity — with a
checklist so nothing is missed.

## Variables
- `{{OLD_SERIAL}}` — Source (old) device serial
- `{{NEW_SERIAL}}` — Target (new) device serial
- `{{KEEP_OLD}}` — `true` / `false` — whether the old phone stays as a backup

## Prompt

You are NAVIG Keeper migrating from `{{OLD_SERIAL}}` (old) to `{{NEW_SERIAL}}` (new).

Both devices should be connected. Work through the phases in order and confirm each.

### Phase 1 — Snapshot the Old Device
1. `device-inventory --serial {{OLD_SERIAL}}` — record model, Android version, app list.
2. `permission-audit --serial {{OLD_SERIAL}}` — capture the permission posture to reproduce.
3. List installed third-party apps (`pm list packages -3`) — this is the migration set.

### Phase 2 — Back Up
1. `file-transfer --direction media --serial {{OLD_SERIAL}}` — pull all media to the media pull dir (`devices/media`).
2. `apk-extract` each sideloaded (non-store) app to the APK dir (`devices/apks`).
3. `app-backup` for any app that supports it (and its data matters).

### Phase 3 — Prepare the New Device
1. `adb-connect` / `device-inventory --serial {{NEW_SERIAL}}` — confirm it's authorized.
2. Note the new device's Android version — flag any app that won't run on it.

### Phase 4 — Restore
1. Reinstall store apps via their store account (note which — you won't sideload these).
2. `apk-install` each sideloaded APK from the APK dir (`devices/apks`) onto `{{NEW_SERIAL}}`.
3. Push media back with `file-transfer --direction push` (or leave in cloud/computer).
4. `app-backup --action restore` for any archived app data.

### Phase 5 — Verify Parity
Produce a table comparing old vs. new:

| Check | Old | New | OK? |
|---|---|---|---|
| Third-party app count | N | N | ✅/❌ |
| Media file count | N | N | ✅/❌ |
| Key apps launch | — | — | ✅/❌ |

### Phase 6 — Handoff
If `{{KEEP_OLD}}` is `false`, remind the user to sign out of accounts and factory-reset
the old device **after** parity is confirmed — never before.

### Checklist
- [ ] Old device fully inventoried
- [ ] All media pulled and verified
- [ ] All sideloaded APKs extracted
- [ ] New device authorized
- [ ] Apps reinstalled and launch
- [ ] Media restored / accessible
- [ ] Parity confirmed
- [ ] Old device signed out (if not kept)
