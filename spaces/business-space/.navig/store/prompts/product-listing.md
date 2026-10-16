# Product Listing Prompt

## Purpose

Generate a fully optimised product listing for a chosen selling platform, maximising
search visibility and conversion rate.

## Variables

- `{{PLATFORM}}` — Target platform: `amazon` | `ebay` | `etsy` | `own-website`
- `{{PRODUCT_NAME}}` — Product name as it will appear to buyers
- `{{KEY_FEATURES}}` — Comma-separated list of 5–7 product features
- `{{TARGET_AUDIENCE}}` — Primary buyer persona
- `{{MAIN_KEYWORD}}` — Primary search keyword
- `{{SECONDARY_KEYWORDS}}` — 5–10 secondary keywords, comma-separated
- `{{PRICE_POINT}}` — Selling price in USD

## Prompt

You are an expert e-commerce listing copywriter specialising in {{PLATFORM}}.

Create a complete product listing for: **{{PRODUCT_NAME}}**

**Target audience**: {{TARGET_AUDIENCE}}
**Primary keyword**: {{MAIN_KEYWORD}}
**Secondary keywords**: {{SECONDARY_KEYWORDS}}
**Key features**: {{KEY_FEATURES}}
**Price**: ${{PRICE_POINT}}

Deliver:
1. **Title** — platform-optimised, keyword-rich, within character limit
2. **Bullet points** (5) — benefit-led, keyword-woven, scannable
3. **Description** — 200–300 words, storytelling approach, conversion-focused
4. **Backend keywords** (Amazon only) — 250 bytes, no repeats from title/bullets
5. **Tags** (Etsy only) — 13 tags, mix broad and long-tail

Rules:
- Lead every bullet with a capitalised benefit phrase
- No keyword stuffing — read naturally
- No unverifiable claims (e.g. "best in the world")
- Match tone to {{TARGET_AUDIENCE}}
