# Wiki — NAVIG Homelab Space

> Knowledge base for the NAVIG Homelab Space. All pages are source of truth — no duplication across `docs/`.

## Pages

| Page | Description |
|---|---|
| [devices.md](devices.md) | Registered devices — hostname, IP, OS, role |
| [architecture.md](architecture.md) | System architecture, diagrams, decisions |
| [runbooks.md](runbooks.md) | Quick-reference runbook index |
| [agent-guide.md](agent-guide.md) | Agent roster and how to invoke each |
| [cable-log.md](cable-log.md) | Physical cable connection log |
| [network-topology.md](network-topology.md) | Network topology diagram and notes |

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
