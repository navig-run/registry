# Mastering Reference

> Loudness standards, delivery specifications, and mastering best practices.

## Platform Loudness Targets

| Platform | Target LUFS | True Peak Max | Notes |
|----------|-------------|---------------|-------|
| Spotify | -14 LUFS | -1.0 dBTP | Normalises down only |
| Apple Music | -16 LUFS | -1.0 dBTP | Sound Check enabled |
| YouTube | -14 LUFS | -1.0 dBTP | Normalises up and down |
| Tidal | -14 LUFS | -1.0 dBTP | |
| Amazon Music | -14 LUFS | -2.0 dBTP | Conservative peak |
| CD | -9 to -12 LUFS | 0.0 dBTP | Genre-dependent |
| Club/DJ | -6 to -9 LUFS | -0.3 dBTP | Louder for live PA |

## Mastering Chain (Typical Order)

1. **EQ** — Gentle broad strokes (shelf boosts, surgical cuts)
2. **Multiband compression** — Tighten low end, control mids
3. **Stereo enhancement** — Widen highs, keep lows mono
4. **Saturation/tape** — Harmonic warmth (subtle)
5. **Limiter** — Final ceiling, target true peak

## Delivery Formats

| Format | Spec | Use Case |
|--------|------|----------|
| WAV 24-bit 44.1kHz | Lossless, standard | Distribution master |
| WAV 16-bit 44.1kHz | CD-quality | CD replication |
| FLAC 24-bit 44.1kHz | Lossless compressed | Hi-res streaming |
| MP3 320kbps CBR | Lossy | Promo, preview |
| WAV 24-bit 48kHz | Broadcast | Film/TV sync |

## Quality Checks

- [ ] Integrated loudness within 0.5 LU of target
- [ ] True peak below platform maximum
- [ ] Loudness range (LRA) between 6–12 LU
- [ ] No inter-sample peaks (check with ISP-aware meter)
- [ ] Mono fold-down clean (no phase cancellation)
- [ ] Start/end silence: 0.5s leading, clean tail

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Over-limiting (distortion) | Reduce gain into limiter, accept lower LUFS |
| Narrow stereo | Check mid/side balance, widen with subtle enhancement |
| No headroom from mix | Ask mix engineer for -6 dBFS peak version |
| Metadata missing | Run metadata-tag skill before final export |

## Related

- [[mixing-guide]] — Preparing a mix for mastering
- [[release-checklist]] — Post-mastering release steps
