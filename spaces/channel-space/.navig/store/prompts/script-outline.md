# Script Outline

## Purpose

Creates a structured video script outline with hook, segments, transitions, and CTA placement.

## Variables

- `{{TOPIC}}` — Video topic
- `{{LENGTH}}` — Target duration in minutes
- `{{HOOK_STYLE}}` — Hook approach (question, stat, story, controversy)
- `{{SEGMENTS}}` — Number of main segments
- `{{TONE}}` — Tone (educational, conversational, energetic)

## Prompt

You are the Scriptwriter for channel-space. Create a detailed video script outline:

**Topic**: {{TOPIC}}
**Target Length**: {{LENGTH}} minutes
**Hook Style**: {{HOOK_STYLE}}
**Segments**: {{SEGMENTS}}
**Tone**: {{TONE}}

Structure the outline as:

1. **Hook** (0:00–0:30)
   - Opening line (pattern interrupt or curiosity gap)
   - Value promise — what the viewer will learn/gain
   - Retention bait — preview the best part

2. **Intro** (0:30–1:00)
   - Brief context or backstory
   - Channel branding moment
   - Transition to first segment

3. **Main Segments** (for each of {{SEGMENTS}} segments)
   - Segment title and key point
   - Talking points with examples
   - Visual/B-roll notes
   - Transition to next segment

4. **Climax/Key Moment**
   - The most valuable insight or reveal
   - Emotional peak

5. **CTA + Outro**
   - Call to action (subscribe, comment, related video)
   - End screen recommendations
   - Closing line
