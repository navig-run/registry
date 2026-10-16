# Distribution Guide

> Multi-platform publishing, RSS feed management, and analytics tracking.

## Platform Overview

| Platform | RSS Required | Manual Upload | Revenue Share | Analytics |
|----------|-------------|---------------|---------------|-----------|
| Apple Podcasts | ✅ | ❌ | Apple Subs | ✅ Basic |
| Spotify | ✅ (or Spotify for Podcasters) | ✅ | Spotify Ads | ✅ Good |
| YouTube Podcasts | ✅ | ✅ | AdSense | ✅ Excellent |
| Google Podcasts | ✅ | ❌ | None | ✅ Basic |
| Amazon Music | ✅ | ❌ | None | ✅ Basic |
| Pocket Casts | ✅ | ❌ | None | ❌ |
| Overcast | ✅ | ❌ | None | ❌ |

## RSS Feed

### Feed Structure
The RSS feed is the single source of truth for podcast distribution. Every platform reads from it.

Use the `rss-generate` skill to build and validate your feed.

### Required Feed Elements
```xml
<channel>
  <title>Show Name</title>
  <link>https://yoursite.com</link>
  <description>Show description</description>
  <language>en</language>
  <itunes:author>Host Name</itunes:author>
  <itunes:image href="https://yoursite.com/artwork.jpg"/>
  <itunes:category text="Technology"/>
  <itunes:explicit>false</itunes:explicit>
</channel>
```

### Per-Episode Elements
```xml
<item>
  <title>Episode Title</title>
  <description>Episode description</description>
  <enclosure url="https://cdn.example.com/ep001.mp3"
             length="45000000" type="audio/mpeg"/>
  <pubDate>Tue, 15 Jan 2025 06:00:00 +0000</pubDate>
  <itunes:duration>00:45:12</itunes:duration>
  <itunes:episode>1</itunes:episode>
  <itunes:season>1</itunes:season>
  <guid isPermaLink="false">unique-episode-id</guid>
</item>
```

### Feed Validation
- Validate with `xmllint` (automated via `rss-generate` skill)
- Test with [Podbase Validator](https://podba.se/validate/)
- Check Apple requirements: artwork 3000x3000 px, JPEG or PNG

### Feed Hosting Options
| Option | Pros | Cons |
|--------|------|------|
| Self-hosted | Full control | Bandwidth costs, maintenance |
| Buzzsprout | Easy, analytics | Monthly cost |
| Podbean | Unlimited storage | Limited free tier |
| Anchor/Spotify | Free | Platform lock-in risk |
| GitHub Pages | Free, version control | No analytics built-in |

## Publishing Workflow

### Pre-Publish Checklist
- [ ] Audio file exported as MP3 192 kbps CBR
- [ ] Loudness normalised to -16 LUFS
- [ ] ID3 tags filled (title, artist, album art)
- [ ] Show notes written and reviewed
- [ ] Transcript file generated
- [ ] Episode artwork prepared (if episode-specific)
- [ ] RSS feed updated and validated

### Scheduling
- Default: **Tuesday 06:00 UTC**
- Consistency matters more than the specific day
- Announce schedule changes to audience in advance

### Episode Numbering
Format: `S01E01` or sequential `#001`
- Use seasons if you have themed content arcs
- Use sequential numbers for ongoing shows
- Always include in RSS feed metadata

## Analytics

### Key Metrics
| Metric | What It Tells You | Target |
|--------|-------------------|--------|
| Downloads (7-day) | Episode reach | Growing month-over-month |
| Unique listeners | Actual audience size | 60-70% of downloads |
| Completion rate | Content quality | > 70% |
| Drop-off point | Where people leave | Note patterns |
| Subscriber growth | Long-term health | 5-10% monthly growth |
| Reviews/ratings | Discoverability | 1+ per week |

### Platform-Specific Analytics
- **Apple Podcasts Connect**: Listeners, followers, episode performance
- **Spotify for Podcasters**: Streams, demographics, starts vs completions
- **YouTube Studio**: Watch time, audience retention, CTR on thumbnails

### Monthly Analytics Review
Use the `monthly-review` workflow to automatically:
1. Pull analytics from all platforms
2. Generate episode performance comparison
3. Summarise audience feedback
4. Identify growth trends
5. Output a monthly report

## Social Distribution

### Clips Per Episode
Target **3 clips** per episode for social promotion:
1. **Teaser clip** (15-30s) — publish 24h before episode drops
2. **Best moment clip** (30-60s) — publish same day as episode
3. **Quote card clip** (15s) — publish 2-3 days after

### Cross-Promotion
- Appear on other podcasts in your niche
- Guest swap: "I'll be on yours, you be on mine"
- Share episodes in relevant communities and newsletters

## Monetisation

| Method | Audience Size Needed | Revenue Potential |
|--------|---------------------|-------------------|
| Sponsorships | 1,000+ downloads/ep | $$$ |
| Listener support (Patreon) | 500+ engaged fans | $$ |
| Premium content | 200+ superfans | $$ |
| Affiliate links | Any | $ |
| Live events/workshops | 1,000+ engaged | $$$ |
| Merchandise | 500+ brand fans | $ |

## Related
- [Podcasting Guide](podcasting-guide.md) — Full production workflow
- [Audio Setup](audio-setup.md) — Export settings and format specs
- [Agent Guide](agent-guide.md) — publisher agent details
