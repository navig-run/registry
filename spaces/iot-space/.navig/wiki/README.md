# Wiki — NAVIG IoT Space

> Knowledge base for the NAVIG IoT Space. All pages are source of truth — no duplication across `docs/`.

## Pages

| Page | Description |
|---|---|
| [devices.md](devices.md) | Registered IoT devices — name, protocol, IP/MAC, firmware, topic |
| [mqtt-topics.md](mqtt-topics.md) | MQTT topic tree and device correlation |
| [segmentation.md](segmentation.md) | VLAN/subnet plan and isolation policy |
| [architecture.md](architecture.md) | System architecture, diagrams, decisions |
| [runbooks.md](runbooks.md) | Quick-reference runbook index |
| [agent-guide.md](agent-guide.md) | Agent roster and how to invoke each |

## How to use

```bash
navig wiki list                     # list all pages
navig wiki search <query>           # search across all pages
navig wiki inbox process            # auto-sort .navig/inbox/ content into wiki
```

## Add a new page

1. Create `.navig/wiki/<topic>.md` with a top-level `#` heading
2. Add an entry to this README table
3. Link from relevant pages
