# Master Checklist

## Purpose

Pre-mastering and post-mastering quality assurance checklist. Ensures every release meets technical standards before distribution.

## Variables

- `{{TRACK_TITLE}}` — Track name
- `{{TARGET_LUFS}}` — Target integrated loudness (e.g., -14 LUFS for streaming)
- `{{TRUE_PEAK_MAX}}` — Maximum true peak (e.g., -1.0 dBTP)
- `{{FORMATS}}` — Required output formats (e.g., WAV 24-bit, FLAC, MP3 320k)

## Prompt

You are performing the mastering QA check for **{{TRACK_TITLE}}**.

### Pre-Mastering Checks

- [ ] Mix approved by producer (sign-off in session notes)
- [ ] No clipping on any individual bus
- [ ] Sufficient headroom (peak below -3 dBFS)
- [ ] Stereo phase correlation above +0.3
- [ ] No unwanted silence, clicks, or artifacts at start/end
- [ ] Fade-in/out applied if needed

### Mastering Targets

| Parameter | Target | Actual | Pass |
|-----------|--------|--------|------|
| Integrated loudness | {{TARGET_LUFS}} LUFS ±0.5 | | |
| True peak | ≤ {{TRUE_PEAK_MAX}} dBTP | | |
| Loudness range | 6–12 LU (genre-dependent) | | |
| Stereo correlation | > +0.3 | | |

### Post-Mastering Checks

- [ ] A/B compare with reference tracks
- [ ] Listen on multiple systems (headphones, monitors, phone, car)
- [ ] Check mono fold-down for streaming
- [ ] Verify no new artifacts introduced
- [ ] Export all required formats: {{FORMATS}}
- [ ] Embed metadata (title, artist, ISRC, artwork)
- [ ] Checksums generated for delivery files

### Sign-Off

- [ ] Master approved → proceed to release-cycle workflow
