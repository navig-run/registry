# Space memory

Runtime state for this space's agents and skills. Nothing personal ships here: each
seed is published as `<name>.example.json`. On first use, copy an example to
`<name>.json` (same folder) and the agents read and update that copy — skills that
write state create the file themselves when it is missing.

| Seed | Runtime file |
|------|--------------|
| `agent-map.example.json` | `agent-map.json` |
| `debug-log.example.json` | `debug-log.json` |
| `goals.example.json` | `goals.json` |
| `habits.example.json` | `habits.json` |
| `known-issues.example.json` | `known-issues.json` |
| `probability-trees.example.json` | `probability-trees.json` |
| `space-context.example.json` | `space-context.json` |

Keep your runtime copies out of version control (they hold your own data).
