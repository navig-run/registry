# Agent Guide — Channel Space

## Working with Agents

Channel-space provides 5 specialised agents that coordinate through formations. Each agent has a dedicated inbox channel and specific capabilities.

## Agent Reference

### Showrunner

- **Role**: Creative Director — oversees everything
- **When to use**: Video planning, production oversight, quality reviews, content strategy
- **Formation**: `video-production`
- **Inbox**: `#production`
- **Example**: "Plan next week's videos" or "Review the final edit"

### Scriptwriter

- **Role**: Content Writer — scripts, hooks, outlines
- **When to use**: Writing video scripts, crafting hooks, creating show notes, batch outlining
- **Formation**: `content-planning`
- **Inbox**: `#scripts`
- **Example**: "Write a script for the Docker tutorial" or "Create a content calendar"

### Editor

- **Role**: Post-Production Lead — editing, effects, export
- **When to use**: Video cutting, colour grading, audio mixing, format conversion, rendering
- **Formation**: `video-production`
- **Inbox**: `#editing`
- **Example**: "Edit today's footage" or "Export in 1080p and 4K"

### Growth Analyst

- **Role**: Data Analyst — SEO, analytics, growth
- **When to use**: SEO audits, analytics reports, competitor analysis, keyword research, retention checks
- **Formation**: `channel-growth`
- **Inbox**: `#growth`
- **Example**: "Run an SEO audit" or "Pull this week's analytics"

### Art Director

- **Role**: Visual Designer — thumbnails, graphics, branding
- **When to use**: Thumbnail creation, A/B testing, brand graphics, end screens
- **Formation**: `thumbnail-lab`
- **Inbox**: `#thumbnails`
- **Example**: "Create a thumbnail for the Python tips video"

## Formation Workflows

| Goal | Formation | Trigger |
|------|-----------|---------|
| Produce a video end-to-end | `video-production` | "Start production on [topic]" |
| Analyse channel performance | `channel-growth` | "Run a growth review" |
| Plan content batch | `content-planning` | "Plan next month's content" |
| Create/test thumbnails | `thumbnail-lab` | "Design thumbnail for [video]" |
| Manage community | `community-ops` | "Review community engagement" |

## Tips

- Address the **agent by name** for direct tasks: "Scriptwriter, outline a video on..."
- Use **formation names** for coordinated work: "Run video-production for..."
- Check `#growth` inbox for automated analytics reports
- The Showrunner is the default escalation point for all agents
