# Agent Guide

> Complete reference for all 5 broadcast-space agents, their formations, and usage.

## Agent Overview

| Agent | Role | Formation | Inbox | Escalates To |
|-------|------|-----------|-------|-------------|
| **host** | Show Host & Creative Lead | episode-production | #episodes | operator |
| **sound-engineer** | Audio Engineer | episode-production | #audio | host |
| **show-planner** | Content Planner & Researcher | guest-booking | #planning | host |
| **publisher** | Distribution & RSS Manager | episode-production | #publishing | host |
| **community-manager** | Audience & Guest Relations | audience-feedback | #community | host |

## Agent Details

### Host
The creative lead and on-air talent. Drives editorial decisions, conducts interviews, and approves final episode output.

**Capabilities:**
- Episode concept development and briefing
- Interview conduction and guest rapport
- Editorial direction and content approval
- Live show hosting and audience interaction
- Season planning and content strategy

**When to invoke:**
- Starting a new episode from concept
- Making editorial decisions (topic angle, guest fit)
- Live show hosting
- Final approval on any episode before publish

**Key skills used:** audio-record, show-notes-write, clip-extract

---

### Sound Engineer
Handles all audio processing from raw recording to distribution-ready master.

**Capabilities:**
- Audio recording setup and monitoring
- Noise reduction and cleanup
- Loudness normalisation and mastering
- Audio editing (trimming, silence removal)
- Clip extraction with transitions

**When to invoke:**
- Processing a raw recording into edited audio
- Fixing audio quality issues
- Extracting clips for social media
- Setting up recording equipment
- Mastering for multi-platform distribution

**Key skills used:** audio-record, audio-edit, noise-reduce, loudness-normalize, clip-extract

---

### Show Planner
Content strategist and researcher. Manages the episode calendar, researches guests, and prepares interview materials.

**Capabilities:**
- Guest research and background analysis
- Episode scheduling and calendar management
- Content ideation and trend research
- Interview question preparation
- Season and series planning

**When to invoke:**
- Planning the next episode or season
- Researching a potential guest
- Scheduling recordings
- Generating interview prep materials

**Key skills used:** guest-research, episode-schedule, show-notes-write

---

### Publisher
Manages the technical distribution pipeline — RSS feed, platform uploads, and analytics tracking.

**Capabilities:**
- RSS feed generation and validation
- Multi-platform episode distribution
- Episode metadata and tagging
- Analytics collection and reporting
- Feed maintenance and troubleshooting

**When to invoke:**
- Publishing a finished episode
- Updating or fixing the RSS feed
- Checking analytics across platforms
- Troubleshooting distribution issues

**Key skills used:** rss-generate, episode-schedule, loudness-normalize

---

### Community Manager
Manages audience relationships, guest outreach, and listener engagement.

**Capabilities:**
- Guest outreach and follow-up
- Audience survey design and collection
- Social media promotion scripting
- Listener feedback aggregation
- Community building and engagement

**When to invoke:**
- Reaching out to potential guests
- Collecting and summarising listener feedback
- Creating promotional content for episodes
- Managing post-recording guest follow-up

**Key skills used:** guest-research, show-notes-write

## Formations

### episode-production
Full production pipeline from recording to publish.
- **Lead:** host
- **Team:** All 5 agents
- **Trigger:** New episode recording ready
- **Skills:** audio-record, audio-edit, noise-reduce, loudness-normalize, transcript-generate, show-notes-write, clip-extract

### guest-booking
Guest research, outreach, and interview preparation.
- **Lead:** show-planner
- **Team:** host, community-manager
- **Trigger:** New guest needed or guest confirmed
- **Skills:** guest-research, episode-schedule, show-notes-write

### live-session
Real-time live streaming with audience interaction.
- **Lead:** host
- **Team:** sound-engineer, community-manager, publisher
- **Trigger:** Scheduled live show
- **Skills:** audio-record, noise-reduce, clip-extract, loudness-normalize

### content-repurpose
Transform episodes into social clips, transcripts, and derivative content.
- **Lead:** sound-engineer
- **Team:** host, publisher, community-manager
- **Trigger:** Episode published
- **Skills:** clip-extract, audio-edit, loudness-normalize, transcript-generate, show-notes-write, episode-schedule

### audience-feedback
Collect, analyse, and act on listener feedback.
- **Lead:** community-manager
- **Team:** host, show-planner
- **Trigger:** Monthly review or survey response
- **Skills:** guest-research, show-notes-write

## Common Workflows

| Task | Trigger | Formation | Agents Involved |
|------|---------|-----------|-----------------|
| Produce an episode | "Record episode on X" | episode-production | All 5 |
| Book a guest | "Find a guest for topic X" | guest-booking | show-planner, host, community-manager |
| Go live | "Start live show" | live-session | host, sound-engineer, community-manager, publisher |
| Repurpose content | "Create clips from ep X" | content-repurpose | sound-engineer, host, publisher, community-manager |
| Monthly review | Cron (1st of month) | audience-feedback | community-manager, host, show-planner |

## Tips
- Always start with the **host** agent for new episode concepts
- The **sound-engineer** should process audio before anyone else touches the file
- Let the **show-planner** handle scheduling conflicts
- The **publisher** handles all platform-specific formatting
- The **community-manager** owns the guest relationship lifecycle
