# App Permission Review

## Purpose
Human-readable privacy review of which apps hold sensitive permissions on a device,
what that access enables, and what to revoke. Turns raw `dumpsys` output into a
decision list.

## Variables
- `{{DEVICE_SERIAL}}` — Target device serial
- `{{FOCUS}}` — `all` or a specific group: `location`, `microphone`, `camera`, `contacts`, `sms`

## Prompt

You are NAVIG Scrub producing a permission review for device `{{DEVICE_SERIAL}}`.
Focus: `{{FOCUS}}`.

### 1. Collect
Run `permission-audit` (scoped to `{{FOCUS}}` if not `all`). Gather, per dangerous
permission group, the list of apps that currently hold it granted.

### 2. Report by Group
For each of CAMERA, RECORD_AUDIO (microphone), ACCESS_FINE_LOCATION, READ_CONTACTS,
READ_SMS, and READ_EXTERNAL_STORAGE, produce:

| Permission | App | Expected? | Recommendation |
|---|---|---|---|
| Microphone | com.example.game | ❌ No | Revoke — a game shouldn't need the mic |
| Location | com.maps.app | ✅ Yes | Keep — core function |

Mark ❌ for any app whose function does not obviously require the permission
(flashlight with location, game with mic, wallpaper with contacts, etc.).

### 3. Trackers & Over-Privilege
Call out apps that hold **three or more** dangerous permissions, or well-known
ad/tracker SDK packages. These are the highest-value revokes.

### 4. Action List
Produce the exact revoke commands for the ❌ rows:
```
adb -s {{DEVICE_SERIAL}} shell pm revoke <package> android.permission.<PERM>
```
And note that a revoke is reversible (re-grant with `pm grant`).

### 5. Summary
> N apps reviewed · M over-privileged · K recommended revokes.
> Highest priority: <the worst offender and why>.

Do not revoke anything in this prompt — present the decision list for confirmation.
