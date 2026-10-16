# Changelog — simulation-space

## [Unreleased] — registry publish

### Changed
- Added `.navig/space.json` (canonical manifest) and an MIT `LICENSE` (NAVIG contributors).
- Author/owner set to `navig-run`; space id aligned to the folder name in every manifest.
- Seed state ships as examples: `.navig/memory/*.example.json` (see `.navig/memory/README.md`) and `.navig/inbox/routes.example.yaml`.
- `.gitignore` keeps runtime memory, inbox and state out of version control.
- Tier aligned to `work`; agent guide and GENESIS aligned with the shipped agents and formations.
- Skill scripts read parameters from `NAVIG_PARAM_*` environment variables instead of templating them into Python source.

## 1.0.0 — 2026-03-12

### Added
- Initial release
- Agents: `debugger`, `habit-engine`, `agent-modeler`, `probability-analyst`
- Formations: `debug-loop`, `habit-sim`, `agent-lab`
- Skills: `run-habit`, `log-debug`, `update-agent`, `assess-probability`
- Workflows: `weekly-simulation-review`
- Memory seeds: habits, agent-map, probability-trees, debug-log, space-context
