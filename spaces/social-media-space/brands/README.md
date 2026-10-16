# Brands

This directory holds one folder per brand managed in this space.

---

## Structure

```
brands/
  _template/          # Template files — copy to create a new brand
    voice.json        # Voice profile template
    accounts.json     # Social accounts template
    guidelines.md     # Narrative guidelines template
    README.md         # This doc
  {brand-slug}/       # One folder per brand
    voice.json        # Brand voice — personality, tone, rules, thresholds
    accounts.json     # Active social media accounts
    guidelines.md     # Target audience, content pillars, rules
```

---

## Add a New Brand

```bash
# 1. Create brand directory using template
cp -r brands/_template brands/{slug}

# 2. Fill in the 3 files — see docs/BRAND_SETUP.md for full schema
# voice.json, accounts.json, guidelines.md

# 3. Activate the brand
# add {slug} to "active_brands" in .navig/memory/space-context.json

# 4. Initialize analytics
mkdir -p analytics/{slug}/$(date +%Y-%m)
echo "date,platform,post_id,post_slug,impressions,likes,comments,shares,clicks,saves,reach,hook_score" \
  > analytics/{slug}/$(date +%Y-%m)/engagement.csv
echo "[]" > analytics/{slug}/hashtags.json
```

---

## Active Brands

Add your brand slugs below as you onboard them. The source of truth is
`.navig/memory/space-context.json` (`active_brands` array) — this list is
for human reference only.

| Slug | Display Name | Status | Platforms |
|------|-------------|--------|-----------|
| *(none yet)* | | | |

---

## Voice File Quick Reference

The `voice.json` file is the most important file in a brand folder.
It controls every AI decision about tone, word choice, and quality gates.

| Field | Controls |
|-------|---------|
| `personality` | The writing persona post-writer adopts |
| `avoid[]` | Words costing -2 per occurrence in voice score |
| `must_feel[]` | Emotions that must be present (-0.5 each if missing) |
| `min_body_chars` | Minimum post body length |

See [docs/BRAND_SETUP.md](../docs/BRAND_SETUP.md) for full schema documentation.
