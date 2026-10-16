# Postmortem Template

## Purpose
Generate a blameless postmortem document for a resolved incident.
Used by the Incident Commander agent after incident closure.

## Variables
- `{{INCIDENT_ID}}` — e.g. `INC-042`
- `{{TITLE}}` — brief incident description
- `{{DATE}}` — incident date YYYY-MM-DD
- `{{SEVERITY}}` — `critical`, `high`, `medium`, `low`
- `{{AFFECTED_SERVICES}}` — comma-separated services
- `{{DURATION}}` — total incident duration (e.g. `47 minutes`)
- `{{TIMELINE}}` — path to incident timeline file, or inline events

## Prompt

You are writing a blameless postmortem. No individual blame — focus on systems and processes.

Incident: {{INCIDENT_ID}} — {{TITLE}}
Date: {{DATE}}
Severity: {{SEVERITY}}
Affected services: {{AFFECTED_SERVICES}}
Duration: {{DURATION}}
Timeline: {{TIMELINE}}

Produce a postmortem in this structure:

---
# Postmortem: {{INCIDENT_ID}} — {{TITLE}}

**Date:** {{DATE}} | **Severity:** {{SEVERITY}} | **Duration:** {{DURATION}}
**Affected:** {{AFFECTED_SERVICES}}
**Authors:** [names]
**Status:** Draft / Final

---

## Summary
[2–3 sentences: what happened, impact, and how it was resolved]

## Impact
- **Users affected:**
- **Revenue impact:**
- **SLO burn:**

## Timeline

| Time | Event |
|------|-------|

## Root Cause
[The deepest cause in the chain. Start with "The root cause was..." — never a person's name]

## Contributing Factors
1.
2.
3.

## What Went Well
-
-

## What Went Poorly
-
-

## Action Items

| ID | Action | Owner | Due | Status |
|----|--------|-------|-----|--------|

---
*This postmortem is blameless. It identifies system and process failures, not individual failures.*
