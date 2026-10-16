# Runbooks Index

Operational runbooks for common failure modes and routine procedures.

> Runbooks are kept in the top-level [runbooks/](../../runbooks/) folder.
> This page is a copy of the index for doc-browsing convenience.

## Creating a Runbook

Use the prompt template:
```
@incident-commander generate-runbook --type <failure-mode> --service <service>
```

Or manually copy `.navig/store/prompts/incident-runbook.md` and fill in the sections.

## Runbook Standards

Every runbook must include:
- **Severity** — Critical / High / Medium / Low
- **Detection** — how the issue is typically noticed
- **Impact** — who or what is affected
- **Steps** — numbered, command-first
- **Escalation** — when to escalate and to whom
- **Post-incident** — follow-up if applicable
