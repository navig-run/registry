# Podcasting Guide

> End-to-end reference for planning, recording, editing, and publishing podcast episodes.

## Episode Lifecycle

```
Concept → Brief → Guest Prep → Record → Edit → Master → Show Notes → Publish → Promote
```

## 1. Pre-Production

### Episode Planning
- Define the topic, angle, and target audience takeaway
- Choose format: solo, interview, panel, Q&A, or narrative
- Use `episode-brief.md` prompt to generate a structured plan
- Schedule recording at least 1 week before publish date

### Guest Preparation (if interview)
- Research guest background using `guest-research` skill
- Generate interview questions with `interview-questions.md` prompt
- Send guest a pre-interview brief:
  - Episode topic and angle
  - Expected duration (default: 45 minutes)
  - Technical requirements (mic, quiet room, wired internet)
  - Recording platform link

## 2. Recording

### Technical Setup
- Sample rate: **48 kHz** (professional standard)
- Bit depth: **24-bit** (headroom for post-processing)
- Format: **WAV** (lossless for editing)
- Channels: **Stereo** (or dual-mono for interview)

### Recording Best Practices
- Record a 10-second room tone sample before starting
- Leave 3 seconds of silence at the start and end
- Clap or use a slate for sync reference in multi-track sessions
- Monitor levels: target **-12 dB** peaks, never clip
- Record backup on a second device when possible

### Remote Interviews
- Use Riverside, SquadCast, or Zencastr for local recording per participant
- Zoom is acceptable but quality is lower (compressed audio)
- Always request separate audio tracks per guest

## 3. Post-Production

### Editing Workflow
1. **Import** all tracks into DAW
2. **Sync** tracks if multi-source recording
3. **Trim** top and tail silence
4. **Remove** filler words, long pauses, mistakes (use `audio-edit` skill)
5. **Reduce noise** with `noise-reduce` skill (afftdn filter)
6. **Normalize loudness** to platform targets:
   - Podcast: **-16 LUFS** (Apple, Spotify standard)
   - YouTube: **-14 LUFS**
7. **Add** intro music (15s), outro (20s), ad reads
8. **Export** master file

### Quality Checklist
- [ ] Noise floor below **-60 dB**
- [ ] Loudness normalised to **-16 LUFS**
- [ ] No clipping or distortion
- [ ] Intro and outro present and timed
- [ ] Show notes and transcript generated
- [ ] Episode metadata filled (title, description, tags)

## 4. Publishing

### File Export
- Distribution format: **MP3 192 kbps** (CBR for compatibility)
- Include ID3 tags: title, artist, album (show name), episode number, artwork
- Filename convention: `episode-NNN-slug.mp3`

### Schedule
- Default publish day: **Tuesday at 06:00 UTC**
- Time zone consideration: schedule for audience's morning commute
- Minimum 3 clips per episode for social promotion

## 5. Formats Reference

| Format | Duration | Best For | Prep Time |
|--------|----------|----------|-----------|
| Solo | 15-30 min | Deep expertise, opinion | Low |
| Interview | 30-60 min | Guest expertise, stories | Medium |
| Panel | 45-90 min | Debate, multiple views | High |
| Q&A | 20-40 min | Audience engagement | Low |
| Narrative | 20-45 min | Storytelling, documentary | Very High |

## Related
- [Audio Setup](audio-setup.md) — Recording gear and processing chain
- [Guest Management](guest-management.md) — Guest pipeline details
- [Distribution Guide](distribution-guide.md) — Platform publishing specifics
