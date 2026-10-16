# Changelog — research-space

## [Unreleased] — registry publish

### Changed
- Added `.navig/space.json` (canonical manifest) and an MIT `LICENSE` (NAVIG contributors).
- Author/owner set to `navig-run`; space id aligned to the folder name in every manifest.
- Seed state ships as examples: `.navig/memory/*.example.json` (see `.navig/memory/README.md`) and `.navig/inbox/routes.example.yaml`.
- `.gitignore` keeps runtime memory, inbox and state out of version control.
- Tier aligned to `work`; manifests list the shipped workflows.
- Skill scripts read parameters from `NAVIG_PARAM_*` environment variables; dataset names validated and SQL identifiers quoted.

## 1.0.0 — 2026-06-15

### Added
- Initial release
- Agents: `scout`, `crawler`, `curator`, `archivist`, `analyst`
- Formations: `discovery-run`, `crawl-pipeline`, `data-foundry`, `analysis-lab`
- Skills: `web-search`, `track-source`, `crawl-site`, `build-dataset`, `db-query`
- Workflows: `daily-discovery-sweep`, `weekly-research-review`
- Memory seeds: sources, datasets, findings, goals, known-issues, space-context
- MCP config: filesystem, shell, fetch, pluggable web-search
- Pipeline contract: crawls/ (raw) → datasets/ (canonical) → out/research.db (queryable)
