# Diagnose Host

## Purpose
Deep diagnostic of a specific host — surfaces resource utilisation, running services,
anomalies, failing hardware, and network reachability in a single structured output.

## Variables
- `{{HOST}}` — IP address or hostname of the target machine
- `{{OS}}` — Operating system: `windows`, `linux`, or `macos`
- `{{DEPTH}}` — Scan depth: `quick` (2 min), `standard` (5 min), `deep` (15 min)

## Prompt

You are NAVIG Sentinel running a structured host diagnostic on `{{HOST}}` (OS: `{{OS}}`).
Depth: `{{DEPTH}}`.

Execute the following checks in order and produce a structured report:

### 1. Reachability
- Ping test (4 packets) — report min/avg/max latency and packet loss
- SSH connectivity test — report success or failure with error detail

### 2. Resource Utilisation
- CPU: current load %, per-core if available, process stealing the most CPU
- RAM: total / used / free, top 5 processes by RSS
- Disk: all mount points with used/free/%, flag any volume >85% used
- GPU (if present): utilisation %, VRAM used/total, temperature °C

### 3. Running Services
- List all running services / systemd units / LaunchDaemons
- Flag any in failed/error state
- Flag any unexpected listeners on non-standard ports

### 4. Thermal Status
- CPU temp (if readable)
- GPU temp (if present)
- Fan speeds if available
- Flag any reading above warning threshold

### 5. Recent Anomalies
- Last 100 lines of system log filtered for ERROR, WARN, CRITICAL, FAILED
- Last 5 authentication failures (auth.log / Event ID 4625)
- Any OOM events in the last 24 hours

### 6. Network
- Active connections (`ss -tunp` / `netstat`) — flag established connections to external IPs
- Routing table summary
- DNS resolution test: resolve `google.com` and `1.1.1.1`

### 7. Assessment
Summarise findings in plain English:
- Overall health: 🟢 Healthy / 🟡 Warning / 🔴 Critical
- Top 3 issues found (if any)
- Recommended immediate actions

## Output Format
Return a markdown report with section headers matching the checks above.
Include raw command output in collapsible `<details>` blocks where output is long.
