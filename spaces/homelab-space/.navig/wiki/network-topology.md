# Network Topology

**Space**: `homelab`  
**Last Updated**: 2026-02-26  
**Maintained by**: Atlas  
**Auto-updated by**: `morning-sweep` workflow (post network scan)

---

## Network Overview

> **Update this section** after running your first network scan:
> `navig skill run network-scan && navig agent run atlas --task "explain network topology"`

| Parameter | Value |
|---|---|
| **Primary Subnet** | `192.168.1.0/24` *(update to your subnet)* |
| **Gateway** | `192.168.1.1` |
| **DNS** | `192.168.1.1` (router) + `1.1.1.1` (upstream) |
| **DHCP Range** | `192.168.1.100 – 192.168.1.254` |
| **Static Range** | `192.168.1.2 – 192.168.1.99` |
| **Devices (known)** | 0 *(populate via onboard-device)* |
| **Last Scanned** | *(run morning-sweep)* |

---

## Recommended IP Allocation Pattern

```
192.168.1.1       → Router / Gateway
192.168.1.2–9     → Network infrastructure (switches, APs)
192.168.1.10–49   → Homelabs / Laptops
192.168.1.50–79   → Servers / NAS
192.168.1.80–99   → IoT / Smart devices
192.168.1.100+    → DHCP pool
```

---

## ASCII Topology Diagram

> Replace this template with output from `explain-network-topology` prompt after first scan.

```
[ISP/WAN]
     |
[Router: 192.168.1.1]
     |
  [Core Switch]
  |          |          |          |
[Homelabs] [Servers]  [NAS]  [IoT/AP]
 .10–.49      .50–.79   .80+
```

---

## Subnet Segments

| Segment | CIDR | Purpose | VLAN |
|---|---|---|---|
| Main LAN | `192.168.1.0/24` | All devices | 1 (default) |
| *(add more if you have VLANs)* | | | |

---

## Active Services Map

| IP | Service | Port | Protocol | Accessible From |
|---|---|---|---|---|
| 192.168.1.1 | Router Admin | 80/443 | HTTP/S | LAN only |
| *(add after first port audit)* | | | | |

---

## Known External Connectivity

| Service | Direction | Port | Notes |
|---|---|---|---|
| *(none configured)* | | | |

---

## Scan History

| Date | Hosts Found | New | Gone | Scan Tool |
|---|---|---|---|---|
| *(run morning-sweep to populate)* | | | | |

---

## Anomalies & Watchlist

Devices discovered on the network but not in the device registry:

| IP | MAC | First Seen | Status |
|---|---|---|---|
| *(none)* | | | |

---

## Topology Update Log

| Date | Change | Changed by |
|---|---|---|
| 2026-02-26 | Initial topology file created | Archivist |
