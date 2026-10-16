# Monitoring

Prometheus alert rules, Grafana dashboard exports, and domain lists for certificate monitoring.

## Contents

| File/Folder | Purpose |
|-------------|---------|
| `domains.txt` | Domains monitored by `cert-check` skill |

Create `alert-rules/` (Prometheus alerting rules, YAML) and `dashboards/` (Grafana dashboard
JSON exports) here as you add them — they are not shipped with the space.

## Adding a Domain to Certificate Monitoring

Add the domain (one per line) to `domains.txt`. It will be checked automatically by the
`weekly-reliability-review` workflow and on any manual `cert-check` run.

## Adding an Alert Rule

1. Create a Prometheus rule file in `alert-rules/`
2. Each rule must include a `runbook_url` annotation pointing to the relevant runbook
3. Set `for: 5m` minimum to prevent flapping

## Agent Assistance

```
@site-reliability alert-rule --metric <metric_name> --threshold <value> --window 5m
```
