# Changelog

## [1.0.1] — 2026-10-16

### Fixed
- Space id is now `social-media-space` (matches its folder) in every manifest.
- Skills take parameters from environment variables (no `{{...}}` pasted into Python or
  PowerShell) and reject brand slugs / draft names that would escape their folder.
- `.navig/plans/briefs/` exists (formations and workflows write briefs there); runtime
  outputs in `.navig/ops/`, `.navig/memory/` and `briefs/` are gitignored.
- README: `cp -r` for the brand template.

### Removed
- Stray `.navig/space-config.json`, runtime `.navig/local-persona-override.json`, empty
  `screenshots/`, `scripts/`, `tests/` placeholders and `.github/` tooling.

## [1.0.0] — 2026-03-18

### Added
- Full `.navig/` structure: config, context, store, memory, plans, wiki
- Agents: `content-strategist`, `post-writer`, `analytics-watcher`, `brand-guardian`, `scheduler`
- Formations: `content-pipeline`, `analytics-review`, `viral-radar`
- Skills: `create-post-draft`, `schedule-post`, `analyze-engagement`, `check-brand-voice`, `hashtag-research`
- Workflows: `weekly-content-plan`, `daily-post-review`, `analytics-weekly`, `viral-monitor`
- Prompts: `post-draft`, `content-calendar`, `brand-voice-check`, `viral-hook-score`
- Multi-brand data model: `brands/` with per-brand `voice.json`, `accounts.json`, `guidelines.md`
- Content pipeline directories: `content/drafts/`, `content/scheduled/`, `content/published/`, `content/calendar/`
- Analytics directory: `analytics/`
- Brand template: `brands/_template/`
- Full wiki: `README.md`, `agent-guide.md`, `runbooks.md`, `brand-setup.md`
- Documentation: `docs/BRAND_SETUP.md`, `docs/PLATFORM_GUIDE.md`
- `.github/instructions/` with `MASTER.instructions.md` and `plugin-sdk.instructions.md`
