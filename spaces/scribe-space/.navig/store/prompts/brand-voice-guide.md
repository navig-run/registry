# Brand Voice Guide

## Purpose
Generate a brand voice and style guide for a publication, product, or persona.
Provides tone-of-voice rules, vocabulary, and do/don't examples.

## Variables
- `{{BRAND_NAME}}` — name of the brand, publication, or product
- `{{AUDIENCE}}` — who the audience is (demographics, expertise level)
- `{{BRAND_PERSONALITY}}` — 3–5 adjectives (e.g. "sharp, witty, authoritative")
- `{{BRAND_MISSION}}` — 1-sentence mission or value proposition
- `{{COMPETITORS}}` — 1–3 brands to differentiate from (or "none")
- `{{OFF_LIMITS}}` — topics, words, or styles to avoid

## Prompt

You are a senior brand strategist and editorial director.

Brand: {{BRAND_NAME}}
Audience: {{AUDIENCE}}
Personality: {{BRAND_PERSONALITY}}
Mission: {{BRAND_MISSION}}
Differentiate from: {{COMPETITORS}}
Off-limits: {{OFF_LIMITS}}

Produce a brand voice guide in this format:

---
## Brand Voice Guide — {{BRAND_NAME}}

### Who we are
(2–3 sentences on brand identity and mission)

### Our audience
(Who they are, what they know, what they care about)

### Voice pillars
For each adjective in {{BRAND_PERSONALITY}}:
- **[Adjective]**: What it means for us | In practice | ✅ Do | ❌ Don't

### Vocabulary
**Words we use:**
**Words we avoid:**
**Jargon policy:**

### Tone by context
| Context | Tone | Example phrase |
|---------|------|----------------|
| Headlines | | |
| Error messages | | |
| Social posts | | |
| Long-form articles | | |

### Sentence structure
- Sentence length target:
- Active vs. passive:
- Reading level target (Flesch-Kincaid):

### Punctuation & formatting
(Oxford comma, em dash usage, capitalisation, etc.)

---
