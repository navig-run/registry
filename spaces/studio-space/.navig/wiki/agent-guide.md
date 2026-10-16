# Agent Guide

> How to work with studio space agents and formations.

## Agents Overview

| Agent | Role | Primary Formation | Inbox |
|-------|------|-------------------|-------|
| **producer** | Creative Director & Lead | track-production | #production |
| **mix-engineer** | Technical Audio Specialist | mastering-suite | #mixing |
| **sound-designer** | Sonic Architect | sample-lab | #samples |
| **release-manager** | Distribution Coordinator | release-pipeline | #releases |
| **session-planner** | Production Logistics | collab-session | #production |

## Formations

### track-production
- **Lead**: producer
- **Team**: mix-engineer, sound-designer, session-planner
- **Use**: Full track creation from concept to stems

### mastering-suite
- **Lead**: mix-engineer
- **Team**: producer
- **Use**: Mixing and mastering operations

### sample-lab
- **Lead**: sound-designer
- **Team**: producer
- **Use**: Sample creation, cataloging, sound design

### release-pipeline
- **Lead**: release-manager
- **Team**: mix-engineer, session-planner
- **Use**: Release preparation and distribution

### collab-session
- **Lead**: session-planner
- **Team**: producer, mix-engineer
- **Use**: Collaboration setup and management

## How Agents Communicate

1. **Inbox channels** route tasks to the right agent automatically
2. **Escalation** follows the chain: specialist → producer → operator
3. **Context memory** is shared via `.navig/memory/` JSON files
4. Agents read/write their specific memory paths defined in their YAML configs

## Triggering Agents

### Via Workflows
The playbooks in `.navig/store/workflows/` are followed by the agents, not run as CLI
commands. Ask for one by name ("run the morning-studio routine", "start the
track-production pipeline for this idea"), or hand a request to the active formation:

```bash
navig formation run "Start a new track: 92 BPM, F minor, lo-fi"
```

### Via Inbox
Send a message to a channel and the routes will direct it:
- `#production` → producer
- `#mixing` → mix-engineer
- `#mastering` → mix-engineer
- `#samples` → sound-designer
- `#releases` → release-manager

### Via Direct Invocation
```bash
# Ask the producer to review an arrangement
navig agent run producer --task "review the arrangement of the session in ./sessions/my-track"

# Ask the mix engineer to check loudness
navig agent run mix-engineer --task "check the loudness of ./masters/track.wav"
```

## Adding a Custom Agent

1. Create a new YAML file in `.navig/store/agents/`
2. Follow the schema from existing agents (id, name, version, persona, role, capabilities, triggers)
3. Add the agent to a formation in `.navig/store/formations/`
4. Register in `.navig/space.config.json`

## Related

- [[production-workflow]] — See agents in action across the pipeline
- [[mixing-guide]] — Tasks the mix-engineer handles
