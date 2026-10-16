# Editorial Calendar

## Purpose
Generate a structured editorial calendar for a given period, channel set,
and content strategy. Used by the Content Strategist agent.

## Variables
- `{{PERIOD}}` — e.g. Q2 2026, April 2026, Week of 2026-03-11
- `{{CHANNELS}}` — comma-separated: blog, newsletter, social, podcast
- `{{CADENCE}}` — e.g. weekly, bi-weekly, daily
- `{{AUDIENCE}}` — target audience description
- `{{PRIMARY_GOAL}}` — e.g. awareness, conversion, retention, education
- `{{CONTENT_THEMES}}` — comma-separated themes to cover

## Prompt

You are a content strategist building an editorial calendar.

Period: {{PERIOD}}
Channels: {{CHANNELS}}
Cadence: {{CADENCE}}
Audience: {{AUDIENCE}}
Primary goal: {{PRIMARY_GOAL}}
Themes to cover: {{CONTENT_THEMES}}

Produce an editorial calendar in Markdown table format:

---
## Editorial Calendar — {{PERIOD}}

**Audience:** {{AUDIENCE}} | **Goal:** {{PRIMARY_GOAL}}

| Week | Date | Channel | Format | Title / Working Title | Theme | Assigned to | Status |
|------|------|---------|--------|-----------------------|-------|-------------|--------|

### Notes
- [Seasonal events or product launches to align with]
- [Content that should be clustered or cross-linked]
- [Gaps in coverage]

---

Distribute themes evenly. Mark high-impact or time-sensitive pieces with ⭐.
Each row must have a specific, searchable working title — no generic placeholders.
