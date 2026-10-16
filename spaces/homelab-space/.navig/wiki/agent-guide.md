# Agent Guide — homelab space

> Who they are, what they own, how to invoke them.
> This guide is the authoritative reference for all agents in the `homelab` space.

---

## Overview

The `homelab` space runs six specialized agents, each owning a distinct operational domain.
They collaborate through formations and communicate via inbox channels.

| Agent | Role | Formation | Inbox Channel |
|-------|------|-----------|----------------|
| **atlas** | Infrastructure cartographer | `network-ops` | `#network` |
| **sentinel** | Security & anomaly watcher | `security-watch` | `#security` |
| **wrench** | Maintenance automator | `maintenance-crew` | `#maintenance` |
| **herald** | Cross-platform command translator | `cross-platform-ops` | `#cross-platform` |
| **archivist** | Config and knowledge keeper | `maintenance-crew` | `#configs` |
| **pulse** | Hardware health monitor | `hardware-patrol` | `#hardware` |

---

## atlas — Infrastructure Cartographer

**Role**: Maintains the living map of all devices, networks, cables, and physical topology.
Atlas knows every host, every subnet, every cable run. When a device goes missing or
a new device appears, atlas is the first to know and the last to forget.

**Assigned formation**: `network-ops`

**Triggers**:
- New device detected on subnet
- Network scan requested
- Cable documentation session initiated
- Topology change detected (IP/MAC shift)

**Capabilities**:
- Run `network-scan` across any subnet range
- Run `port-audit` on any discovered host
- Run `cable-trace` interactively
- Update `devices.md`, `network-topology.md`, and `device-registry.json`
- Correlate MAC addresses to known hosts

**Inbox channel**: `#network`

**Example invocations**:
```
# Scan the LAN and update the device registry
navig agent run atlas --task "Scan 192.168.1.0/24 and update the device registry"

# Trace cables for the new rack installation
navig agent run atlas --task "Start a cable trace session for the new server rack"

# Explain the current network topology
navig agent run atlas --task "explain network topology"
```

---

## sentinel — Security & Anomaly Watcher

**Role**: Continuous guardian of the space. Monitors open ports, suspicious processes,
unexpected outbound connections, and access log anomalies. Sentinel never sleeps —
it correlates events across all hosts and raises alerts when patterns warrant attention.

**Assigned formation**: `security-watch`

**Triggers**:
- Unknown port opened on any host
- Process with anomalous CPU/network profile detected
- Failed SSH attempt spike
- Unauthorized user login detected
- Manual security brief requested

**Capabilities**:
- Run `port-audit` in full or quick preset on any host
- Run `process-investigate` in anomaly detection mode
- Parse auth logs and firewall logs
- Write to `known-issues.json` with severity tagging
- Generate `security-brief.md` reports
- Escalate critical events to space lead

**Inbox channel**: `#security`

**Example invocations**:
```
# Generate a security situation report
navig agent run sentinel --task "security brief"

# Investigate a suspicious process on a host
navig agent run sentinel --task "Investigate PID 4821 on host homelab-01"

# Full port audit on all registered hosts
navig agent run sentinel --task "Run full port audit across all registered devices"
```

---

## wrench — Maintenance Automator

**Role**: Keeps every machine in the space clean, updated, and running smoothly.
Wrench owns all scheduled maintenance tasks: disk cleanup, log rotation, update
checking, and routine health sweeps. It runs quietly and reports exceptions.

**Assigned formation**: `maintenance-crew`

**Triggers**:
- Scheduled morning sweep (06:00 daily)
- Disk space drops below 15% on any host
- Log directory exceeds size threshold
- Weekly review cycle
- Manual maintenance request

**Capabilities**:
- Run `disk-clean` in dry-run or execute mode
- Check OS update status (Windows: `winget upgrade --list`, Linux: `apt list --upgradable`, macOS: `softwareupdate -l`)
- Rotate logs older than 30 days
- Generate disk space summary reports
- Coordinate with archivist for config backup before risky operations

**Inbox channel**: `#maintenance`

**Example invocations**:
```
# Run disk cleanup dry-run on all hosts
navig agent run wrench --task "Dry-run disk cleanup on all registered hosts and report"

# Check for pending updates across the space
navig agent run wrench --task "Check update status on all Linux machines"

# Run the morning sweep workflow
navig ask "run the morning-sweep workflow"
```

---

## herald — Cross-Platform Command Translator

**Role**: The polyglot of the space. Herald translates high-level tasks into the
correct shell syntax for whatever OS is running on the target host. It knows
the differences between PowerShell, bash, zsh, and CMD — and routes commands correctly
so operators never need to think about the target OS.

**Assigned formation**: `cross-platform-ops`

**Triggers**:
- Command submitted without specifying target OS
- Multi-OS batch operation requested
- Script portability check requested
- Platform-specific error encountered during skill execution

**Capabilities**:
- Detect target OS via NAVIG host registry
- Translate commands: bash ↔ PowerShell ↔ zsh ↔ CMD
- Route `navig run` calls with correct shell flag (`--shell bash|pwsh|zsh|cmd`)
- Identify platform-specific path separators, env var syntax, service managers
- Validate scripts for cross-platform compatibility

**Inbox channel**: `#cross-platform`

**Example invocations**:
```
# Translate a bash command to PowerShell
navig agent run herald --task "Translate this bash one-liner to PowerShell: find /var/log -name '*.log' -mtime +7 -delete"

# Run a task on all hosts regardless of OS
navig agent run herald --task "Check free disk space on all registered hosts"

# Validate a script for cross-platform use
navig agent run herald --task "Review this script and flag any non-portable commands" --attach script.sh
```

---

## archivist — Config & Knowledge Keeper

**Role**: Custodian of all configuration, documentation, and institutional memory in the space.
Archivist syncs dotfiles, updates wiki entries, writes memory files, and ensures
no knowledge is lost when machines change. It is the space's librarian and historian.

**Assigned formation**: `maintenance-crew`

**Triggers**:
- Dotfile change detected on primary host
- New device onboarded (needs config seeded)
- Wiki update requested
- Memory write from another agent
- Weekly review cycle (compiles agent reports)

**Capabilities**:
- Run `sync-configs` between any two hosts
- Write and update all files under `.navig/wiki/`
- Write and update all files under `.navig/memory/`
- Compile weekly review wiki entries
- Maintain `device-registry.json` and `known-issues.json`
- Create space export packages (`.navig-space` bundles)

**Inbox channel**: `#configs`

**Example invocations**:
```
# Sync dotfiles to a new machine
navig agent run archivist --task "Sync my dotfiles from primary-desktop to new-laptop"

# Update the device registry with new host info
navig agent run archivist --task "Add new-nas to the device registry: IP 192.168.1.50, MAC aa:bb:cc:dd:ee:ff, role storage"

# Compile this week's ops report
navig agent run archivist --task "Compile the weekly ops report and write it to the wiki"
```

---

## pulse — Hardware Health Monitor

**Role**: The space's diagnostic eye. Pulse continuously monitors CPU thermals, GPU health,
VRAM usage, disk S.M.A.R.T. status, RAM pressure, and overall hardware vitals across
every registered host. It alerts before hardware fails, not after.

**Assigned formation**: `hardware-patrol`

**Triggers**:
- GPU temperature exceeds threshold (>85°C NVIDIA, >90°C AMD)
- CPU temperature exceeds 90°C
- Disk S.M.A.R.T. status changes to warning or failing
- RAM usage stays above 90% for >10 minutes
- Manual hardware report requested
- Morning sweep cycle

**Capabilities**:
- Run `gpu-health` on any NVIDIA or AMD GPU host
- Run `hardware-inventory` for full system enumeration
- Parse S.M.A.R.T. data via `smartctl` or `wmic diskdrive`
- Monitor thermal sensors (lm-sensors, iStats, HWiNFO)
- Write alerts to `known-issues.json`
- Generate `hardware-report.md` summaries

**Inbox channel**: `#hardware`

**Example invocations**:
```
# Full hardware health check on all hosts
navig agent run pulse --task "Run hardware health check on all registered hosts and report"

# GPU status on the homelab
navig agent run pulse --task "Check GPU health on primary-desktop"

# Generate a hardware report
navig agent run pulse --task "hardware report"
```
