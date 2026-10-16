# Wiki — NAVIG Android Space

> Knowledge base for the NAVIG Android Space. All pages are source of truth — no duplication across `docs/`.

## Pages

| Page | Description |
|---|---|
| [devices.md](devices.md) | Registered devices — name, model, Android version, serial, role |
| [architecture.md](architecture.md) | Space architecture, agents/formations, decisions |
| [adb-guide.md](adb-guide.md) | ADB & wireless-debugging cheatsheet |
| [debloat-catalog.md](debloat-catalog.md) | Safe-to-remove package catalog per OEM |
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
