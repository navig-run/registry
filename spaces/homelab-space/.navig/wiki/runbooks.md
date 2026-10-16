# Runbooks Index — homelab space

> Operational runbooks linking skills, workflows, and agent responsibilities.
> Last updated: 2026-02-26

---

## Quick Reference

| Situation | Runbook | Primary Agent | Skills Used |
|-----------|---------|---------------|-------------|
| Network device missing | [Network Discovery](#network-discovery) | atlas | network-scan, port-audit |
| Disk space critical | [Disk Emergency](#disk-emergency) | wrench | disk-clean |
| Suspicious process | [Process Triage](#process-triage) | sentinel | process-investigate, port-audit |
| New device arrived | [Device Onboarding](#device-onboarding) | atlas + archivist | ssh-connect, hardware-inventory |
| GPU overheating | [GPU Thermal Response](#gpu-thermal-response) | pulse | gpu-health |
| Config out of sync | [Config Sync](#config-sync) | archivist | sync-configs |
| Power cycle needed | [Wake-on-LAN](#wake-on-lan) | herald | wake-on-lan |
| Weekly ops review | [Weekly Review](#weekly-review) | all agents | all skills |

---

## Network Discovery

**Trigger**: New device expected but not reachable; topology change detected.

**Step 1 — Sweep the subnet**
```
navig skill run network-scan --target 192.168.1.0/24
```

**Step 2 — Port-audit any new host**
```
navig skill run port-audit --target <new-ip> --preset quick
```

**Step 3 — Update wiki**
```
# Edit .navig/wiki/devices.md — add new host entry
navig wiki edit devices
```

**Step 4 — Cable trace if physical**
```
navig skill run cable-trace --interactive
```

**Resolution criteria**: Device appears in `devices.md` with confirmed IP, MAC, OS, and role.

---

## Disk Emergency

**Trigger**: Any host reporting <10% free disk space. Alert from `morning-sweep` workflow.

**Step 1 — Identify top consumers**
```
navig skill run disk-clean --target <host> --dry-run
```

**Step 2 — Review output, then execute**
```
navig skill run disk-clean --target <host> --execute
```

**Step 3 — If still critical — archive old logs**
```
# On Linux/macOS
navig skill run sync-configs --source <host>:/var/log/archive --dest backup:/logs/<host>

# On Windows
navig skill run sync-configs --source "<host>:<log-archive-dir>" --dest backup:/logs/<host>
```

**Resolution criteria**: Free space above 20%. Log cleanup documented in `cable-log.md` or wiki.

---

## Process Triage

**Trigger**: sentinel anomaly alert; CPU >90% unexplained; unknown network connection.

**Step 1 — Identify**
```
navig skill run process-investigate --target <host> --mode anomaly
```

**Step 2 — Cross-check open ports**
```
navig skill run port-audit --target <host> --preset full
```

**Step 3 — If malicious — isolate**
```
# Block outbound on Windows (run on target as admin):
navig host use <host>
navig run "netsh advfirewall firewall add rule name='ISOLATE' dir=out action=block"

# Block on Linux:
navig host use <host>
navig run "sudo iptables -I OUTPUT -j DROP"
```

**Step 4 — Document in known-issues**
```
# Edit .navig/memory/known-issues.json — add an entry (see the template in the file)
```

**Resolution criteria**: Process identified, contained, documented. Ticket in `known-issues.json`.

---

## Device Onboarding

**Trigger**: New computer, server, NAS, or peripheral added to the homelab space.

**Step 1 — Run interactive onboarding workflow**
```
navig ask "run the onboard-device workflow"
```

**Step 2 — Hardware inventory**
```
navig skill run hardware-inventory --target <new-host>
```

**Step 3 — SSH key exchange (Linux/macOS targets)**
```
navig skill run ssh-connect --host <new-host> --setup-keys
```

**Step 4 — Register in device registry**
```
# Edit .navig/memory/device-registry.json — add an entry (copy the shape of an example device)
```

**Step 5 — Update wiki**
```
navig wiki edit devices
navig wiki edit network-topology
```

**Resolution criteria**: Device in registry, reachable by name, assigned to a formation, wiki updated.

---

## GPU Thermal Response

**Trigger**: GPU temp >85°C (NVIDIA) or >90°C (AMD). Alert from `hardware-patrol` formation.

**Step 1 — Assess**
```
navig skill run gpu-health --target <host>
```

**Step 2 — Force fan curve (NVIDIA)**
```
navig host use <host>
navig run "nvidia-smi -pm 1 && nvidia-smi --auto-boost-default=0"
```

**Step 3 — Check airflow**
```
# Use cable-trace interactively to verify physical cable routing near GPU exhaust
navig skill run cable-trace --interactive --note "GPU airflow check"
```

**Step 4 — Log event**
```
# Add to known-issues.json with severity: warning
```

**Resolution criteria**: GPU temp stable <80°C. Root cause documented.

---

## Config Sync

**Trigger**: Dotfiles modified on primary machine; new machine needs bootstrap config.

**Step 1 — Dry run**
```
navig skill run sync-configs --source <primary-host> --dest <target-host> --dry-run
```

**Step 2 — Execute**
```
navig skill run sync-configs --source <primary-host> --dest <target-host>
```

**Step 3 — Verify**
```
navig skill run ssh-connect --host <target-host> -- "diff ~/.bashrc /tmp/bashrc.bak"
```

**Resolution criteria**: Target config matches source. No diff errors.

---

## Wake-on-LAN

**Trigger**: Remote machine needed; appears offline.

**Step 1 — Look up MAC from registry**
```
grep -A6 '"<hostname>"' .navig/memory/device-registry.json      # or: Select-String -Context 0,6
```

**Step 2 — Send magic packet**
```
navig skill run wake-on-lan --mac <MAC> --broadcast 192.168.1.255
```

**Step 3 — Confirm wake**
```
# Wait ~30s then:
navig skill run network-scan --target <expected-ip> --quick
```

**Resolution criteria**: Host responds to ping within 60s of WOL packet.

---

## Weekly Review

**Trigger**: Every Monday 08:00 or on demand.

```
navig ask "run the weekly-review workflow"
```

Collects reports from all agents, runs `morning-sweep`, generates wiki entry at `.navig/wiki/weekly-<date>.md`.

**Resolution criteria**: Wiki entry written, all critical issues acknowledged, `known-issues.json` updated.
