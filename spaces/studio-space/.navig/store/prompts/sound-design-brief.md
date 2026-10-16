# Sound Design Brief

## Purpose

Structured prompt for creating new sounds from scratch. Guides through the synthesis/sampling approach, processing chain, and integration into a track.

## Variables

- `{{SOUND_TYPE}}` — What to create (e.g., "bass patch", "pad", "riser", "foley hit")
- `{{GENRE}}` — Target genre for sonic context
- `{{CHARACTER}}` — Descriptive adjective (e.g., "warm", "aggressive", "ethereal", "gritty")
- `{{SYNTH_OR_SAMPLER}}` — Tool to use (e.g., Serum, Vital, Kontakt, field recording)
- `{{BPM}}` — Track tempo for tempo-synced elements

## Prompt

You are designing a new **{{SOUND_TYPE}}** for a **{{GENRE}}** production.

### 1. Sound Profile

- **Type**: {{SOUND_TYPE}}
- **Character**: {{CHARACTER}}
- **Frequency role**: sub / low / mid / high / full-range
- **Dynamic role**: sustain / transient / evolving / one-shot

### 2. Synthesis Approach

Using **{{SYNTH_OR_SAMPLER}}**:
- **Oscillators/Sources**: describe waveforms, sample layers, or recordings
- **Filter**: type (LP/HP/BP), cutoff, resonance, envelope
- **Modulation**: LFO targets, envelope shapes, macro assignments
- **Effects chain**: distortion, chorus, reverb, delay, EQ

### 3. Processing Chain

| Slot | Effect | Settings | Purpose |
|------|--------|----------|---------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |

### 4. Variations

Create 3 variations:
1. **Clean** — minimal processing, suitable for layering
2. **Processed** — full chain applied, mix-ready
3. **Extreme** — pushed to creative limits, experimental

### 5. Export Specs

- Format: WAV 24-bit
- Sample rate: match project (44100 or 48000)
- Naming: `{{SOUND_TYPE}}_{{CHARACTER}}_v1.wav`
- Save preset in synthesiser for recall

### 6. Integration Notes

How this sound fits into the mix — frequency range, panning, dynamics, sidechain relationships.
