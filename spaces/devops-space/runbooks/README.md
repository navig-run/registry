# Runbooks

Human-readable operational runbooks for incident response and routine operations.

## Naming Convention

```
<failure-mode>-runbook.md
```

Examples:
- `high-error-rate-runbook.md`
- `disk-full-runbook.md`
- `database-connection-pool-runbook.md`

## Template

Use `.navig/store/prompts/incident-runbook.md` to generate a new runbook:

```
@incident-commander generate-runbook --type <failure-mode> --service <service>
```

## Index

| File | Incident Type | Service |
|------|--------------|---------|
| _(Add runbooks here as you create them)_ | | |
