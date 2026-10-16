# Live Streaming

> Setup, platforms, and best practices for live podcast episodes and streaming shows.

## Platform Comparison

| Platform | Max Duration | Audio Quality | Chat | Clips | Monetisation |
|----------|-------------|---------------|------|-------|-------------|
| YouTube Live | Unlimited | AAC 128k | ✅ | ✅ | Super Chat, memberships |
| Twitch | 48 hours | AAC 160k | ✅ | ✅ | Subs, bits |
| Twitter/X Spaces | Unlimited | Variable | ✅ | ❌ | Tickets |
| LinkedIn Live | 4 hours | AAC 128k | ✅ | ❌ | None |
| Spotify Live | Unlimited | Variable | ✅ | ❌ | None |

## Pre-Show Checklist

### Technical
- [ ] Test audio input and output (48 kHz / 24-bit)
- [ ] Verify internet upload speed (minimum 5 Mbps, 10+ recommended)
- [ ] Close unnecessary applications (CPU/RAM headroom)
- [ ] Set up backup recording (local recording alongside stream)
- [ ] Test stream key and platform connection
- [ ] Prepare scenes/layouts in OBS or streaming software

### Content
- [ ] Episode brief reviewed and accessible
- [ ] Guest connected and audio-tested (15 min before)
- [ ] Chat moderation set up (bot or human moderator)
- [ ] Scheduled start time announced on social media
- [ ] Overlay graphics loaded (lower thirds, logos, alerts)

## Streaming Software

### OBS Studio (Recommended)
- Free, open source, cross-platform
- Audio filters: noise suppression, compressor, limiter
- Scene switching for different show segments

**Recommended OBS Audio Settings:**
```
Sample Rate: 48 kHz
Channels: Stereo
Audio Bitrate: 160 kbps (Twitch) / 128 kbps (YouTube)
Noise Suppression: RNNoise
Compressor: Ratio 3:1, Threshold -18 dB
Limiter: -1 dB ceiling
```

### Riverside / StreamYard
- Browser-based, no software install needed
- Records local quality per participant
- Built-in multi-stream to YouTube + LinkedIn + Facebook
- Best for remote guests who aren't tech-savvy

## Live Show Structure

### Timeline Template
```
-15:00  Guest arrives, sound check
-05:00  Final prep, "going live in 5"
 00:00  Go live — energy opener, welcome viewers
 02:00  Introduce topic and guest
 05:00  Main discussion begins
 20:00  Mid-show chat check — read questions
 35:00  Deep-dive or debate segment
 45:00  Lightning round / rapid fire
 50:00  Closing thoughts, CTAs
 52:00  Sign off, keep chat open 5 min
 57:00  End stream
```

### Engagement Techniques
- **Greet viewers by name** when they join
- **Pose questions** to chat every 10-15 minutes
- **React to comments** — acknowledge disagreement respectfully
- **Run polls** for topic direction or opinions
- **Tease upcoming content** to keep viewers watching

## Post-Stream Workflow

1. **Download** the full recording from platform or local backup
2. **Extract clips** using `clip-extract` skill (3-5 best moments)
3. **Noise reduce** and **normalise** the full recording
4. **Generate transcript** for accessibility
5. **Write show notes** using the `show-notes.md` prompt
6. **Publish** as a regular podcast episode (edited version)
7. **Distribute clips** to social platforms

## Multi-Streaming

Streaming to multiple platforms simultaneously:
- Use **Restream.io** or **OBS + multiple RTMP outputs**
- Be aware of platform exclusivity rules (Twitch affiliates/partners)
- Adapt chat interaction — use a combined chat tool

## Audio Quality for Streams

Live audio targets differ from edited podcasts:
| Parameter | Live Target | Edited Target |
|-----------|------------|---------------|
| Loudness | -14 to -16 LUFS | -16 LUFS |
| Noise floor | < -50 dB | < -60 dB |
| Compression | More aggressive | Gentle |
| Limiter | -1 dB hard | -1 dB true peak |

## Related
- [Podcasting Guide](podcasting-guide.md) — Full production workflow
- [Audio Setup](audio-setup.md) — Hardware and processing chain
- [Agent Guide](agent-guide.md) — Agents involved in live sessions
