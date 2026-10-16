# Agent Invocation Guide

Complete reference for interacting with every agent in this space.

---

## content-strategist

**Purpose:** Sets direction. Writes briefs, plans weeks, detects pillar gaps.
**Inbox:** #strategy
**Formation:** content-pipeline (lead)

```bash
# Generate weekly content plan for a brand
@content-strategist weekly-plan --brand {slug}

# Create a content brief for a specific topic
@content-strategist brief --brand {slug} --topic "your topic" --pillar education

# Detect pillar gaps (which pillars have no post in 14+ days)
@content-strategist gaps --brand {slug}

# Generate repurposing plan from top performing posts
@content-strategist repurpose --brand {slug} --source-post {post-slug}
```

**Writes to:** `.navig/plans/briefs/`
**Reads from:** `analytics/`, `.navig/memory/space-context.json`

---

## post-writer

**Purpose:** Writes the posts. Always produces 3 hook variants. Respects character limits.
**Inbox:** #drafts
**Formation:** content-pipeline (supporting)

```bash
# Write a new draft post
@post-writer draft --brand {slug} --platform linkedin --brief "brief text here"

# Write from a brief file
@post-writer draft --brand {slug} --platform twitter --brief-file .navig/plans/briefs/brief-slug.md

# Rewrite a rejected draft (with guardian notes)
@post-writer rewrite --brand {slug} --draft content/drafts/{brand}/file.md

# Generate hook variants only
@post-writer hooks --brand {slug} --platform instagram --topic "your topic"
```

**Writes to:** `content/drafts/{brand}/`
**Character limits:** Twitter 280 · Instagram 2200 · LinkedIn 3000 · TikTok 2200 · Threads 500 · Bluesky 300

---

## brand-guardian

**Purpose:** Voice gate. No post goes to scheduler without crossing 7.
**Inbox:** #review (priority: high)
**Formation:** content-pipeline (supporting)

```bash
# Voice check a single draft
@brand-guardian review --brand {slug} --draft content/drafts/{brand}/file.md

# Batch review all drafts in review queue
@brand-guardian batch-review --brand {slug}

# Check brand voice consistency across last 5 published posts
@brand-guardian audit --brand {slug} --last 5

# Request rewrite with specific note
@brand-guardian reject --brand {slug} --draft file.md --note "Too formal — needs conversational register"
```

**Score rubric:**
- 9-10: Publish-ready
- 7-8: Approved
- 5-6: Revise
- 1-4: Reject

**Hard rule:** Never approves anything < 7. No exceptions.

---

## scheduler

**Purpose:** Queue management. No double-booking. Always picks optimal slots.
**Inbox:** #schedule
**Formation:** content-pipeline (supporting)

```bash
# Add an approved draft to the schedule
@scheduler add --brand {slug} --draft content/drafts/{brand}/file.md --platform linkedin --at 2026-03-20T09:00Z

# Let scheduler pick optimal time
@scheduler add --brand {slug} --draft file.md --platform twitter --auto-time

# View upcoming queue for a brand
@scheduler queue --brand {slug} --days 7

# Check for posting gaps
@scheduler gaps --brand {slug}

# Dequeue a scheduled post
@scheduler dequeue --brand {slug} --post 20260320T090000Z-linkedin-post-slug

# Fill a whole week automatically from approved drafts
@scheduler fill-week --brand {slug} --week 2026-W12
```

**Rules:** ±30 min buffer per brand+platform. Only schedules status:approved drafts.

---

## analytics-watcher

**Purpose:** Performance intelligence. Feeds strategy loop. Detects viral.
**Inbox:** #analytics (regular) / #viral (urgent)
**Formations:** analytics-review (lead), viral-radar (lead)

```bash
# Run engagement report for a brand
@analytics-watcher report --brand {slug} --period last-7-days

# Run for all brands
@analytics-watcher report --all --period last-7-days

# Check for viral breakouts
@analytics-watcher viral-check --brand {slug}

# Get top performing hashtags
@analytics-watcher hashtags --brand {slug}

# Detect anomalies
@analytics-watcher anomalies --brand {slug} --threshold 30

# Get best performing content pillars
@analytics-watcher pillars --brand {slug} --period last-30-days
```

**Escalates to:** content-strategist on 30%+ engagement drop.
**Activates viral-radar on:** any post exceeding 3× baseline engagement.
