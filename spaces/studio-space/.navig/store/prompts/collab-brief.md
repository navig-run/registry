# Collaboration Brief

## Purpose

Generate a clear collaboration brief to share with external producers, vocalists, or musicians. Includes project context, deliverable specs, and timeline.

## Variables

- `{{PROJECT_NAME}}` — Project or track name
- `{{COLLABORATOR}}` — Name of the collaborator
- `{{ROLE}}` — Their role (vocalist, guitarist, co-producer, etc.)
- `{{DEADLINE}}` — Deliverable deadline (YYYY-MM-DD)
- `{{BPM}}` — Track tempo
- `{{KEY}}` — Track key
- `{{GENRE}}` — Genre/style

## Prompt

You are drafting a collaboration brief for **{{COLLABORATOR}}** ({{ROLE}}) on the project **{{PROJECT_NAME}}**.

### Project Overview

- **Track**: {{PROJECT_NAME}}
- **Genre**: {{GENRE}}
- **BPM**: {{BPM}}
- **Key**: {{KEY}}

### What We Need

Describe clearly what the collaborator should deliver:
- File format and quality (e.g., WAV 24-bit 44.1kHz, dry, no processing)
- Specific parts needed (e.g., "lead vocal for chorus," "guitar solo 8 bars")
- Creative direction and reference material

### Deliverables

| Item | Format | Notes |
|------|--------|-------|
| | WAV 24-bit 44.1kHz | |
| | | |

### Timeline

- **Stems/references sent**: (today's date)
- **First draft due**: {{DEADLINE}}
- **Revisions window**: 5 business days after feedback
- **Final deadline**: (calculate from above)

### Technical Requirements

- Sample rate: 44.1kHz (must match project)
- Bit depth: 24-bit minimum
- Dry recordings preferred (no reverb/delay unless creative choice)
- Name files: `{{PROJECT_NAME}}_{{ROLE}}_v1.wav`

### Files Included

List the stems, references, and guide tracks being shared.
