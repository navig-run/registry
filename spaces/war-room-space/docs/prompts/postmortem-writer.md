# Postmortem Writer

## Purpose
Turn a closed incident into a blameless, timeline-driven postmortem that finds the
real contributing causes and produces action items someone will actually do. Run within
a few days of closing any SEV1/SEV2 — while memory and logs are fresh.

## Variables
- `{{INCIDENT_TITLE}}` — the incident being reviewed
- `{{OP_RECORD}}` — where the live record lives (e.g. `operations/<op-id>.md` from the IC runbook)
- `{{SEVERITY}}` — SEV1 / SEV2 / SEV3
- `{{IMPACT_SUMMARY}}` — measured impact: duration, users/revenue/data affected
- `{{TIMEZONE}}` — for normalizing timestamps in the timeline
- `{{REVIEW_DATE}}` — today's ISO date (e.g. `2026-06-20`)

## Prompt
You are the `strategist` writing the postmortem for `{{INCIDENT_TITLE}}` (`{{SEVERITY}}`).
Blameless: name systems and gaps, never people-at-fault. Every claim ties to the record.
Read `{{OP_RECORD}}` and the linked `log-intel` signals in `intelligence/` for the
ground truth.

1. **Summary first.** A 4-sentence executive summary: what happened, the impact
   (`{{IMPACT_SUMMARY}}`), the root contributing causes, and the headline prevention.
   A reader should grasp the whole incident from this alone.
2. **Build the timeline.** From `{{OP_RECORD}}`, reconstruct a normalized timeline
   (`{{TIMEZONE}}`): first signal → detection → declaration → key mitigations →
   resolution. For each entry: timestamp, event, who/what acted. Compute the real
   numbers: time-to-detect, time-to-mitigate, time-to-resolve.
3. **Find contributing causes (not "a cause").** Use a 5-whys / contributing-factors
   approach across technical, process, and detection dimensions. Separate the **trigger**
   (what set it off) from the **vulnerabilities** (what let it become an incident).
4. **What went well / what hurt.** Two honest lists: what limited the blast radius or
   sped recovery, and what slowed or worsened it (alerting gaps, missing runbook, unclear
   ownership, bad rollback).
5. **Action items that ship.** A table of concrete, owned, dated improvements:

   | # | Action | Type (prevent/detect/mitigate) | Owner | Due | Priority |
   |---|---|---|---|---|---|

   Each must be specific and verifiable — "add an alert on X latency > Y", not "improve
   monitoring." Stage any reusable artifact into `arsenal/` (a new runbook, a playbook).
6. **Detection & metrics review.** Would current alerting catch this next time, faster?
   State the detection gap and the specific signal to add. Note the SLO/SLA impact.

## Output
A blameless postmortem for `{{INCIDENT_TITLE}}`: executive summary, normalized timeline
with TTD/TTM/TTR metrics, contributing-causes analysis (trigger vs vulnerabilities),
went-well/went-wrong lists, an owned+dated action-item table, and the detection gap to
close. Save under `operations/` and stage any new runbook into `arsenal/`.
