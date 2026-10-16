# Brand Setup Guide

Detailed walkthrough of setting up a new brand in this space.
Start here when onboarding any brand — spend time here now, save hours
of revisions later.

---

## What Makes a Brand File Set

Every brand lives in `brands/{slug}/` with exactly three files:

```
brands/
  acme/               # Brand slug — lowercase, hyphenated, no spaces
    voice.json        # Personality, tone, rules, thresholds
    accounts.json     # Social media accounts for this brand
    guidelines.md     # Narrative brand rules, target audience, pillars
```

---

## voice.json — Field Reference

This file controls every AI decision about this brand's writing.

```json
{
  "brand": "acme",
  "display_name": "Acme Corp",
  "personality": ["bold", "direct", "clever"],
  "tone": "professional",
  "vocabulary": ["innovative", "proven", "built for scale"],
  "avoid": ["cheap", "simple", "just", "basically", "synergy"],
  "must_feel": ["confident", "informed", "ready to act"],
  "min_body_chars": 200,
  "content_pillars": ["education", "trust", "product", "community"],
  "example_posts": {
    "linkedin": "We built Acme when every existing tool failed us...",
    "twitter": "The dashboard everyone copied? Ours. 4 years ago."
  }
}
```

**Field explanations:**

| Field | Type | Purpose |
|-------|------|---------|
| `personality` | string[] | Adjectives that define the brand voice — post-writer uses these as persona anchors |
| `tone` | string | Overall register: `casual`, `professional`, `authoritative`, `friendly`, `irreverent` |
| `vocabulary` | string[] | Preferred words — brand-guardian rewards their use |
| `avoid` | string[] | Words/phrases that are off-brand — each occurrence costs -2 in voice score |
| `must_feel` | string[] | Emotions the reader must feel after any post — absence docks -0.5 each |
| `min_body_chars` | integer | Minimum length for the post body (excluding hook and CTA) |
| `content_pillars` | string[] | Active content categories for this brand |
| `example_posts` | object | Per-platform example of perfect brand voice — the gold standard for post-writer |

**Tips:**
- Keep `avoid` specific: `"synergy"` is better than `"corporate language"`
- Keep `must_feel` to 2-4 emotions — too many dilutes the signal
- Add `example_posts` entries for every active platform — they dramatically improve output quality

---

## accounts.json — Field Reference

One entry per active social account.

```json
[
  {
    "platform": "linkedin",
    "account_id": "urn:li:organization:12345678",
    "display_name": "Acme Corp",
    "profile_url": "https://linkedin.com/company/acme-corp",
    "credentials_ref": "vault://social-media/acme/linkedin",
    "active": true
  },
  {
    "platform": "twitter",
    "account_id": "@acmecorp",
    "display_name": "Acme Corp",
    "profile_url": "https://x.com/acmecorp",
    "credentials_ref": "vault://social-media/acme/twitter",
    "active": true
  }
]
```

**Field explanations:**

| Field | Type | Purpose |
|-------|------|---------|
| `platform` | string | One of: `twitter`, `linkedin`, `instagram`, `tiktok`, `bluesky`, `threads`, `mastodon` |
| `account_id` | string | Platform-native identifier (username, org ID, etc.) |
| `display_name` | string | Human-readable account name |
| `profile_url` | string | Public profile URL |
| `credentials_ref` | string | Vault path to API credentials — never store credentials in this file |
| `active` | boolean | Set to `false` to pause scheduling for this account without deleting it |

---

## guidelines.md — Template

Free-form narrative guide. Write this once and update when the brand evolves.

```markdown
# {Brand Name} — Content Guidelines

## Target Audience
Who we write for — demographics, roles, goals, pain points.

## Content Pillars

| Pillar | % of content | What it covers |
|--------|-------------|----------------|
| Education | 40% | How-to, industry insights, data |
| Trust | 25% | Customer stories, behind the scenes, provenance |
| Product | 20% | Features, releases, use cases |
| Community | 15% | Q&A, conversation, events |

## Forbidden Topics
- Do not comment on competitors by name
- Do not share unverified data or speculative claims
- Do not discuss pricing in public posts

## Visual Style Notes
(For any platform where images accompany posts)
- Primary color: #...
- Image style: photography / illustration / screenshot
- Always include logo in corner for brand posts

## Competitor Rule
Never tag or name competitors. If differentiating, reference "legacy tools" 
or "traditional approaches" without naming names.
```

---

## After Setup

1. Add brand slug to `active_brands` in `.navig/memory/space-context.json`
2. Create analytics directories (see RB-001)
3. Run voice audit: `@brand-guardian audit --brand {slug}`
4. Generate first brief: `@content-strategist brief --brand {slug} --topic intro`
