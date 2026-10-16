# On-Call Handoff

## Purpose
Transfer the watch cleanly at shift change so nothing falls through the cracks — active
incidents, fragile systems, watch items, and what's most likely to page next. Run at the
end of every on-call shift, and especially mid-incident when the IC chair changes hands.

## Variables
- `{{OUTGOING}}` — who/which agent is handing off
- `{{INCOMING}}` — who/which agent is taking the watch
- `{{SHIFT_WINDOW}}` — the shift being closed (e.g. "2026-06-20 08:00–20:00 CET")
- `{{ACTIVE_OPS}}` — current open operations (IDs/titles), or "none"
- `{{WATCH_ITEMS}}` — things being monitored that aren't yet incidents
- `{{HANDOFF_TIME}}` — ISO timestamp of the handoff

## Prompt
You are the `strategist` producing the on-call handoff from `{{OUTGOING}}` to
`{{INCOMING}}` at `{{HANDOFF_TIME}}`, closing shift `{{SHIFT_WINDOW}}`. The incoming
watch must be able to take a page in the next minute and know exactly where things stand.
Read the open operations in `operations/` and recent `log-intel` signals in
`intelligence/`.

1. **State of the world.** One-line status: 🟢 quiet / 🟡 watching / 🔴 active incident.
   Then the headline the incoming watch needs in the first 30 seconds.
2. **Active incidents.** For each op in `{{ACTIVE_OPS}}`: current status (from the
   pipeline), severity, what's been done, what's in flight, who else is engaged, the next
   scheduled update, and the single next action `{{INCOMING}}` should take. If `{{INCOMING}}`
   becomes IC, point to the `incident-commander-runbook` record to continue.
3. **Watch items.** For each of `{{WATCH_ITEMS}}`: what you're watching, the threshold
   that turns it into an incident, where to look, and what to do if it trips. These are
   the "didn't page yet but might" items.
4. **Recent intel.** Summarize new signals logged this shift (`log-intel`) — adversary
   activity, near-misses, vendor advisories — with reliability, so the incoming watch
   isn't surprised by context.
5. **Fragile / known-risk areas.** Systems running degraded, deferred maintenance, or a
   change that just shipped and is still "watch closely." Note any change-freeze or
   maintenance window in `{{SHIFT_WINDOW+1}}`.
6. **Logistics.** Escalation contacts, where the runbooks live (`arsenal/`), any access/
   credential the incoming watch needs, and pending callbacks (vendors, legal).
7. **Acknowledge.** End with an explicit handoff line for `{{INCOMING}}` to confirm
   receipt, and log the handoff so the chain of custody is recorded.

## Output
A handoff brief from `{{OUTGOING}}` to `{{INCOMING}}`: world-state line, active-incident
cards with the next action each, watch items with trip thresholds, recent-intel summary,
fragile-areas list, logistics, and an acknowledgment line. Save to `operations/` as the
shift handoff record for `{{SHIFT_WINDOW}}`.
