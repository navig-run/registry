# Changelog — war-room-space

## 2.0.1 — 2026-10-16 — registry cleanup

### Fixed
- Space id is `war-room-space` (matches its folder) and tier `work` across every manifest;
  the canonical `.navig/space.json` now reflects the v2 space (the old `.navig/space.config.json` still described v1).
- Skills take parameters from environment variables instead of pasting `{{params.x}}` into Python.
- `arsenal/CONNECTIONS.md` points at the public `navig install add plugin:navig-pentest` instead of the private labs monorepo.
- Memory ships as `*.example.json` seeds; plans refreshed to the v2 scope; incident sub-space id is `incident`.
- Author/owner `navig-run`; LICENSE held by NAVIG contributors.

## 2.0.0 — 2026-06-20 — Operator Command Center (OSINT · Investigation · Ethical Hacking)

Re-oriented the War Room from broad "conflict management" into a **find → investigate →
operate → report** operator command center, with a hard authorization/RoE gate.

### Added
- **Doctrine:** rewrote `.navig/context.md` (Prime Directive — authorization gates everything),
  `README.md`, `docs/ETHICS-AND-AUTHORIZATION.md`.
- **Agents (5):** `osint-analyst`, `recon-operator`, `red-team-lead`, `forensics-investigator`,
  `case-manager` (existing 4 kept).
- **Formations (4):** `osint-sweep`, `recon-and-map`, `investigation`, `red-team-op` (gated).
- **Skills (5):** `open-case`, `add-entity` (OSINT graph), `log-finding`, `map-asset`
  (engagement-gated), `start-engagement` (refuses without written authorization).
- **Memory (6):** `cases`, `entities` (nodes+edges), `findings`, `assets`, `iocs`, `engagements`.
- **Connections/MCP:** `.navig/store/mcp/connections.mcp.json` (filesystem, case-db, web-search/
  fetch, browser, dns-whois, shodan, breach-lookup, gated recon-cli, git/github) + `arsenal/CONNECTIONS.md`.
- **Arsenal:** `osint/` + `recon/` categories; legal `authorization-template` + `rules-of-engagement`;
  forensic `chain-of-custody`; `arsenal/osint/collection-sources`, `arsenal/recon/footprinting-playbook`.
- **Lab:** isolated practice range (`lab/README.md`) — no-egress, target catalog, snapshot discipline.
- **Prompt arsenal (10):** osint-target-profile, entity-graph-pivot, domain-infra-recon,
  attack-surface-map, breach-exposure-check, username-identity-correlation, engagement-scope-roe,
  recon-to-findings, case-intelligence-report, evidence-chain-of-custody (existing 5 incident prompts kept).

### Guardrails
- Every active operation passes the authorization gate (`legal-counsel`); passive/open sources by
  default; scope is a fence; minimize + protect; lab for dangerous work; responsible disclosure.

## 1.0.0 — 2026-03-12

### Added
- Initial release
- Agents: `strategist`, `intelligence-officer`, `legal-counsel`, `narrative-engineer`
- Formations: `ops-command`, `intel-sweep`, `narrative-war`
- Skills: `build-op`, `log-intel`, `advance-status`, `arsenal-search`
- Workflows: `weekly-war-room-brief`
- Memory seeds: operations, intel-log, adversaries, arsenal-registry, space-context
- Arsenal directory structure: legal, verbal, marketing, forensic, cyber
