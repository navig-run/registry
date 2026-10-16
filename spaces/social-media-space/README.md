# Social Media Space

> Unified command layer for all social media — brands, accounts, content pipelines, scheduling, analytics, and viral intelligence.

## What It Handles

- **Multi-brand** — one brand or fifty, each with its own voice, accounts, and calendar
- **Multi-platform** — X/Twitter · Instagram · LinkedIn · TikTok · YouTube · Threads · Bluesky · Mastodon
- **Content pipeline** — Idea → Brief → Draft → Voice check → Schedule → Published → Analysed
- **Brand voice guardian** — AI-enforced consistency before anything publishes
- **Viral scoring** — hooks scored before publish; best content surfaced automatically
- **Analytics** — per-brand, per-platform, per-post engagement tracking

## Quick Start

```bash
# Set up your first brand
cp -r brands/_template brands/my-brand
# Edit brands/my-brand/voice.json with your brand personality
# Edit brands/my-brand/accounts.json with your platform accounts

# Create a post draft
@post-writer draft --brand my-brand --platform linkedin --topic "Product launch"

# Review drafts in pipeline
@content-strategist calendar --brand my-brand --week current

# Check analytics
@analytics-watcher report --brand my-brand --period last-7-days
```

## Structure

```
brands/           Each brand: voice.json, accounts.json, guidelines.md
content/
  drafts/         Ideas and WIP drafts (not yet approved)
  scheduled/      Approved, queued to publish
  published/      Published content archive
  calendar/       Content calendar data per brand
analytics/        Engagement data per brand/platform
```

## Multi-Brand Model

One space handles any number of brands. Each brand is a folder in `brands/` with:
- `voice.json` — personality, tone, vocabulary, taboos
- `accounts.json` — platform account IDs and metadata
- `guidelines.md` — brand editorial guidelines

See `docs/BRAND_SETUP.md` for full setup instructions.

## First run

Memory ships as examples: copy `.navig/memory/*.example.json` to `*.json` and
`.navig/inbox/routes.example.yaml` to `routes.yaml` (see the README in each folder).
