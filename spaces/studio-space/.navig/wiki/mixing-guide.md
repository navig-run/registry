# Mixing Guide

> Signal flow, techniques, and best practices for mixing in the studio space.

## Signal Flow

```
Source → Insert FX → Channel Fader → Bus → Master Bus → Output
```

## Gain Staging

1. Set all faders to unity (0 dB)
2. Adjust input gain so peaks hover around -18 to -12 dBFS
3. Leave 6 dB headroom on the master bus before mastering

## EQ Principles

| Technique | When to Use |
|-----------|-------------|
| High-pass filter | On everything except kick and bass |
| Subtractive EQ | Remove mud (200–400 Hz) and harshness (2–5 kHz) |
| Additive EQ | Enhance presence (3 kHz), air (12 kHz+) sparingly |
| Dynamic EQ | Tame resonances that only appear on loud notes |

## Compression

| Element | Ratio | Attack | Release | Notes |
|---------|-------|--------|---------|-------|
| Vocals | 3:1–4:1 | 5–15 ms | Auto | Consistent level |
| Drums (bus) | 2:1–4:1 | 10–30 ms | Release to groove | Glue, not squash |
| Bass | 4:1–6:1 | 10–20 ms | 50–100 ms | Control peaks |
| Mix bus | 1.5:1–2:1 | 20–30 ms | Auto | Gently, 1–3 dB GR |

## Panning

- **Center**: kick, snare, bass, lead vocal
- **Slightly off-center**: rhythm guitar, keys, backing vocals
- **Wide**: stereo pads, doubled guitars, effects returns
- **Hard pan**: only with paired elements (L/R guitars)

## Reverb & Delay

- Short reverb (plate) for intimacy
- Long reverb (hall) for depth — keep it behind the source
- Delay synced to BPM (1/8, 1/4, dotted) for rhythmic interest
- High-pass the reverb return at 200–400 Hz to avoid mud

## Automation

Automate these for a dynamic mix:
- Vocal level (phrase by phrase)
- Effect sends (more reverb in chorus, less in verse)
- Filter sweeps on synths
- Master fader for section transitions

## Quality Checks

- [ ] Mono compatibility (collapse to mono, check for cancellation)
- [ ] Low-end clarity (solo sub, check phase between kick and bass)
- [ ] Vocal intelligibility (can you understand every word?)
- [ ] Reference comparison at matched loudness

## Related

- [[production-workflow]] — Full pipeline overview
- [[mastering-reference]] — Preparing for mastering
