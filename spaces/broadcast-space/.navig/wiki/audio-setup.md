# Audio Setup

> Recording equipment, processing chain, and technical standards for broadcast-quality audio.

## Audio Standards

| Parameter | Recording | Distribution |
|-----------|-----------|-------------|
| Sample Rate | 48 kHz | 48 kHz |
| Bit Depth | 24-bit | 16-bit (MP3) |
| Format | WAV | MP3 192 kbps CBR |
| Channels | Stereo / Dual Mono | Stereo |
| Loudness | -12 dB peaks | -16 LUFS (podcast) |
| Noise Floor | < -60 dB | < -60 dB |
| True Peak | — | -1 dB TP |

## Equipment Tiers

### Starter (~$100-200)
| Item | Recommendation | Why |
|------|---------------|-----|
| Microphone | Audio-Technica ATR2100x-USB | USB + XLR dual connectivity |
| Headphones | Sony MDR-7506 | Flat response, industry standard |
| Pop filter | Any dual-mesh | Reduces plosives |
| Boom arm | Any desk clamp | Consistent mic positioning |

### Professional (~$500-1000)
| Item | Recommendation | Why |
|------|---------------|-----|
| Microphone | Shure SM7B / Rode PodMic | Broadcast standard dynamic mics |
| Interface | Focusrite Scarlett 2i2 | Clean preamps, low latency |
| Headphones | Beyerdynamic DT 770 Pro | Closed-back, accurate monitoring |
| Acoustic treatment | Foam panels + bass traps | Room reflections control |
| Boom arm | Rode PSA1+ | Heavy-duty, smooth movement |

### Studio (~$2000+)
| Item | Recommendation | Why |
|------|---------------|-----|
| Microphone | Neumann U87 / Sennheiser MKH 416 | Reference condenser/shotgun |
| Interface | Universal Audio Apollo Twin | Built-in DSP processing |
| Preamp | dbx 286s | Dedicated channel strip |
| Monitoring | Genelec 8010A (pair) | Reference monitors |
| Room | Full acoustic treatment | Professional studio quality |

## Recording Environment

### Room Treatment Priority
1. **Behind the speaker** — absorb first reflections
2. **Opposite wall** — prevent standing waves
3. **Ceiling** — reduce flutter echo
4. **Corners** — bass traps for low-frequency control

### Quick Fixes (No Budget)
- Record in a closet full of clothes (natural absorption)
- Hang blankets on walls behind and in front
- Use a reflection filter behind the microphone
- Avoid rooms with hard parallel walls

### Noise Control
- Close windows and doors
- Turn off fans, AC, appliances
- Disable desktop notifications (click sounds)
- Use a noise gate or noise reduction in post

## Processing Chain

### Signal Flow
```
Microphone → Preamp/Interface → DAW Recording → Edit → Process → Master → Export
```

### Post-Processing Order (Critical)
1. **Noise Reduction** → `noise-reduce` skill (afftdn filter)
   - Light: noise reduction -20
   - Moderate: noise reduction -25
   - Aggressive: noise reduction -30
2. **EQ** → Shape tone, remove rumble
   - High-pass filter at 80 Hz (remove low rumble)
   - Slight presence boost at 3-5 kHz (clarity)
   - De-ess at 6-8 kHz if sibilance present
3. **Compression** → Even out dynamics
   - Ratio: 3:1 to 4:1
   - Threshold: -18 to -24 dB
   - Attack: 10-20 ms
   - Release: 100-200 ms
4. **Loudness Normalisation** → `loudness-normalize` skill
   - Target: -16 LUFS for podcast
   - True peak limit: -1 dB
5. **Limiter** → Catch any remaining peaks
   - Ceiling: -1 dB true peak
   - Fast attack, medium release

### FFmpeg Quick Reference

```bash
# Noise reduction
ffmpeg -i input.wav -af "afftdn=nf=-25" output.wav

# Loudness normalisation
ffmpeg -i input.wav -af loudnorm=I=-16:TP=-1:LRA=11 output.wav

# Measure loudness
ffmpeg -i input.wav -af ebur128 -f null -

# Convert WAV to MP3
ffmpeg -i input.wav -codec:a libmp3lame -b:a 192k output.mp3

# Trim audio
ffmpeg -i input.wav -ss 00:01:30 -to 00:45:00 output.wav

# Extract clip with fade
ffmpeg -i input.wav -ss 00:15:00 -to 00:15:45 -af "afade=in:d=0.5,afade=out:st=44.5:d=0.5" clip.wav
```

## Microphone Technique

### Distance
- Dynamic mics: **2-4 inches** from mouth
- Condenser mics: **6-12 inches** from mouth
- Maintain consistent distance throughout recording

### Positioning
- Speak across the mic, not directly into it (reduces plosives)
- Angle the mic 15-20° off-axis for harsh voices
- Keep the mic at mouth level or slightly below

### Common Problems
| Problem | Cause | Fix |
|---------|-------|-----|
| Popping P/B sounds | Plosives | Pop filter + angle mic |
| Sibilance (harsh S) | Proximity + bright mic | De-esser or move back |
| Room echo | Hard surfaces | Treat room or use dynamic mic |
| Hum/buzz | Electrical interference | Check cables, use balanced XLR |
| Inconsistent volume | Distance variation | Boom arm + discipline |

## Related
- [Podcasting Guide](podcasting-guide.md) — Full production workflow
- [Live Streaming](live-streaming.md) — Live audio considerations
- [Agent Guide](agent-guide.md) — sound-engineer agent details
