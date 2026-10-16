# Thumbnail Playbook

## Core Principles

1. **Readable at small sizes** — Thumbnails appear as small as 116x65px on mobile
2. **Maximum 4 words of text** — If you need more, the concept is too complex
3. **High contrast** — Stand out in the feed against YouTube's white/dark backgrounds
4. **Faces sell** — Human faces with clear emotions increase CTR by 30%+
5. **Consistency** — Recognisable brand style builds trust and click habits

## Composition Rules

| Rule | Why |
|------|-----|
| Rule of thirds | Focal point at intersection points |
| Left-to-right reading | Place key visual on the left, text on the right |
| Clean background | Busy backgrounds reduce text readability |
| Depth/layers | Foreground subject + background creates visual interest |
| Negative space | Empty areas draw attention to the focal point |

## Text Overlay

- **Font**: Bold sans-serif (Impact, Montserrat Black, Bebas Neue)
- **Size**: Large enough to read on mobile
- **Outline/shadow**: Always add stroke or shadow for contrast
- **Colour**: High contrast against background (white on dark, yellow on blue)
- **Position**: Top or bottom third, never centre (gets obscured by timestamp)

## Colour Strategy

| Combination | Effect | Best For |
|-------------|--------|----------|
| Yellow + Black | Urgency, warning | Lists, tips |
| Blue + White | Trust, calm | Tutorials |
| Red + White | Energy, excitement | Reviews, reactions |
| Green + White | Growth, money | Business, investing |
| Purple + Gold | Premium, creative | Art, design |

## A/B Testing Process

1. Create 2-3 variants with distinct visual approaches
2. Score each variant using `thumbnail-score` skill
3. Select top performer based on contrast, readability, and emotion
4. After publishing, review CTR at 48 hours
5. If CTR below 5%, swap to the alternative variant
6. Document what works in the style guide

## Technical Specs

- **Resolution**: 1280x720 pixels (16:9 ratio)
- **Max file size**: 2 MB
- **Format**: PNG (preferred) or JPG
- **Colour space**: sRGB
- **Safe zone**: Keep key elements away from bottom-right (video duration overlay)
