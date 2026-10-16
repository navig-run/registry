# War Room — Operator Command Center

The War Room is the operator's command center for **OSINT, investigation, and authorized
offensive security**. It finds, investigates, and operates: open-source intelligence on
people / orgs / infrastructure, structured case-work that turns scattered signals into a
defensible intelligence product, attack-surface mapping and ethical hacking against
**authorized** targets, digital forensics, and the lab where tradecraft is practiced safely.

It keeps the original four conflict theaters (legal, narrative, competitive intel, cyber) —
an investigation almost always has a legal and a narrative dimension — but its center of
gravity is now **find → investigate → operate → report**, run from one place with many
connections (MCP servers, data sources, the lab) wired in.

## The Prime Directive — authorization gates everything

> **No collection, recon, scanning, or exploitation against a target without standing
> authorization for that target.** This is not advisory. It is the gate every operation
> passes through.

1. **Authorized targets only.** Every active engagement references a written authorization
   (scope + rules of engagement + dates + asset list) recorded in `engagements.json`. OSINT
   on public figures/orgs follows legality + platform ToS + privacy law; **passive/open
   sources by default**, no unauthorized access, no social-engineering of real people without
   explicit scope.
2. **Scope is a fence, not a suggestion.** In-scope assets are explicit. Out-of-scope is
   off-limits even if reachable. Recon that drifts out of scope is a stop-and-escalate event.
3. **Minimize and protect.** Collect the minimum that answers the question. Treat subject data
   as sensitive; redact PII in reports that don't need it; store evidence with chain of custody.
4. **Lab for the dangerous parts.** Exploit development, malware analysis, and tool practice
   happen in the **isolated lab** (no egress), never against production or third parties.
5. **Responsible disclosure.** Findings against real systems go to the owner first, with a
   remediation window, before anyone else.

The `legal-counsel` agent owns this gate. `red-team-lead` cannot open an engagement, and
`recon-operator` cannot begin active recon, until the gate is green.

## The pipelines

```
Investigation:    open-case → collect (OSINT) → enrich entity-graph → corroborate → findings → report
Recon (authz):    authorize → footprint → map attack-surface → prioritize → findings → disclose
Red-team (authz): scope+RoE → recon → plan (ATT&CK) → execute-in-scope → evidence → report → remediate
Threat-intel:     observe → log IOC/TTP → attribute → adversary dossier → hunt
Operation:        planning → active → hold → closed | aborted   (the spine that tracks them all)
```

## Capabilities & memory (the operator's data plane)

| Capability | Memory store | What it holds |
|---|---|---|
| Investigations | `cases.json` | cases: subject, objective, scope, authorization, status, report ref |
| OSINT graph | `entities.json` | nodes (person/org/domain/ip/email/handle/wallet/asset) + typed edges |
| Findings | `findings.json` | per-case findings with confidence, source, evidence ref |
| Attack surface | `assets.json` | discovered hosts/domains/ports/services/exposures (scoped) |
| Threat intel | `iocs.json` | indicators + ATT&CK TTPs, linked to adversaries |
| Engagements | `engagements.json` | **authorized** red-team engagements: scope, RoE, auth ref, dates |
| Adversaries | `adversaries.json` | dossiers (existing) |
| Operations | `operations.json` | the tracking spine (existing) |
| Intel signals | `intel-log.json` | timestamped signals + reliability (existing) |
| Arsenal | `arsenal-registry.json` | tools/playbooks/templates inventory (existing) |

## Agents

| Agent | Theater | Role |
|---|---|---|
| `strategist` | command | War picture across all theaters, tasking, priorities (lead) |
| `osint-analyst` | OSINT | Open-source collection, entity enrichment, the graph |
| `recon-operator` | recon | Authorized footprinting + attack-surface mapping |
| `red-team-lead` | offense | Authorized ethical-hacking engagements (ATT&CK), the lab |
| `forensics-investigator` | DFIR | Evidence, artifacts, chain of custody, timelines |
| `case-manager` | investigation | Owns cases end-to-end; the final intelligence report |
| `intelligence-officer` | intel | Adversary tracking, IOC/TTP, signal reliability |
| `legal-counsel` | legal/ethics | **The authorization gate** — scope, RoE, legality, privacy, disclosure |
| `narrative-engineer` | narrative | Comms, counter-narrative, disinformation tracing |

## Formations

```
ops-command     strategist leads — default, cross-theater command
osint-sweep     osint-analyst + case-manager — collection → graph
recon-and-map   recon-operator + osint-analyst — footprint authorized target
investigation   case-manager leads + osint-analyst + forensics-investigator — full case
red-team-op     red-team-lead + recon-operator, GATED by legal-counsel — authorized offense
intel-sweep     intelligence-officer — threat/IOC sweep (existing)
narrative-war   narrative-engineer — comms theater (existing)
```

## Arsenal & lab

```
arsenal/osint/      collection playbooks, source lists, pivot recipes, sock-puppet hygiene
arsenal/recon/      footprinting/enumeration playbooks (scoped), tooling notes
arsenal/cyber/      offense playbooks, ATT&CK mappings, exploit notes (lab only)
arsenal/forensic/   evidence protocols, chain-of-custody, artifact parsers
arsenal/legal/      authorization templates, RoE, NDAs, disclosure templates
arsenal/verbal/     interview/elicitation, reporting language, counter-narrative
arsenal/marketing/  competitive positioning (existing theater)
lab/                isolated practice range — targets, snapshots, NO egress (see lab/README.md)
```

## Operating principles

1. **Find, then prove.** A lead is a hypothesis. A finding has corroboration (≥2 independent
   sources) and a confidence score. Reports separate *fact* from *assessment*.
2. **Everything is logged.** Every signal, entity, finding, and asset is timestamped with a
   source and reliability. The case is reproducible by another analyst from the log alone.
3. **Passive before active.** Exhaust open/passive sources before touching the target.
4. **The graph is the truth.** People, orgs, infra, and identifiers are nodes; relationships
   are edges. Pivots happen on the graph, not in your head.
5. **Connections are configured, not improvised.** OSINT sources, scanners, the browser, the
   case DB, and the lab are wired as MCP servers / registered connections (see
   `.navig/store/mcp/` + `arsenal/CONNECTIONS.md`) — each with its auth and a legality note.
6. **The gate is sacred.** See the Prime Directive. When in doubt, stop and ask the operator.
