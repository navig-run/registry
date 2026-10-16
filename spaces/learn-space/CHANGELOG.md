# Changelog — Learn Space

## [Unreleased] — registry publish

### Changed
- Added `.navig/space.json` (canonical manifest) and an MIT `LICENSE` (NAVIG contributors).
- Author/owner set to `navig-run`; space id aligned to the folder name in every manifest.
- Seed state ships as examples: `.navig/memory/*.example.json` (see `.navig/memory/README.md`) and `.navig/inbox/routes.example.yaml`.
- `.gitignore` keeps runtime memory, inbox and state out of version control.
- `.navig/config.yaml` merged into one YAML document; inbox routes rewritten in the loader schema; library folders added.
- Status → planned: the four packaged skills were never shipped — references removed from the manifest and the skill-assessment workflow.

## [1.0.0] — 2026-03-18

### Added
- Initial space setup with 4 agents: course-tracker, book-synthesizer, skill-planner, review-scheduler
- 3 formations: active-learning, weekly-review, skill-sprint
- 3 workflows: start-course, weekly-review, skill-assessment
- Spaced repetition system
- Skill profile and gap analysis framework
