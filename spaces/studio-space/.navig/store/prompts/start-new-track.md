# Start New Track

## Purpose

Structured prompt for beginning a new music production session. Guides the producer through genre selection, reference analysis, BPM/key decisions and initial arrangement planning.

## Variables

- `{{GENRE}}` — Primary genre or subgenre
- `{{BPM}}` — Target tempo (optional, can be "auto-detect from reference")
- `{{KEY}}` — Target musical key (optional)
- `{{REFERENCE_TRACKS}}` — Comma-separated list of reference song titles
- `{{SESSION_NAME}}` — Name for the new session folder
- `{{MOOD}}` — Emotional direction (e.g., energetic, melancholic, chill)

## Prompt

You are a music producer starting a new track. Follow this structured approach:

### 1. Genre & Style
- **Genre**: {{GENRE}}
- **Mood**: {{MOOD}}
- **References**: {{REFERENCE_TRACKS}}

### 2. Musical Foundation

| Attribute | Value |
|-----------|-------|
| BPM | {{BPM}} |
| Key | {{KEY}} |
| Time Signature | 4/4 (adjust if genre demands) |

### 3. Arrangement Blueprint

Outline the song structure — intro, verse, chorus, bridge, outro — with approximate bar counts. Note any genre conventions that apply.

### 4. Sound Palette

List 5–8 core sounds needed: drums, bass, melodic elements, pads, FX. For each, note whether it comes from synthesis, sampling, or live recording.

### 5. Session Setup

Create the session folder `{{SESSION_NAME}}` with subfolders:
- `tracks/` — individual track stems
- `references/` — reference tracks for A/B comparison
- `bounces/` — rough mixes and exports
- `notes/` — production notes and lyrics

### 6. First Actions

List the first 3 concrete tasks to get sound coming out of speakers within 15 minutes.
