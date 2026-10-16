# Space Architecture

**Space**: `homelab-space`  
**Root**: the folder containing `.navig/` (installed: `~/.navig/spaces/homelab-space`)  
**Last Updated**: 2026-02-26  
**Maintained by**: Archivist

---

## Overview

The `homelab` space is a unified command-and-control layer for all personal hardware,
computers, network devices, and peripherals. It provides a single namespace for managing
heterogeneous infrastructure — Windows homelabs, Linux servers, macOS laptops, NAS
appliances, Raspberry Pi nodes, network switches, and IoT devices — through the NAVIG
agent framework.

The space is designed to be cloned, forked, and operated by any NAVIG user running a
home lab, developer homelab, or small office infrastructure.

---

## Core Design Principles

| Principle | Description |
|---|---|
| **Cross-Platform First** | Every skill, agent, and workflow handles Windows, Linux, and macOS through the `herald` agent's OS-routing layer |
| **Registry-Driven** | All device knowledge lives in `device-registry.json` — no hardcoded IPs anywhere |
| **Self-Documenting** | Every event writes to memory; every significant change updates the wiki |
| **Layered Agents** | Six specialist agents cover the full operational surface without overlap |
| **Scheduled Automation** | Morning sweep, nightly sync, and weekly review run unattended |

---

## Formation Layer

Formations group agents around operational concerns:

```
network-ops          ← atlas + sentinel (network scanning, topology, cables)
hardware-patrol      ← pulse (GPU, CPU, disk, thermals)
cross-platform-ops   ← herald (OS routing, shell translation)
security-watch       ← sentinel + pulse (port audit, process investigation)
maintenance-crew     ← wrench + archivist (disk clean, log rotation, config sync)
```

---

## Agent Layer

| Agent | Domain | Inbox |
|---|---|---|
| `atlas` | Network cartographer | `#network` |
| `sentinel` | Security monitor | `#security` |
| `pulse` | Hardware health | `#hardware` |
| `herald` | Cross-platform routing | `#cross-platform` |
| `archivist` | Config & knowledge | `#configs` |
| `wrench` | Maintenance automation | `#maintenance` |

---

## Workflow Layer

| Workflow | Schedule | Purpose |
|---|---|---|
| `morning-sweep` | Mon–Fri 7 AM | Network + hardware + anomaly check |
| `nightly-sync` | Daily 1 AM | Config backup + log rotation |
| `weekly-review` | Sunday 9 AM | Full ops review + wiki archive |
| `deep-audit` | Sunday 2 AM (opt-in) | Full port + process + GPU + disk audit |
| `onboard-device` | On-demand | Register new device interactively |
| `cable-map-update` | On-demand | Document physical cable connections |

---

## Directory Structure

```
homelab-space\
├── .navig\
│   ├── config.yaml              ← Space configuration
│   ├── context.md               ← Space narrative context
│   ├── skills\                  ← Skill definitions (11)
│   ├── store\
│   │   ├── agents\              ← Agent definitions (6)
│   │   ├── formations\          ← Formation definitions (5)
│   │   ├── workflows\           ← Workflow definitions (6)
│   │   ├── prompts\             ← Reusable prompt library (8)
│   │   └── mcp\                 ← MCP server configuration
│   ├── memory\                  ← Structured memory assets (*.example.json seeds)
│   ├── inbox\                   ← Inbox routing rules (routes.example.yaml seed)
│   └── wiki\                    ← Operational wiki
│       └── history\             ← Archived ops reviews
├── tools\smartctl\              ← smartmontools tool pack
├── space.manifest.json          ← NAVIG Store manifest
├── README.md                    ← Publication-quality readme
├── PREVIEW.md                   ← Store listing card
├── CHANGELOG.md                 ← Version history
├── LICENSE                      ← MIT license
└── .gitignore                   ← Space gitignore
```

---

## Data Flow

```
User Intent / Schedule Trigger
        ↓
   NAVIG Inbox (routes.yaml)
        ↓
   Agent (yaml definition)
        ↓
   Formation (context + peers)
        ↓
   Skill (cross-platform execution)
        ↓
   Output → Memory / Wiki / Report
```

---

## Configuration

Key settings in `.navig/config.yaml`:

```yaml
space: homelab-space
default_network_range: "192.168.1.0/24"   # UPDATE to your subnet
wol_broadcast: "192.168.1.255"            # UPDATE to your broadcast address
ssh_timeout: 5
smartctl_path: ""                         # empty = resolve smartctl from PATH
```

The backup destination lives in `.navig/memory/space-context.json` (`backup_location` → `path`).

All device-specific credentials are stored in the space vault — never in this file.

---

## Getting Started

1. Install the space: `navig space install github:navig-run/registry/spaces/homelab-space`
2. Copy the `.navig/memory/*.example.json` seeds to their live names; set your subnet in
   `.navig/config.yaml` → `default_network_range`
3. Register your first device: `navig ask "run the onboard-device workflow"`
4. Run the morning sweep: `navig ask "run the morning-sweep workflow"`
5. View the status: `navig space check homelab-space`
