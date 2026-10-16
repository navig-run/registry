# Network Segmentation

**Space**: `iot`
**Last Updated**: 2026-07-10
**Maintained by**: Warden
**Auto-updated by**: `security-mesh` formation (post vlan-audit)

---

## Segmentation Policy

IoT devices are untrusted by default. They live on an **isolated VLAN** and may reach
the internet and the local MQTT broker / Home Assistant, but **must not** initiate
connections into the trusted LAN.

| Parameter | Value |
|---|---|
| **IoT VLAN** | `20` *(update to your VLAN)* |
| **IoT Subnet** | `192.168.20.0/24` |
| **Trusted (main) Subnet** | `192.168.1.0/24` |
| **Gateway** | `192.168.20.1` |
| **DHCP Range (IoT)** | `192.168.20.100 – 192.168.20.254` |
| **Static Range (IoT)** | `192.168.20.2 – 192.168.20.99` |

---

## Isolation Rules (intent)

```
IoT VLAN 20  ── ALLOW ──►  Internet (WAN)
IoT VLAN 20  ── ALLOW ──►  MQTT broker + Home Assistant (specific IP:port only)
IoT VLAN 20  ── DENY  ──►  Trusted LAN 192.168.1.0/24 (no new sessions)
Trusted LAN  ── ALLOW ──►  IoT VLAN 20 (established, for control)
```

The trusted LAN may reach IoT devices to control them; IoT devices may **not** reach the
trusted LAN. Verify with `navig skill run vlan-audit`.

---

## Recommended IP Allocation Pattern (IoT VLAN)

```
192.168.20.1        → VLAN gateway
192.168.20.2–9      → Hubs / coordinators (Zigbee, Z-Wave, broker bridge)
192.168.20.10–49    → Cameras / high-bandwidth
192.168.20.50–99    → Static plugs, bulbs, controllers
192.168.20.100+     → DHCP pool (sensors, transient devices)
```

---

## Segment Membership

| Device | IP | Expected VLAN | Confirmed | Notes |
|---|---|---|---|---|
| *(populate via vlan-audit)* | | | | |

---

## Boundary Crossings & Leaks

Devices that appeared outside their expected segment:

| Device | IP Seen | Expected Subnet | Detected | Status |
|---|---|---|---|---|
| *(none)* | | | | |

---

## Cloud Phone-Home Watchlist

IoT devices with known cloud dependencies to monitor (or block at the firewall):

| Device | Endpoint | Direction | Policy |
|---|---|---|---|
| *(add as discovered)* | | | |

---

## Segmentation Update Log

| Date | Change | Changed by |
|---|---|---|
| 2026-07-10 | Initial segmentation policy created | Warden |
