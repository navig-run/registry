# Agent Guide — Clips Space

> Reference for all agents, formations, and usage in clips-space.

## Agents

### clip-director
- **Role**: Creative Lead
- **Formation**: clip-factory
- **Inbox**: #clips
- **Best for**: Clip strategy, quality review, batch planning, content calendar
- **Escalation**: operator

### hook-writer
- **Role**: Hook Specialist
- **Formation**: clip-factory
- **Inbox**: #hooks
- **Best for**: First 3 seconds, captions, CTAs, text overlays, A/B hooks
- **Escalation**: clip-director

### clip-editor
- **Role**: Video Editor
- **Formation**: clip-factory
- **Inbox**: #editing
- **Best for**: Trimming, effects, caption overlay, format adaptation, batch exports
- **Escalation**: clip-director

### trend-scout
- **Role**: Trend Analyst
- **Formation**: trend-ride
- **Inbox**: #trends
- **Best for**: Trending sounds, viral formats, hashtag monitoring, analytics
- **Escalation**: clip-director

### distributor
- **Role**: Multi-Platform Publisher
- **Formation**: batch-schedule
- **Inbox**: #scheduling
- **Best for**: Cross-posting, scheduling, platform adaptation, posting times
- **Escalation**: clip-director

## Formations

| Formation | Lead | Purpose |
|-----------|------|---------|
| clip-factory | clip-director | End-to-end clip production |
| trend-ride | trend-scout | Rapid trend response |
| repurpose-lab | clip-editor | Long-form → short-form conversion |
| batch-schedule | distributor | Weekly batch planning and scheduling |
| performance-review | trend-scout | Cross-platform analytics |

## Common Commands

```bash
# Produce a clip
navig formation run "Make a clip about 5 productivity hacks for TikTok, Reels and Shorts"

# Ride a trend
navig formation run "Ride this trend: <trend URL>"

# Repurpose content
navig formation run "Cut episodes/ep42.mp4 into 5 short clips"

# Plan the week
navig formation run "Plan and schedule next week at 2 clips per day"

# Review performance
navig formation run "Review the last 7 days of clip performance on TikTok, Reels and Shorts"
```

## Tips

1. Start with `clip-factory` for single clips, `batch-schedule` for weekly planning
2. Use `trend-ride` when speed matters — it's optimised for < 4 hour turnaround
3. Use `repurpose-lab` to maximise existing long-form content
4. Run `performance-review` every Friday to inform next week's strategy
5. All workflows support `--dry-run` for preview before execution
