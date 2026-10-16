# Interview Brief

## Purpose
Prepare a journalist for an interview by generating a structured brief —
background, key questions, and follow-up probes — based on the subject and angle.

## Variables
- `{{SUBJECT_NAME}}` — person being interviewed
- `{{SUBJECT_ROLE}}` — title / position / context
- `{{STORY_ANGLE}}` — the specific angle or thesis of the story
- `{{PUBLICATION_OUTLET}}` — where the piece will run
- `{{INTERVIEW_FORMAT}}` — email / phone / in-person / recorded video
- `{{SENSITIVE_AREAS}}` — topics to handle carefully or avoid (or "none")

## Prompt

You are a senior journalist preparing for an interview.

Subject: {{SUBJECT_NAME}} ({{SUBJECT_ROLE}})
Angle: {{STORY_ANGLE}}
Outlet: {{PUBLICATION_OUTLET}}
Format: {{INTERVIEW_FORMAT}}
Sensitive areas: {{SENSITIVE_AREAS}}

Produce an interview brief in this format:

---
## Interview Brief — {{SUBJECT_NAME}}

**Story angle:** {{STORY_ANGLE}}

**Background summary** (3–4 sentences: who they are, why they matter to this story)

### Must-ask questions (5)
1.
2.
3.
4.
5.

### Follow-up probes (for each must-ask)
- Question 1 follow-ups:
- Question 2 follow-ups:
[...]

### Soft-close question
(An open question that lets the subject say anything they want to add)

### Notes on sensitive areas
{{SENSITIVE_AREAS}} — suggested framing if these topics arise

---

Questions must be open-ended and non-leading.
Flag any question that touches {{SENSITIVE_AREAS}} with ⚠️.
