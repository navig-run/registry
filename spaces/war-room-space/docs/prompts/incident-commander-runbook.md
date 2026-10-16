# Incident Commander Runbook

## Purpose
Stand up and drive an active incident from the command chair — assign roles, set a
communication cadence, coordinate the workstreams, and keep one authoritative running
record. Run the moment an incident is declared, and keep it open until handoff or close.

## Variables
- `{{INCIDENT_TITLE}}` — short name: e.g. "Primary API down", "Vendor data-breach exposure"
- `{{SEVERITY}}` — declared severity (from `severity-triage`): SEV1 / SEV2 / SEV3
- `{{DECLARED_AT}}` — ISO timestamp the incident was declared
- `{{IMPACT}}` — who/what is affected and how (users, revenue, data, reputation)
- `{{RESPONDERS}}` — available agents/people and their domains
- `{{OBJECTIVE}}` — the one-line definition of "resolved"

## Prompt
You are the `strategist` acting as Incident Commander for `{{INCIDENT_TITLE}}`
(`{{SEVERITY}}`, declared `{{DECLARED_AT}}`). You own coordination and the record, not
every fix — delegate and track. Open the op with the `build-op` skill and drive it
through the `planning → active → hold → closed` pipeline via `advance-status`.

1. **Establish command.** Create the operation (`build-op`) with BLUF =
   `{{INCIDENT_TITLE}}`, objective `{{OBJECTIVE}}`, theater, and priority from
   `{{SEVERITY}}`. Confirm you are IC and state where the running record lives in
   `operations/`. Set the status to `active`.
2. **Assign roles.** From `{{RESPONDERS}}`, name an Operations lead (drives the fix), a
   Comms lead (route to `comms-status-drafter`), and a Scribe (maintains the timeline).
   For breach/legal exposure, pull `legal-counsel` and stage relevant items via
   `arsenal-search`. State who owns what in one table.
3. **Size the problem.** Restate `{{IMPACT}}`, the current blast radius, and the
   objective. Log the initial picture as an intel signal (`log-intel`) with reliability.
4. **Set the cadence.** Define the update interval (SEV1 ~15min, SEV2 ~30min, SEV3
   hourly), the next-update time, and the channels. State it explicitly so everyone knows
   when the next sync is.
5. **Drive workstreams.** Maintain a live action log: each action has an owner, a
   status (doing/blocked/done), and a timestamp. Track mitigations separately from the
   root-cause hunt — restore service first, diagnose second. Re-log significant findings
   with `log-intel`.
6. **Decide & checkpoint.** At each cadence tick, decide: keep mitigating, escalate
   severity, move to `hold` (waiting on a vendor), or move toward `closed`. Record the
   decision and rationale. Resolve only when `{{OBJECTIVE}}` is met and verified.
7. **Close or hand off.** On resolution, `advance-status` → `closed`, confirm impact has
   ended, schedule the postmortem (`postmortem-writer`), and capture the timeline. If the
   shift ends first, trigger `on-call-handoff` instead.

## Output
A live incident command record in `operations/`: the operation entry, the role
assignment table, impact + objective, the communication cadence, a timestamped action
log, decision checkpoints, and a clean close (or handoff) with the postmortem scheduled.
