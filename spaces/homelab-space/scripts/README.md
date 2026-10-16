# Scripts

Standalone automation scripts for homelab maintenance. The space ships none yet — the
capabilities live in `.navig/skills/`. Put your own helper scripts here.

## Naming Convention

`<verb>-<noun>.<ext>` — e.g. `scan-network.sh`, `backup-configs.ps1`, `check-disk.py`

## Script Header Template

```bash
#!/usr/bin/env bash
# PURPOSE:       <one-line description>
# USAGE:         ./<script-name> [args]
# PREREQUISITES: <tools required, e.g. nmap, ssh>
# REQUIRES:      <elevated | none>
```

## Rules

- Anything that changes system state (registry, PATH, services, files outside the space)
  must support a dry-run mode and check for elevation explicitly before acting.
- Never hard-code machine-specific paths — read them from `.navig/config.yaml` or
  environment variables.
