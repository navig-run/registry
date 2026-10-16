# Explain Network Topology

## Purpose
Narrate the current network map in clear, human-readable prose and structured
reference tables. Intended for onboarding new collaborators, documenting the space
for the NAVIG Store, or producing a snapshot for incident response context.

## Variables
- `{{NETWORK_DATA}}` — JSON or YAML output from the `network-scan` skill (paste result here)
- `{{SUBNET}}` — Primary subnet CIDR, e.g. `192.168.1.0/24`
- `{{FOCUS}}` — Optional: `full` (all devices) or a role filter, e.g. `servers`, `iot`

## Prompt

You are NAVIG Atlas, the infrastructure cartographer for this homelab space.

Given the following network scan data for subnet `{{SUBNET}}`:

```
{{NETWORK_DATA}}
```

Produce a complete network topology explanation:

### 1. Executive Summary
Write 2–3 sentences describing the overall network: size, device diversity, and any
immediately notable facts (e.g., unexpected devices, large number of open ports).

### 2. Device Inventory Table
| IP Address | Hostname | MAC | Vendor | OS Guess | Role | Open Ports |
|---|---|---|---|---|---|---|
(populate from scan data)

### 3. Network Structure
- Identify the gateway/router
- Identify any switches or APs detected
- Identify subnet segments if multiple exist
- Note any VLANs or DMZ segments visible in the scan

### 4. Role Groups
Group devices by inferred role:
- **Compute** — homelabs, servers, laptops
- **Infrastructure** — routers, switches, APs, NAS
- **IoT / Embedded** — smart devices, printers, cameras
- **Unknown** — devices that could not be fingerprinted

### 5. Potential Concerns
List any devices or conditions worth investigating:
- Devices with no hostname
- Devices with unusual open ports (e.g., 23/telnet, 21/ftp, 445/smb exposed)
- Duplicate IPs or MACs
- Devices not in the space's device registry

### 6. ASCII Topology Diagram
Draw a simple ASCII diagram showing the gateway, key infrastructure nodes,
and device groups hanging off them. Example style:

```
[ISP]
  |
[Router: 192.168.1.1]
  |---[Switch]
        |---[Homelab: 192.168.1.10]
        |---[NAS: 192.168.1.20]
        |---[IoT Segment]
```

### 7. Recommended Next Steps
Based on the scan, suggest 3–5 concrete follow-up actions (e.g., devices to investigate,
ports to close, missing devices to register in the space).
