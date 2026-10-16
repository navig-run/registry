# Changelog — Travel Space

## [Unreleased] — registry publish

### Changed
- Added `.navig/space.json` (canonical manifest) and an MIT `LICENSE` (NAVIG contributors).
- Author/owner set to `navig-run`; space id aligned to the folder name in every manifest.
- Seed state ships as examples: `.navig/memory/*.example.json` (see `.navig/memory/README.md`) and `.navig/inbox/routes.example.yaml`.
- `.gitignore` keeps runtime memory, inbox and state out of version control.
- `.navig/config.yaml` merged into one YAML document; inbox routes rewritten in the loader schema.
- Status → planned: the four packaged skills were never shipped — references removed from the manifest and the new-trip workflow.

## [1.0.0] — 2026-03-18

### Added
- Initial space setup with 4 agents: trip-planner, itinerary-builder, budget-watcher, document-keeper
- 3 formations: trip-planning, active-trip, post-trip
- 3 workflows: new-trip, pre-departure, trip-debrief
- Trip folder structure templates
- Pre-departure document checklist system
