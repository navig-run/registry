# Changelog — residence-space

## [Unreleased] — registry publish

### Changed
- Added `.navig/space.json` (canonical manifest) and an MIT `LICENSE` (NAVIG contributors).
- Author/owner set to `navig-run`; space id aligned to the folder name in every manifest.
- Seed state ships as examples: `.navig/memory/*.example.json` (see `.navig/memory/README.md`) and `.navig/inbox/routes.example.yaml`.
- `.gitignore` keeps runtime memory, inbox and state out of version control.
- Inbox routes now cover the `#home` and `#medical` channels the agents use.
- Skill scripts read parameters from `NAVIG_PARAM_*` environment variables instead of templating them into Python source.
- Doc fixes: audit cadence (monthly), memory path, retired `navig flow run` replaced by agent invocations.

## 1.0.0 — 2026-03-12

### Added
- Initial release
- `housekeeper`, `medic`, `steward`, `organizer` agents
- Formations: `household-ops`, `medical-watch`, `maintenance-crew`
- Skills: `log-item`, `track-medication`, `check-expiry`, `inventory-export`
- Workflows: `weekly-home-review`, `medication-expiry-check`, `monthly-inventory-audit`
- Prompts: `home-audit-brief`, `medication-review`, `room-inventory`, `maintenance-checklist`
- Memory seeds: room-registry, inventory, medication-log, maintenance-log, goals, known-issues
