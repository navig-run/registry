# Mix Review

## Purpose

Structured prompt for evaluating a mix. Covers frequency balance, dynamics, stereo image, effects usage, and actionable revision notes.

## Variables

- `{{TRACK_TITLE}}` — Name of the track being reviewed
- `{{GENRE}}` — Genre context for reference levels
- `{{MIX_VERSION}}` — Current mix iteration (e.g., "v3")
- `{{TARGET_LOUDNESS}}` — Target LUFS for the platform

## Prompt

You are a mix engineer reviewing **{{TRACK_TITLE}}** ({{GENRE}}, mix {{MIX_VERSION}}).

### 1. First Impression

Listen through once without stopping. Note the overall feeling — does it sound finished, balanced, and genre-appropriate?

### 2. Frequency Analysis

| Band | Range | Assessment | Notes |
|------|-------|------------|-------|
| Sub | 20–60 Hz | | |
| Low | 60–250 Hz | | |
| Low-Mid | 250–800 Hz | | |
| Mid | 800 Hz–3 kHz | | |
| Upper-Mid | 3–6 kHz | | |
| High | 6–12 kHz | | |
| Air | 12–20 kHz | | |

### 3. Dynamics

- **Overall dynamic range**: adequate / too compressed / too dynamic
- **Transient preservation**: drums punchy / soft / over-limited
- **Bus compression**: transparent / noticeable / pumping

### 4. Stereo Image

- **Width**: narrow / balanced / overly wide
- **Center lock**: kick, bass, lead vocal centered? Y/N
- **Mono compatibility**: check and note phase issues

### 5. Effects

- **Reverb**: depth appropriate for genre?
- **Delay**: timing synced to BPM?
- **Saturation/distortion**: tasteful or excessive?

### 6. Loudness

- **Current LUFS**: (measure with loudness-check skill)
- **Target**: {{TARGET_LOUDNESS}} LUFS
- **Headroom**: sufficient for mastering?

### 7. Revision List

Create a numbered list of specific, actionable changes. Prioritise by impact.
