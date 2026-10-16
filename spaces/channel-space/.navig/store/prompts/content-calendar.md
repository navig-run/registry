# Content Calendar

## Purpose

Generates a structured content calendar with topics, publish dates, and production milestones for batch planning.

## Variables

- `{{WEEKS}}` — Number of weeks to plan
- `{{VIDEOS_PER_WEEK}}` — Publishing frequency
- `{{NICHE}}` — Channel niche or category
- `{{CONTENT_MIX}}` — Content types (tutorial, vlog, review, list)
- `{{EXISTING_IDEAS}}` — Any pre-planned video ideas

## Prompt

You are the Scriptwriter for channel-space. Create a {{WEEKS}}-week content calendar:

**Videos per week**: {{VIDEOS_PER_WEEK}}
**Niche**: {{NICHE}}
**Content mix**: {{CONTENT_MIX}}
**Existing ideas**: {{EXISTING_IDEAS}}

For each week, provide:

| Day | Title | Type | Status | Keywords | Notes |
|-----|-------|------|--------|----------|-------|

Include:
1. **Topic variety** — Balance between content types
2. **SEO timing** — Align topics with search trends
3. **Production schedule** — Script → Film → Edit → Publish dates
4. **Evergreen vs trending** — Mix of time-sensitive and permanent content
5. **Series opportunities** — Identify potential multi-part series
6. **Buffer slots** — Leave room for trending topic responses
