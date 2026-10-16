# Post Draft Prompt

## Purpose
Generate a complete social media post — hook, body, and CTA — that fits
the brand voice, respects platform character limits, and opens with a
scroll-stopping hook designed to break the pattern.

---

## Variables

| Variable | Description |
|----------|-------------|
| `BRAND` | Brand slug (e.g., `acme`) |
| `PLATFORM` | Target platform (twitter/linkedin/instagram/tiktok/bluesky/threads) |
| `BRIEF` | The content brief or topic summary |
| `VOICE_SUMMARY` | Condensed brand voice: personality + tone + avoid words |
| `PILLAR` | Content pillar (e.g., education/trust/product/community) |
| `CHAR_LIMIT` | Platform character limit |

---

## Prompt

You are writing a social media post for **{{BRAND}}** on **{{PLATFORM}}**.

**Brand Voice:**
{{VOICE_SUMMARY}}

**Content Brief:**
{{BRIEF}}

**Pillar:** {{PILLAR}}
**Character Limit:** {{CHAR_LIMIT}}

---

### What to produce:

Return **exactly three variants** of the post. Each variant has:

```
VARIANT 1
----------
HOOK: <one line, the opening that stops the scroll — no more than 12 words>
BODY: <the main content — facts, story, value, proof>
CTA: <one clear action — comment, share, follow, save, click>
CHAR_COUNT: <total characters including hook + body + CTA>
HOOK_SCORE: <self-score 1-10: pattern interrupt + curiosity + specificity + emotion + shareability>
```

---

### Rules:

1. Hook must interrupt the pattern — no "I want to tell you", no "Did you know", no "Here's how"
2. Body must deliver real value — no filler, no padding, no generic advice
3. CTA must be specific to THIS post, not boilerplate
4. Total character count must be ≤ {{CHAR_LIMIT}}
5. Do NOT use any word in the brand's avoid list: {{VOICE_SUMMARY}}
6. Platform-specific formatting applies:
   - LinkedIn: paragraphs, line breaks for readability, professional register
   - Twitter/X: punchy, no wasted words, thread option if idea is large
   - Instagram: visual cue in first line, hashtags at bottom (5–10 max)
   - TikTok: conversational, hooks that work as spoken text, trending format
   - Bluesky/Threads: direct, community-aware, no corporate tone
7. The voice_score must ≥ 7 to be accepted — write it like you know the brand

---

Choose the best variant and mark it `RECOMMENDED:`.
