# Changelog — singularity-space

## [Unreleased] — registry publish

### Changed
- Added `.navig/space.json` (canonical manifest) and an MIT `LICENSE` (NAVIG contributors).
- Author/owner set to `navig-run`; space id aligned to the folder name in every manifest.
- Seed state ships as examples: `.navig/memory/*.example.json` (see `.navig/memory/README.md`) and `.navig/inbox/routes.example.yaml`.
- `.gitignore` keeps runtime memory, inbox and state out of version control.
- Inbox route `#singularity` added for the oracle; agent guide aligned with the formations.
- Skill scripts read parameters from `NAVIG_PARAM_*` environment variables instead of templating them into Python source.

## 1.0.0 — 2026-03-12

### Added
- Initial release
- Agents: `oracle`, `signal-tracker`, `destiny-keeper`, `ai-researcher`
- Formations: `signal-watch`, `destiny-mapping`, `ai-frontier`
- Skills: `snapshot-self`, `rate-signal`, `log-insight`, `tag-content`
- Workflows: `weekly-signal-sweep`, `monthly-singularity-review`
- Memory seeds: self-versions, civilization-signals, destiny-log, ai-journal, space-context
