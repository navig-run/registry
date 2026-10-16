# War Room — Operator Command Center 🛰️

> **OSINT · Investigation · Ethical Hacking.** Find, investigate, and operate from one
> command center — open-source intelligence, structured case-work, attack-surface mapping,
> authorized red-team ops, digital forensics, and an isolated lab. Every operation is **gated
> by written authorization and rules of engagement** (see [Prime Directive](#prime-directive)).

See [`.navig/context.md`](.navig/context.md) for the full doctrine.

## Prime Directive
**No collection, recon, scanning, or exploitation against a target without standing
authorization for that target.** Passive/open sources by default; scope is a fence; minimize
and protect subject data; the dangerous parts happen in the isolated `lab/`; responsible
disclosure always. The `legal-counsel` agent owns this gate — see
[`docs/ETHICS-AND-AUTHORIZATION.md`](docs/ETHICS-AND-AUTHORIZATION.md).

## Agents
| Agent | Theater | Role |
|---|---|---|
| `strategist` | command | War picture across theaters, tasking, priorities (lead) |
| `osint-analyst` | OSINT | Open-source collection, entity enrichment, the graph |
| `recon-operator` | recon | Authorized footprinting + attack-surface mapping |
| `red-team-lead` | offense | Authorized ethical-hacking engagements (ATT&CK), the lab |
| `forensics-investigator` | DFIR | Evidence, artifacts, chain of custody, timelines |
| `case-manager` | investigation | Owns cases end-to-end; the final intelligence report |
| `intelligence-officer` | intel | Adversary tracking, IOC/TTP, signal reliability |
| `legal-counsel` | legal/ethics | The authorization gate — scope, RoE, legality, disclosure |
| `narrative-engineer` | narrative | Comms, counter-narrative, disinformation tracing |

## Skills
| Skill | Purpose |
|---|---|
| `open-case` | Open an investigation (subject, objective, scope, authorization) |
| `add-entity` | Add a node to the OSINT graph (person/org/domain/ip/email/handle/wallet) |
| `log-finding` | Log a corroborated finding (confidence, source, evidence ref) |
| `map-asset` | Register a discovered asset in the attack-surface registry (scoped) |
| `start-engagement` | Open an **authorized** red-team engagement (scope + RoE + auth ref) — gated |
| `build-op` · `advance-status` | Create / advance an operation (planning → active → hold → closed) |
| `log-intel` · `arsenal-search` | Log a signal · search the arsenal |

## Formations
`ops-command` (default) · `osint-sweep` · `recon-and-map` · `investigation` · `red-team-op` (gated) · `intel-sweep` · `narrative-war`

## Pipelines
```
Investigation:    open-case → collect → enrich graph → corroborate → findings → report
Recon (authz):    authorize → footprint → map surface → prioritize → findings → disclose
Red-team (authz): scope+RoE → recon → plan(ATT&CK) → execute-in-scope → evidence → report
Operation spine:  planning → active → hold → closed | aborted
```

## Data plane (`.navig/memory/`)
`cases.json` · `entities.json` (graph) · `findings.json` · `assets.json` (attack surface) ·
`iocs.json` · `engagements.json` (authorized) · `adversaries.json` · `operations.json` ·
`intel-log.json` · `arsenal-registry.json`

## Arsenal & lab
```
arsenal/osint  recon  cyber  forensic  legal  verbal  marketing      lab/  (isolated range — see lab/README.md)
```

## Connections (MCP)
OSINT sources, scanners, the browser, the case DB, and the lab are wired as MCP servers /
registered connections — see [`.navig/store/mcp/`](.navig/store/mcp/) and
[`arsenal/CONNECTIONS.md`](arsenal/CONNECTIONS.md).

## Prompt arsenal
Ready-to-run OSINT / investigation / ethical-hacking prompts in [`docs/prompts/`](docs/prompts/).

## Workflows
| Workflow | Schedule | Purpose |
|---|---|---|
| `weekly-war-room-brief` | Mon 07:00 | Full theater brief: ops, cases, intel, surface, narrative |

---
## First run

Memory ships as examples: copy `.navig/memory/*.example.json` to `*.json` and
`.navig/inbox/routes.example.yaml` to `routes.yaml` (see the README in each folder).

---
_Part of the [NAVIG registry](https://github.com/navig-run/registry) — `navig-space-2` runtime._
