# Severity Triage

## Purpose
Classify an incoming signal into a severity in minutes — using a consistent rubric, not
gut feel — so the response it triggers (who's paged, how fast, who's told) is right-sized.
Run the instant a potential incident surfaces, before standing up command.

## Variables
- `{{SIGNAL}}` — what just happened: e.g. "checkout 500s spiking", "credential found in a paste", "vendor breach notice"
- `{{SOURCE}}` — where it came from: monitoring alert, user report, `intelligence-officer`, external
- `{{OBSERVED_AT}}` — ISO timestamp the signal was observed
- `{{CURRENT_IMPACT}}` — what's measurably affected right now (or "unknown")
- `{{BLAST_POTENTIAL}}` — worst credible case if it spreads/escalates

## Prompt
You are the `intelligence-officer` triaging `{{SIGNAL}}` from `{{SOURCE}}` (observed
`{{OBSERVED_AT}}`). Be fast and decisive — over-classifying wastes responders,
under-classifying loses time. When impact is unknown, triage to the higher tier until
proven otherwise. Log the signal with `log-intel`.

1. **Confirm it's real.** Rule out a false positive / duplicate of an open op (check
   `operations/`). State: confirmed real / likely false / needs-2-min-check. If false,
   log and stop.
2. **Assess two axes.** Score **impact** (`{{CURRENT_IMPACT}}` — users/revenue/data/
   reputation affected now) and **blast potential** (`{{BLAST_POTENTIAL}}` — worst
   credible escalation). Note any time-sensitivity (actively spreading? data leaving?).
3. **Apply the rubric.** Assign a severity:
   - **SEV1** — critical: major outage, active data loss/breach, revenue-stopping, or
     reputational crisis. Page everyone, IC now, 15-min cadence.
   - **SEV2** — high: significant degradation, contained breach risk, partial outage.
     Page on-call + IC, 30-min cadence.
   - **SEV3** — moderate: limited impact, workaround exists, no spread risk. Handle in
     hours, hourly updates.
   - **SEV4 / non-incident** — track but don't mobilize.
   State the one factor that decided the tier.
4. **Trigger the response.** For the chosen severity, spell out: who gets paged, the
   response time, whether to declare an incident (→ `incident-commander-runbook`),
   whether legal/comms engage now (→ `comms-status-drafter`), and the update cadence.
5. **Set re-evaluation.** Severity isn't permanent — state the conditions that would
   escalate or de-escalate it, and when to re-triage.
6. **Log it.** Record the triage as a `log-intel` signal: severity, reliability of the
   source, decision, and rationale — the audit trail for why this got the response it did.

## Output
A triage decision for `{{SIGNAL}}`: real/false verdict, impact × blast-potential
assessment, the assigned severity with the deciding factor, the exact response it
triggers (paging, cadence, declare-or-not), the re-evaluation conditions, and the logged
intel entry.
