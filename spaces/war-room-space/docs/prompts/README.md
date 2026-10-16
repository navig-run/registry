# War Room Prompt Library — Incident & Ops Command

> Reusable prompts for running the war-room as an incident/ops command center:
> declare and drive an incident, write the postmortem, hand off on-call cleanly,
> triage severity fast, and draft external comms. Each maps onto the space's agents
> (`strategist` · `intelligence-officer` · `legal-counsel` · `narrative-engineer`),
> skills (`build-op` · `log-intel` · `advance-status` · `arsenal-search`), and the
> `planning → active → hold → closed` operation pipeline.

Run a prompt by pasting its `## Prompt` section into NAVIG / Claude Code from the
war-room space root, filling the `{{VARIABLES}}`. Artifacts land in `operations/`,
`intelligence/`, and `arsenal/`.

## Prompts

- [Incident Commander Runbook](incident-commander-runbook.md) — stand up and drive an active incident with clear roles, cadence, and a live op record.
- [Postmortem Writer](postmortem-writer.md) — turn a closed incident into a blameless, timeline-driven postmortem with real action items.
- [On-Call Handoff](on-call-handoff.md) — transfer the watch cleanly: active ops, watch items, and what could page next.
- [Severity Triage](severity-triage.md) — classify an incoming signal into a severity in minutes, with the response it triggers.
- [Comms & Status-Page Drafter](comms-status-drafter.md) — draft accurate, audience-tuned incident updates for status page, users, and stakeholders.

## OSINT / Investigation / Ethical Hacking

> The operator's go-to playbooks for **find → investigate → operate → report**. These map
> onto the OSINT/investigation/offense agents (`osint-analyst` · `recon-operator` ·
> `red-team-lead` · `forensics-investigator` · `case-manager` · `legal-counsel`), the
> skills (`open-case` · `add-entity` · `log-finding` · `map-asset` · `start-engagement`),
> and the memory stores (`cases.json` · `entities.json` · `findings.json` · `assets.json` ·
> `engagements.json`). **The Prime Directive gates everything**: no recon/scanning/
> exploitation without standing authorization (see
> [ETHICS-AND-AUTHORIZATION.md](../ETHICS-AND-AUTHORIZATION.md)); passive/open sources by
> default; investigations of people carry a legitimate-purpose + minimization + no-harassment
> guardrail; every claim separates **fact from assessment** with confidence and ≥2-source
> corroboration.

- [OSINT Target Profile](osint-target-profile.md) — build a full passive-source profile on a person or org from a seed, writing corroborated nodes to the entity graph.
- [Entity Graph Pivot](entity-graph-pivot.md) — read the current graph and rank the next best pivots (identifiers→accounts→infra→people) by expected value.
- [Domain Infrastructure Recon](domain-infra-recon.md) — passive footprint of a domain (DNS/WHOIS/CT/subdomains/tech/ASN) into an infra map; active enum only under an engagement.
- [Attack Surface Map](attack-surface-map.md) — **gated**: verify engagement + scope first, then map an authorized target's external surface to `assets.json`; refuses without authorization.
- [Breach Exposure Check](breach-exposure-check.md) — check an identity's breach exposure via legitimate sources, explain the risk defensively, recommend remediation — no raw dumps.
- [Username / Identity Correlation](username-identity-correlation.md) — correlate a handle/email across platforms, score confidence, and refuse false merges; privacy guardrails for people.
- [Engagement Scope & RoE](engagement-scope-roe.md) — **the gate**: draft the authorization + scope + Rules of Engagement package and a go/no-go checklist before any active testing.
- [Recon to Findings](recon-to-findings.md) — turn raw recon output into prioritized, deduplicated findings with severity, evidence refs, and remediation (writes `findings.json`).
- [Case Intelligence Report](case-intelligence-report.md) — synthesize a case into a defensible report: BLUF, key judgments with confidence, evidence appendix, and honest gaps.
- [Evidence & Chain of Custody](evidence-chain-of-custody.md) — handle digital evidence forensically: hash-first, who/when/where/how, read-only originals, integrity verified at every hop.
