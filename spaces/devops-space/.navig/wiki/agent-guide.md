# Agent Guide — DevOps Space

## Quick Reference

| Agent | Inbox | Formation | Activated by |
|-------|-------|-----------|-------------|
| pipeline-engineer | #pipeline | ci-pipeline | `@pipeline-engineer` or `deploy-check` |
| infra-architect | #infra | infra-deploy | `@infra-architect` |
| site-reliability | #sre / #alerts | sre-ops | `@site-reliability` or `weekly-reliability-review` |
| incident-commander | #incidents / #alerts | incident-response | `@incident-commander` or `incident-triage` |

---

## Pipeline Engineer

```
@pipeline-engineer design --platform github-actions --language python --deploy kubernetes
@pipeline-engineer diagnose --log ci-cd/failure-log.txt
@pipeline-engineer optimise --pipeline ci-cd/my-pipeline.yml
```

---

## Infrastructure Architect

```
@infra-architect design --cloud aws --pattern vpc-3tier --region us-east-1
@infra-architect review --plan infrastructure-as-code/terraform-starter/tfplan.txt
@infra-architect scaffold --tool terraform --env prod --prefix navig-prod
```

Infra Architect **never applies changes** — always escalates to operator for approval.

---

## Site Reliability Engineer

```
@site-reliability slo --service api-gateway --target 99.9 --window 30d
@site-reliability alert-rule --metric http_error_rate --threshold 0.01 --window 5m
@site-reliability review --period weekly --services api-gateway,auth-service
```

---

## Incident Commander

```
# Open a new incident
@incident-commander open --severity high --title "API gateway 5xx spike"

# Update during incident
@incident-commander update --incident INC-042 --status "mitigated, monitoring"

# Write postmortem
@incident-commander postmortem --incident INC-042 --timeline incidents/INC-042-timeline.md
```

Incidents are **never closed** without a resolution statement and follow-up action items.
