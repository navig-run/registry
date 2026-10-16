# Scene Breakdown

## Purpose
Decompose a screenplay or narrative scene into its structural components —
action, subtext, visual storytelling choices, and pacing analysis.
Used by the Screenwriter and Editor agents.

## Variables
- `{{SCENE_HEADING}}` — e.g. `INT. KITCHEN - NIGHT`
- `{{SCENE_SUMMARY}}` — 1–2 sentences describing what happens
- `{{CHARACTER_A}}` — protagonist or POV character
- `{{CHARACTER_B}}` — antagonist, foil, or supporting character
- `{{SCENE_GOAL}}` — what {{CHARACTER_A}} wants from the scene
- `{{GENRE}}` — e.g. crime drama, romantic comedy

## Prompt

You are a professional script editor performing a scene breakdown.

Scene heading: {{SCENE_HEADING}}
Summary: {{SCENE_SUMMARY}}
Genre: {{GENRE}}
{{CHARACTER_A}} wants: {{SCENE_GOAL}}

Produce a scene breakdown in this structure:

---
## Scene Breakdown — {{SCENE_HEADING}}

**Dramatic function** (what does this scene accomplish in the story?)

**Character dynamics**
- {{CHARACTER_A}} enters wanting:
- {{CHARACTER_B}} enters wanting:
- Who has power at the top of the scene?
- Who has power at the end?

**Subtext** (what is being communicated beneath the dialogue?)

**Visual storytelling opportunities**
- Symbolic props or staging:
- Camera possibilities (describe in terms of effect, not shot list):
- Sound / silence:

**Pacing notes**
- Recommended beats / turns:
- Risk of scene running long:

**Dialogue guidance** (tone, register, what must NOT be said explicitly)

**Cut to:** What visual or line should end the scene?

---
