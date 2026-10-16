# Brand Setup — Full Reference

> Complete technical documentation for adding and managing brands in the social-media-space.
> See also: [Wiki Brand Setup Guide](../.navig/wiki/brand-setup.md) for a concise walkthrough.

---

## Directory Structure

```
brands/
  _template/          # Copy this to create a new brand
    voice.json
    accounts.json
    guidelines.md
    README.md
  {brand-slug}/       # One directory per brand
    voice.json        # Voice profile — controls all AI writing decisions
    accounts.json     # Social accounts for this brand
    guidelines.md     # Narrative guide — audience, pillars, rules
```

---

## voice.json — Complete Schema

```json
{
  "$schema": "navig:social-media/voice/v1",
  "brand": "string — brand slug, must match parent directory name",
  "display_name": "string — human-readable brand name",
  "personality": ["array of 3-5 adjectives — the brand's character traits"],
  "tone": "casual | professional | authoritative | friendly | irreverent",
  "vocabulary": ["preferred words — reward for using these"],
  "avoid": ["forbidden words and phrases — each occurrence -2 voice score"],
  "must_feel": ["emotions reader must experience — missing keywords -0.5 each"],
  "min_body_chars": 0,
  "content_pillars": ["list of active content categories"],
  "example_posts": {
    "platform": "example of perfect brand-voice post for this platform"
  }
}
```

### Validation Rules

| Field | Required | Allowed Values |
|-------|----------|----------------|
| `brand` | Yes | lowercase, hyphens only |
| `display_name` | Yes | any string |
| `personality` | Yes | 3-5 items |
| `tone` | Yes | one of the 5 allowed values |
| `vocabulary` | No | list of strings |
| `avoid` | Yes | min 3 items recommended |
| `must_feel` | Yes | 2-4 items recommended |
| `min_body_chars` | Yes | integer ≥ 0 |
| `content_pillars` | Yes | min 2 items |
| `example_posts` | No | keyed by platform slug |

---

## accounts.json — Complete Schema

```json
[
  {
    "platform": "twitter | linkedin | instagram | tiktok | bluesky | threads | mastodon",
    "account_id": "platform-native identifier",
    "display_name": "human-readable account name",
    "profile_url": "https://...",
    "credentials_ref": "vault://social-media/{brand}/{platform}",
    "active": true
  }
]
```

### Credentials Management

Credentials are **never** stored in `accounts.json`. They live in the NAVIG vault:

```bash
# Store platform tokens in vault
navig vault set social-media/{brand}/{platform} '{"api_key": "...", "api_secret": "..."}'

# Verify vault entry
navig vault get social-media/{brand}/{platform}
```

---

## guidelines.md — Template Fields

| Section | Required | Purpose |
|---------|----------|---------|
| Target Audience | Yes | Who reads this brand's content |
| Content Pillars table | Yes | Pillar name, % of content, description |
| Forbidden Topics | Yes | What never to post |
| Visual Style Notes | No | Image style, colors (for platforms with visuals) |
| Competitor Rule | Yes | How to handle competitor mentions |

---

## Brand Activation Checklist

- [ ] `brands/{slug}/voice.json` created and all required fields filled
- [ ] `brands/{slug}/accounts.json` created with at least one active account
- [ ] `brands/{slug}/guidelines.md` completed
- [ ] `{slug}` added to `active_brands` in `.navig/memory/space-context.json`
- [ ] Analytics directory created: `analytics/{slug}/{YYYY-MM}/engagement.csv`
- [ ] Hashtag log initialized: `analytics/{slug}/hashtags.json` (empty array `[]`)
- [ ] Voice audit passed: `@brand-guardian audit --brand {slug}` returns no critical issues
- [ ] First brief generated: `@content-strategist brief --brand {slug}`

---

## Deactivating a Brand

1. Set `active: false` on all accounts in `accounts.json`
2. Remove `{slug}` from `active_brands` in space-context.json
3. Archive any pending drafts: `mv content/drafts/{slug}/ content/published/{slug}/ARCHIVED/`
4. Analytics data is preserved in `analytics/{slug}/`
