# NAVIG Homelab Space

> **Command-and-control hub for all your hardware, devices, and networks.**
> Fork it, customize it, run it. Zero manual setup.

---

## Overview

The **homelab** space is a complete NAVIG infrastructure management environment
designed for operators who run multiple machines — desktops, laptops, servers, NAS
units, and network gear — across Windows, Linux, and macOS. It ships with everything
wired up: skills, agents, formations, automated workflows, a prompt library, wiki
starter kit, and operational memory files.

This is a **community reference space** — the canonical example of how a serious
personal infrastructure NAVIG space is structured. Fork it, fill in your device
registry, and you are operational in under 10 minutes.

---

## Architecture

```
homelab-space/
├── .navig/
│   ├── config.yaml           — space configuration
│   ├── context.md            — space narrative context
│   ├── skills/               — 11 cross-platform skills
│   ├── store/
│   │   ├── agents/           — 6 specialized agents
│   │   ├── formations/       — 5 operational formations
│   │   ├── prompts/          — 8 production-ready prompts
│   │   ├── workflows/        — 6 workflow playbooks
│   │   └── mcp/              — MCP server configuration (workstation.mcp.json)
│   ├── wiki/                 — 6 starter wiki entries
│   ├── memory/               — 4 example memory files (*.example.json)
│   └── inbox/                — inbox routing rules (routes.example.yaml)
├── tools/smartctl/           — smartmontools tool pack
├── tests/                    — skill smoke tests
├── space.manifest.json       — NAVIG Store manifest
├── README.md                 — this file
├── PREVIEW.md                — store listing card
├── CHANGELOG.md              — version history
└── LICENSE                   — MIT
```

### Network Layout (default)

```
Internet
    │
[Router/Gateway]  192.168.1.1
    │
[LAN Subnet]  192.168.1.0/24
    ├── primary-desktop    192.168.1.10   Windows 11
    ├── linux-server       192.168.1.20   Ubuntu 24.04
    └── [your devices]     192.168.1.x    (register via onboard-device workflow)
```

---

## Skills

| Skill | Description | Platforms |
|-------|-------------|-----------|
| `network-scan` | Discover all devices on LAN using nmap / arp | All |
| `port-audit` | Audit open ports on any target host | All |
| `cable-trace` | Interactive physical cable documentation wizard | All |
| `hardware-inventory` | Enumerate CPU, GPU, RAM, storage | All |
| `gpu-health` | GPU temps, VRAM, driver health (NVIDIA + AMD) | All |
| `disk-clean` | Safe disk cleanup with dry-run mode | All |
| `process-investigate` | Find suspicious or resource-heavy processes | All |
| `ssh-connect` | Rapid SSH into any registered device | All |
| `wake-on-lan` | Send WOL magic packet by MAC address | All |
| `sync-configs` | Rsync dotfiles and configs across machines | All |
| `disk-health` | Physical disk & volume health, optional S.M.A.R.T. via smartctl | All |

---

## Formations

| Formation | Agents | Purpose |
|-----------|--------|---------|
| `network-ops` | atlas | Network scanning, topology, cable documentation |
| `hardware-patrol` | pulse | GPU, CPU, thermal, disk health monitoring |
| `cross-platform-ops` | herald | OS-aware command routing and translation |
| `security-watch` | sentinel | Port audits, process anomalies, security reporting |
| `maintenance-crew` | wrench, archivist | Disk clean, log rotation, config sync, wiki updates |

---

## Agent Roster

| Agent | Role | Formation | Inbox |
|-------|------|-----------|-------|
| **atlas** | Infrastructure cartographer | network-ops | `#network` |
| **sentinel** | Security & anomaly watcher | security-watch | `#security` |
| **wrench** | Maintenance automator | maintenance-crew | `#maintenance` |
| **herald** | Cross-platform command translator | cross-platform-ops | `#cross-platform` |
| **archivist** | Config & knowledge keeper | maintenance-crew | `#configs` |
| **pulse** | Hardware health monitor | hardware-patrol | `#hardware` |

---

## Prompt Library

| Prompt | Purpose |
|--------|---------|
| `diagnose-host` | Deep host diagnosis — resources, services, anomalies |
| `explain-network-topology` | Narrate the current network map clearly |
| `security-brief` | Human-readable security situation report |
| `hardware-report` | Structured hardware health summary |
| `onboard-device` | Guided new device registration |
| `cable-map-wizard` | Step-by-step cable documentation elicitation |
| `incident-response` | Structured incident triage and resolution |
| `weekly-ops-review` | Weekly infrastructure review with checklist |

---

## Workflows

| Workflow | Schedule | Description |
|----------|----------|-------------|
| `morning-sweep` | Daily 06:00 | Network scan → hardware health → disk report → anomaly alert |
| `deep-audit` | On-demand | Full port audit + process investigation + GPU + disk clean (dry run) |
| `onboard-device` | On-demand | Interactive new device registration flow |
| `cable-map-update` | On-demand | Guided cable documentation session |
| `nightly-sync` | Nightly 01:00 | Sync configs and logs to backup location |
| `weekly-review` | Weekly Mon 08:00 | Agent reports → wiki entry |

---

## Quickstart Guide

### 1. Install NAVIG

See [navig.run/install](https://navig.run/install).

### 2. Install the space

```
navig space install github:navig-run/registry/spaces/homelab-space
navig space use homelab-space
```

Or clone [github.com/navig-run/registry](https://github.com/navig-run/registry) and copy
`spaces/homelab-space/` wherever you keep your spaces.

### 3. Seed and customize for your environment

The space ships example state only. Copy each example to its live name, then edit it:

```
.navig/memory/space-context.example.json   → space-context.json   (subnet, gateway, DNS)
.navig/memory/device-registry.example.json → device-registry.json (replace the two example devices)
.navig/memory/known-issues.example.json    → known-issues.json
.navig/memory/goals.example.json           → goals.json
.navig/inbox/routes.example.yaml           → routes.yaml
```

Then set your SSH user and network defaults in `.navig/config.yaml`.

### 4. Run your first scan

```
navig skill run network-scan --target 192.168.1.0/24
```

### 5. Onboard your first device and start the morning sweep

Workflows in `.navig/store/workflows/` are playbooks the space's agents follow:

```
navig ask "run the onboard-device workflow"
navig ask "run the morning-sweep workflow"
```

---

## Sharing

The `.gitignore` in this space excludes:
- Secrets and vault data
- Local log files
- Your live memory files and inbox routes (only the `*.example.*` seeds are committed)
- MCP audit logs

Everything else (skills, agents, formations, workflows, prompts, wiki structure,
example memory) is safe to commit and share.

---

## Requirements

| Tool | Required | Purpose |
|------|----------|---------|
| NAVIG | ✅ Required | Core runtime |
| nmap | Optional | `network-scan` (falls back to arp) |
| nvidia-smi | Optional | `gpu-health` NVIDIA mode |
| smartctl | Optional | Disk S.M.A.R.T. monitoring |
| rsync | Optional | `sync-configs` (falls back to robocopy on Windows) |
| wakeonlan / wol | Optional | `wake-on-lan` (Python fallback included) |

---

## Contributing

This is a community reference space. Improvements, additional skills, and agent
enhancements are welcome — open a pull request at
[github.com/navig-run/registry](https://github.com/navig-run/registry).

---

## License

MIT — see [LICENSE](LICENSE)
