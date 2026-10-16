# Episode Brief

## Purpose
Structure a complete episode plan from concept to production-ready outline.

## Variables
- `{{TOPIC}}` — Episode topic or theme
- `{{GUEST_NAME}}` — Guest name (if interview format)
- `{{FORMAT}}` — Episode format (solo, interview, panel, Q&A)
- `{{TARGET_DURATION}}` — Target duration in minutes
- `{{EPISODE_NUMBER}}` — Episode number
- `{{SERIES}}` — Series or season name (if applicable)

## Prompt

You are planning **Episode {{EPISODE_NUMBER}}** of a podcast.

**Topic**: {{TOPIC}}
**Format**: {{FORMAT}}
**Target Duration**: {{TARGET_DURATION}} minutes
**Guest**: {{GUEST_NAME}}
**Series**: {{SERIES}}

Generate a complete episode brief with these sections:

### 1. Episode Summary
- One-paragraph description suitable for show notes
- Key takeaway for the listener

### 2. Cold Open / Hook
- Opening 30-second hook to grab attention
- Tease the most compelling insight

### 3. Segment Outline
For each segment, provide:
| Segment | Duration | Content | Transition |
|---------|----------|---------|------------|

### 4. Key Questions (if interview)
- 10-15 questions ordered from warm-up to deep-dive
- 2-3 follow-up prompts per key question
- 1 unexpected/fun question

### 5. Talking Points (if solo)
- Main arguments or insights
- Supporting data or examples
- Personal stories or anecdotes

### 6. Resources to Mention
- Books, tools, links to reference during episode
- Guest's work to highlight

### 7. Call to Action
- Primary CTA (subscribe, review, visit link)
- Secondary CTA (join community, check guest's work)

### 8. Production Notes
- Required audio (intro, outro, ad reads)
- Sound effects or music cues
- Technical setup notes
