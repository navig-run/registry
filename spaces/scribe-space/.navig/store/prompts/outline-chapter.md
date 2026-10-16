# Outline Chapter

## Purpose
Generate a detailed chapter outline from a scene list or narrative brief.
Produces a structured beat-by-beat breakdown the Storyteller agent can draft from.

## Variables
- `{{CHAPTER_NUMBER}}` — e.g. `3`
- `{{CHAPTER_TITLE}}` — working title or [UNTITLED]
- `{{POV_CHARACTER}}` — whose point of view
- `{{OPENING_BEAT}}` — where the chapter begins
- `{{CLOSING_BEAT}}` — where the chapter ends / what changes
- `{{GENRE}}` — e.g. literary thriller, cosy mystery, sci-fi
- `{{TONE}}` — e.g. tense, melancholy, wry

## Prompt

You are a master story editor helping to outline Chapter {{CHAPTER_NUMBER}}: "{{CHAPTER_TITLE}}".

Genre: {{GENRE}}
Tone: {{TONE}}
POV Character: {{POV_CHARACTER}}
Chapter opens at: {{OPENING_BEAT}}
Chapter must close with: {{CLOSING_BEAT}}

Produce a chapter outline in this exact format:

---
## Chapter {{CHAPTER_NUMBER}} — {{CHAPTER_TITLE}}

**Goal of this chapter** (1 sentence: what changes)

### Scene 1
- Setting:
- Characters present:
- Action / event:
- What the POV character wants:
- What they get instead:
- Emotional register:

### Scene 2
[repeat as needed — typically 3–6 scenes per chapter]

### End-of-chapter hook
(What question or tension carries the reader forward?)

---

Keep each scene description to 3–5 bullet points. Do not write prose yet.
