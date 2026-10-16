# Changelog — NAVIG Homelab Space

All notable changes to the `homelab-space` space will be documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [1.2.0] — 2026-10-16

### Removed
- Windows Start-menu organizer scripts and the Explorer context-menu `.reg` fixes — they
  were single-machine maintenance tooling, not homelab capability.
- The bundled default persona; the space now defaults to its own `atlas` agent.
- The `dev` / `chrome` subspace claim — those are standalone spaces (`dev-space`,
  `chrome-ext-space`) installed on their own.

### Changed
- Space id is `homelab-space`; author `navig-run`.
- Memory files and inbox routes ship as `*.example.*` seeds — copy them to their live names.
- `tools/smartctl` pack resolves `smartctl` from PATH (or `homelab.smartctl_path`) and no
  longer edits the machine PATH.
- Layout paths in `config.yaml` match the real tree (`.navig/skills/`, `.navig/store/…`).
- Docs use placeholders instead of machine-specific paths.

---

## [1.1.0] — 2026-03-01

### Added

**Skills**
- `disk-health` — physical disk & volume health for Windows/Linux/macOS; covers `Get-PhysicalDisk`, `Get-StorageReliabilityCounter` (temperature, wear, latency), `Get-Volume` (free space, dirty bit), WMI cross-check, Windows Event Log disk errors, and optional `smartctl` SMART attributes

**Tool Pack**
- `tools/smartctl/pack.yaml` — Tool Pack wrapping smartmontools `smartctl`; commands: `health`, `nvme`, `info`, `scan`, `selftest_short`, `selftest_results`; Windows uses `/dev/pdN` device path

**Tests**
- `test-disk-health.ps1` — 7-step PowerShell smoke test covering all Windows disk-health steps

**Note:** Windows `Get-StorageReliabilityCounter` can report `Wear: 0` on NVMe drives — a known Windows driver limitation. Use smartctl for true wear data.

### Changed
- `disk-health` `smart_check_windows` step: fixed device path to use `/dev/pdN` (not `/dev/nvme0`, which fails on Windows); smartctl binary resolved from PATH or the default smartmontools install location

---

## [1.0.0] — 2026-02-26

### Added

**Skills (10)**
- `network-scan` — cross-platform LAN device discovery via nmap / arp
- `port-audit` — open port auditing with quick and full presets
- `cable-trace` — interactive physical cable documentation wizard
- `hardware-inventory` — full hardware enumeration (CPU, GPU, RAM, storage) for Windows/Linux/macOS
- `gpu-health` — GPU temperature, VRAM, driver health for NVIDIA and AMD
- `disk-clean` — safe disk cleanup with mandatory dry-run preview
- `process-investigate` — suspicious and resource-heavy process detection
- `ssh-connect` — rapid SSH with key setup support and host registry lookup
- `wake-on-lan` — WOL magic packet sender with Python fallback
- `sync-configs` — rsync/robocopy dotfile and config synchronization

**Formations (5)**
- `network-ops` — network scanning, topology, cable documentation
- `hardware-patrol` — GPU, CPU, thermal, disk health monitoring
- `cross-platform-ops` — OS-aware command routing
- `security-watch` — port audits, anomaly detection, security reporting
- `maintenance-crew` — disk clean, log rotation, update checking, config sync

**Agents (6)**
- `atlas` — infrastructure cartographer (network-ops)
- `sentinel` — security and anomaly watcher (security-watch)
- `wrench` — maintenance automator (maintenance-crew)
- `herald` — cross-platform command translator (cross-platform-ops)
- `archivist` — config and knowledge keeper (maintenance-crew)
- `pulse` — hardware health monitor (hardware-patrol)

**Prompts (8)**
- `diagnose-host` · `explain-network-topology` · `security-brief` · `hardware-report`
- `onboard-device` · `cable-map-wizard` · `incident-response` · `weekly-ops-review`

**Workflows (6)**
- `morning-sweep` (daily) · `deep-audit` (on-demand) · `onboard-device` (on-demand)
- `cable-map-update` (on-demand) · `nightly-sync` (nightly) · `weekly-review` (weekly)

**Wiki (6 entries)**
- `architecture.md` · `devices.md` · `network-topology.md`
- `cable-log.md` · `runbooks.md` · `agent-guide.md`

**Memory files (4)**
- `space-context.json` · `device-registry.json` · `known-issues.json` · `goals.json`

**Infrastructure**
- MCP config: `.navig/store/mcp/workstation.mcp.json` with per-agent tool allowlists and security policy
- Inbox routes: `routes.yaml` with 6 channels, escalation rules, and notification settings
- `.gitignore` with sensible defaults for secrets, logs, and local-only data

**Store assets**
- `space.manifest.json` — NAVIG Store manifest with all required fields
- `README.md` — publication-quality space documentation
- `PREVIEW.md` — store listing card
- `CHANGELOG.md` — this file
- `LICENSE` — MIT
- `screenshots/` — screenshot descriptor files

---

## [Unreleased]

*Planned for future versions:*
- `vpn-connect` skill — WireGuard / OpenVPN connection management
- `backup-verify` skill — verify integrity of backup destinations
- `dns-check` skill — local DNS resolution diagnostics
- `docker-health` skill — container and compose stack health
- `thermal-trend` workflow — log thermal data over time and surface degradation trends
- `failover-test` workflow — simulate primary machine failure, verify secondary readiness
