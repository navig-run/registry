# Viral Hook Score Prompt

## Purpose
Score a single post hook on its viral potential across 5 dimensions.
If the hook scores below 7, produce a rewritten version that would score
higher. Every post hook must pass this gate before being marked ready for
scheduling.

---

## Variables

| Variable | Description |
|----------|-------------|
| `HOOK_TEXT` | The opening line(s) of the post — the hook only |
| `PLATFORM` | Target platform (affects format expectations) |
| `BRAND` | Brand slug (for voice alignment check) |
| `AVOID_WORDS` | Brand's forbidden words/phrases (from voice.json) |

---

## Prompt

You are evaluating the viral potential of a hook for **{{BRAND}}** on **{{PLATFORM}}**.

**Hook to evaluate:**
> {{HOOK_TEXT}}

**Brand avoid list:** {{AVOID_WORDS}}

---

### What to produce:

#### HOOK SCORE: X/10

| Dimension | Score (1–2) | What it measures |
|-----------|-------------|-----------------|
| Pattern interrupt | | Does it break the expected scroll pattern? Does it feel different from everything around it? |
| Curiosity gap | | Does it plant a question the reader must answer? Does it create tension without resolving it? |
| Specificity | | Does it contain a concrete detail — a number, a name, a specific scenario — rather than a generic claim? |
| Emotional resonance | | Does it trigger a measurable emotion: surprise, fear, desire, validation, identity, aspiration? |
| Shareability | | Would someone send this to someone else, or post it as a story reaction? Does it feel like "I had to show you this"? |

**Total: X/10**

---

**VERDICT:**
- Score 9–10: 🔥 VIRAL TIER — ship immediately
- Score 7–8: ✅ STRONG — ready to publish
- Score 5–6: ⚠️ WEAK — rewrite required
- Score 1–4: ❌ GENERIC — fully rework the hook concept

---

**If score < 7, provide THREE rewrites:**

```
REWRITE A (boost: pattern interrupt + curiosity):
[Hook rewrite A]

REWRITE B (boost: specificity + emotion):
[Hook rewrite B]

REWRITE C (boost: shareability):
[Hook rewrite C]
```

For each rewrite, predict the new score in parentheses: e.g., `(predicted: 8/10)`

---

### Platform-specific Hook Rules:

| Platform | Hook format |
|----------|-------------|
| Twitter/X | First line is the entire visible preview — one sentence max |
| LinkedIn | First line before "...see more" break — 210 chars max to hit the fold |
| Instagram | First 125 chars show before "more" — front-load the tension |
| TikTok | Hook must work spoken aloud — test it as a verbal opener |
| Bluesky | Conversational, no PR-speak, treat reader as peer |
| Threads | Casual but high-signal — think DM energy, not press release |

---

### Hard Rejections (score = 1 regardless of other dimensions):

- "I want to tell you about..."
- "Did you know that..."
- "Here's everything you need to know about..."
- "I'm excited to announce..."
- Any hook containing a word from the brand avoid list
- Generic calls to engagement: "What do you think?" as the opening line
