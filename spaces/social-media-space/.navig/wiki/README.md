# Social Media Space — Wiki

Quick reference for agents, operators, and contributors.

---

## Agent Roster

| Agent | Role | Formation | Inbox | What to ask |
|-------|------|-----------|-------|-------------|
| `content-strategist` | Lead | content-pipeline | #strategy | Briefs, weekly plan, pillar gaps |
| `post-writer` | Writer | content-pipeline | #drafts | Draft posts, hook variants, repurposing |
| `brand-guardian` | Voice gate | content-pipeline | #review | Voice audits, approve/reject drafts |
| `scheduler` | Queue manager | content-pipeline | #schedule | Schedule posts, check gaps, dequeue |
| `analytics-watcher` | Data lead | analytics-review / viral-radar | #analytics / #viral | Engagement reports, breakout detection |

---

## Channel Map

| Channel | Purpose | Primary Agent |
|---------|---------|---------------|
| `#strategy` | Content briefs, weekly plans | content-strategist |
| `#drafts` | Post writing, draft handoffs | post-writer + brand-guardian |
| `#review` | Voice check, approval decisions | brand-guardian |
| `#schedule` | Queue management | scheduler |
| `#analytics` | Performance reports | analytics-watcher |
| `#viral` | Breakout alerts — URGENT | analytics-watcher + content-strategist |

---

## Formation Map

| Formation | What it does | Lead |
|-----------|--------------|------|
| `content-pipeline` | Idea → draft → voice-check → scheduled | content-strategist |
| `analytics-review` | Weekly performance digest | analytics-watcher |
| `viral-radar` | Breakout detection + rapid follow-up | analytics-watcher |

---

## Quick Invocations

```bash
# Get this week's content plan for a brand
@content-strategist weekly-plan --brand acme

# Write a post
@post-writer draft --brand acme --platform linkedin --brief "..."

# Voice check a draft
@brand-guardian review --draft content/drafts/acme/2026-03-18.md

# Schedule an approved post
@scheduler add --brand acme --draft 2026-03-18.md --platform linkedin --at 2026-03-20T09:00Z

# Check upcoming queue
@scheduler queue --brand acme --days 7

# Run analytics
@analytics-watcher report --brand acme --period last-7-days

# Trigger viral monitor
@analytics-watcher viral-check --brand acme
```

---

## Key Thresholds

| Threshold | Value | File |
|-----------|-------|------|
| Voice score to approve | ≥ 7 | space-context.json |
| Hook score to publish | ≥ 7 | space-context.json |
| Viral breakout multiplier | 3× baseline | space-context.json |
| Engagement anomaly flag | ±30% delta | space-context.json |
| Scheduling buffer | ±30 min same brand+platform | scheduler agent |

---

## Docs

- [Brand Setup Guide](brand-setup.md)
- [Runbooks](runbooks.md)
- [Agent Invocation Guide](agent-guide.md)
- [docs/BRAND_SETUP.md](../docs/BRAND_SETUP.md) — full schema reference
- [docs/PLATFORM_GUIDE.md](../docs/PLATFORM_GUIDE.md) — platform best practices
