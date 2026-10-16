# Changelog

All notable changes to **broadcast-space** will be documented in this file.

## [1.0.1] — 2026-10-16

### Fixed
- Repository URL and package name (`broadcast-space`, private); author `navig-run`.
- README and package scripts use real commands (`navig flow run …`); removed the
  non-existent `navig space run|pack|push|version`.
- Skills pass parameters as environment variables instead of pasting `{{...}}` into
  shell and PowerShell commands.
- Memory and inbox ship as `*.example.*` seeds; canonical manifest `.navig/space.json`.

### Removed
- `.github/` tooling and empty `docs/`, `scripts/`, `tests/` placeholders.

## [1.0.0] — 2026-07-09

### Added
- Initial release
- 5 agents: host, sound-engineer, show-planner, publisher, community-manager
- 5 formations: episode-production, guest-booking, live-session, content-repurpose, audience-feedback
- 6 workflows: episode-production, guest-pipeline, live-show, weekly-planning, monthly-review, rss-maintenance
- 10 skills: audio-record, audio-edit, noise-reduce, loudness-normalize, rss-generate, show-notes-write, transcript-generate, guest-research, episode-schedule, clip-extract
- 8 prompt templates
- 7 wiki knowledge pages
- Domain configuration for podcast and streaming defaults
- MCP tool declarations for ffmpeg and whisper
