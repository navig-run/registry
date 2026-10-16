# SKILL_STANDARD — Authoring Guide

> Complete reference for writing skills that work across all NAVIG environments.
> Follow this guide and your skill will pass review on first submission.

---

## Anatomy of a skill file

```yaml
# skill-library/network/my-skill.yaml

# ── Identity (required) ──────────────────────────────────────────────────────
name: Network Scanner
description: Discover devices and open ports on your local network
version: 1.0.0
category: network           # see categories table below
license: MIT
author: your-github-handle  # optional

# ── Invocation (required) ────────────────────────────────────────────────────
user_invocable: true        # true = appears in `navig skill list`
risk_level: safe            # safe | elevated | destructive

# ── Commands (at least one required) ─────────────────────────────────────────
commands:
  - name: scan
    syntax: navig skill run network-scanner scan [--subnet <cidr>] [--json]
    description: Discover all devices on the given subnet (default: auto-detect)
    risk: safe

  - name: portscan
    syntax: navig skill run network-scanner portscan --host <ip> [--ports <range>]
    description: Scan open ports on a specific host
    risk: elevated

  - name: reset
    syntax: navig skill run network-scanner reset
    description: Delete all cached scan results
    risk: destructive
    confirmation: "This deletes all cached scan data. Continue?"  # required for destructive

# ── Examples (at least one required) ─────────────────────────────────────────
# Phrase `user:` as a natural language question an operator would ask
examples:
  - title: Find all devices on my network
    user: What devices are on my LAN?
    command: navig skill run network-scanner scan

  - title: Scan a specific subnet
    user: Scan 10.0.0.0/24 for me
    command: navig skill run network-scanner scan --subnet 10.0.0.0/24

  - title: Check open ports on a host
    user: What ports are open on 192.168.1.1?
    command: navig skill run network-scanner portscan --host 192.168.1.1

# ── Agent hints (required for agent-invocable skills) ─────────────────────────
# These fields tell the AI *when* and *how* to use this skill
agent_hints:
  when_to_use: >
    Use when the user asks about network discovery, device status, unknown hosts,
    port availability, or LAN mapping. Trigger on phrases like "what's on my network",
    "scan my subnet", "is port X open", "find devices".
  output_format: >
    JSON object: { devices: [{ip, mac, hostname, open_ports: []}], scan_time, subnet }
  follow_up: >
    After a scan, offer to run portscan on any suspicious or unnamed device.
    If many ports are open on a device, offer to run security-audit.

# ── Platform compatibility (optional) ────────────────────────────────────────
platforms:
  - linux
  - mac
  - windows

# ── Dependencies (optional) ──────────────────────────────────────────────────
# System tools that must be installed (shown to user if missing)
requires:
  - nmap

# ── Vault keys (optional) ────────────────────────────────────────────────────
# Declare keys the operator must configure via `navig vault set`
# Use {{vault.key_name}} anywhere in commands or entrypoint
# vault_keys:
#   - name: network_password
#     description: Password for protected network segments
#     required: false

# ── Entrypoint (optional) ─────────────────────────────────────────────────────
# Only needed if the skill has a runnable Python/script entrypoint
# entrypoint: main.py
```

---

## Categories

| Category | Use for |
|----------|---------|
| `network` | Network scanning, monitoring, diagnostics |
| `system` | System health, performance, OS management |
| `cloud` | AWS, GCP, Azure, DigitalOcean operations |
| `docker` | Container management and health |
| `database` | DB operations, backups, queries |
| `security` | Audits, vulnerability checks, secrets scanning |
| `developer` | Git, CI/CD, code tools |
| `media` | File conversion, image processing |
| `ai` | LLM utilities, prompt tools |
| `homelab` | Self-hosted services, Proxmox, NAS |
| `productivity` | Email, calendar, notes, task management |
| `custom` | Anything else |

---

## Risk levels

| Level | Meaning | Requirement |
|-------|---------|-------------|
| `safe` | Read-only, no side effects | None |
| `elevated` | Writes files, network calls | Document what is modified in `description:` |
| `destructive` | Deletes data, reformats, sends money | `confirmation:` field is **required** |

---

## Vault placeholders

Never hardcode credentials. Use `{{vault.key_name}}` in any field:

```yaml
commands:
  - name: connect
    syntax: ssh {{vault.homelab_user}}@{{vault.homelab_host}} "ls -la"
    description: SSH into the homelab gateway

vault_keys:
  - name: homelab_user
    description: SSH username for the homelab gateway host
  - name: homelab_host
    description: IP or hostname of the gateway
```

Operator configures once:
```bash
navig vault set homelab_user ubuntu
navig vault set homelab_host 192.168.1.1
```

---

## Agent hints — writing them well

`agent_hints` is the most important section for AI usability.
A well-written `when_to_use` means the model calls your skill automatically.

```yaml
agent_hints:
  # ✅ Good — specific, lists trigger phrases
  when_to_use: >
    Use when the user asks about disk usage, free space, large files,
    or says things like "my disk is full", "clean up space", "what's taking space".

  # ❌ Too vague — won't trigger reliably
  when_to_use: Use for disk things.

  # Always describe exact shape of the output
  output_format: >
    JSON: { total_gb, used_gb, free_gb, percent_used, top_dirs: [{path, size_gb}] }

  # What should the agent suggest next?
  follow_up: >
    If percent_used > 85, offer to identify and clean large temporary files.
    If a single directory dominates, offer to compress or archive it.
```

---

## Skill file template

```bash
cp skill-library/_template.yaml skill-library/<category>/my-skill.yaml
```

---

## Validation

```bash
# Validate a single skill
navig skill validate skill-library/network/my-skill.yaml

# Validate the whole library
find skill-library -name '*.yaml' | xargs -I{} navig skill validate {}

# Run the test suite
npm test
```

---

## Checklist before submitting

- [ ] `name` — concise, unique within category
- [ ] `description` — one sentence, starts with a verb
- [ ] `version` — semver (`1.0.0`)
- [ ] `category` — from the table above
- [ ] `license` — MIT preferred
- [ ] `risk_level` — set correctly
- [ ] Destructive commands have `confirmation:` text
- [ ] No hardcoded IPs, passwords, or tokens (use `{{vault.key_name}}`)
- [ ] At least one `examples:` entry with realistic `user:` phrasing
- [ ] `agent_hints.when_to_use` — specific, includes trigger phrases
- [ ] `agent_hints.output_format` — describes the exact output shape
- [ ] `passes navig skill validate`

---

*Questions? Open an issue or start a discussion.*
