# Platform Specs

> Technical specifications for TikTok, Instagram Reels, and YouTube Shorts.

## Quick Reference

| Spec | TikTok | Reels | Shorts |
|------|--------|-------|--------|
| **Max Duration** | 10 min (60s optimal) | 90 seconds | 60 seconds |
| **Aspect Ratio** | 9:16 | 9:16 | 9:16 |
| **Resolution** | 1080 x 1920 | 1080 x 1920 | 1080 x 1920 |
| **Max File Size** | 287 MB | 250 MB | 256 MB |
| **Format** | MP4, MOV | MP4, MOV | MP4, MOV |
| **Codec** | H.264 | H.264 | H.264 |
| **Frame Rate** | 30-60fps | 30fps | 30fps |
| **Caption Length** | 4000 chars | 2200 chars | 100 chars (title) |
| **Hashtag Limit** | ~5-8 | ~15-30 | ~3-5 |

## TikTok Specifics

- **Sweet spot**: 15-30 seconds
- **Algorithm favours**: Completion rate, rewatches, shares
- **Trending sounds**: Major distribution boost
- **Text on screen**: Bold, centered, 42pt+
- **Captions**: Short, emoji-forward, trend-aware language
- **Best posting times**: 7am, 12pm, 7pm (local)

## Instagram Reels Specifics

- **Sweet spot**: 15-30 seconds
- **Algorithm favours**: Saves, shares, engagement
- **Original audio**: Helps with Explore discovery
- **Hashtags**: 10-15 recommended, mix broad + niche
- **Cover image**: Choose a clean frame for grid aesthetics
- **Best posting times**: 11am, 1pm, 7pm (local)

## YouTube Shorts Specifics

- **Sweet spot**: 30-60 seconds
- **Algorithm favours**: Click-through rate, watch time
- **Title**: Must be keyword-rich and searchable
- **Hashtags**: Use #Shorts + 2 topic hashtags
- **Thumbnail**: Auto-generated from video, no custom upload
- **Best posting times**: 2pm-4pm (varies by audience)

## Export Settings (FFmpeg)

```bash
# TikTok
ffmpeg -i input.mp4 -vf "scale=1080:1920" -t 60 -c:v libx264 -crf 23 -c:a aac -b:a 128k tiktok.mp4

# Reels
ffmpeg -i input.mp4 -vf "scale=1080:1920" -t 90 -c:v libx264 -crf 23 -c:a aac -b:a 128k reels.mp4

# Shorts
ffmpeg -i input.mp4 -vf "scale=1080:1920" -t 60 -c:v libx264 -crf 23 -c:a aac -b:a 128k shorts.mp4
```

## Caption Text Overlay Settings

| Property | Value |
|----------|-------|
| Font | Montserrat Bold / Inter |
| Size | 42-48pt |
| Colour | #FFFFFF |
| Stroke | #000000, 2px |
| Position | Center, lower third, or top |
| Max words/frame | 8-12 |
