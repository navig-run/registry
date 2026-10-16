# NAVIG Homelab Space

**Command-and-control hub for all your hardware, devices, and networks.**

---

## What It Is

A production-grade NAVIG space for managing every machine in your personal environment —
desktops, laptops, servers, NAS, routers — across **Windows, Linux, and macOS** from
a single pane of glass. Fork it, fill in your device list, and you're operational in
under 10 minutes.

---

## Key Features

- **11 cross-platform skills** — network scan, port audit, GPU health, disk health, disk clean, WOL, SSH, cable trace, hardware inventory, process investigation, config sync
- **6 specialized agents** — atlas (network), sentinel (security), pulse (hardware), wrench (maintenance), herald (cross-platform), archivist (configs)
- **6 automated workflows** — morning sweep, deep audit, device onboarding, nightly sync, weekly review, cable mapping
- **8 production prompts** — diagnose host, security brief, hardware report, incident response, weekly ops review + more
- **Full wiki starter kit** — architecture, device registry, network topology, cable log, runbooks, agent guide

---

## Usage Example

```bash
# Install and activate the space
navig space install github:navig-run/registry/spaces/homelab-space
navig space use homelab-space

# Discover all devices on your LAN
navig skill run network-scan --target 192.168.1.0/24

# Full morning sweep (network + hardware + disk + anomalies)
navig ask "run the morning-sweep workflow"

# Onboard a new device interactively
navig ask "run the onboard-device workflow"

# Get a security situation report
navig agent run sentinel --task "security brief"
```

---

**Platform**: Windows · Linux · macOS
**Category**: Infrastructure · Homelab
**Version**: 1.2.0
**License**: MIT
