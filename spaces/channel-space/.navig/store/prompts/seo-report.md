# SEO Report

## Purpose

Generates a comprehensive SEO analysis report for a video or the entire channel, with actionable recommendations.

## Variables

- `{{SCOPE}}` — Analysis scope (single video URL or "channel")
- `{{PERIOD}}` — Time period for data
- `{{COMPETITORS}}` — Competitor channels for comparison
- `{{FOCUS}}` — Focus area (titles, descriptions, tags, all)

## Prompt

You are the Growth Analyst for channel-space. Generate an SEO report:

**Scope**: {{SCOPE}}
**Period**: {{PERIOD}}
**Competitors**: {{COMPETITORS}}
**Focus**: {{FOCUS}}

Report sections:

1. **Executive Summary** — Key findings in 3 bullet points
2. **Title Analysis** — Character count, keyword presence, CTR indicators
3. **Description Audit** — Keyword density, link placement, timestamp usage
4. **Tag Evaluation** — Relevance, coverage, competitor overlap
5. **Search Rankings** — Where videos appear for target keywords
6. **Competitor Comparison** — How our SEO compares to {{COMPETITORS}}
7. **Recommendations** — Prioritised list of improvements
8. **Quick Wins** — Changes that can be made immediately
