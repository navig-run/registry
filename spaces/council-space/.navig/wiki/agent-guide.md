# Council Space — Agent Guide

> These roles are the **design target**. No agent files ship with this space yet
> (`.navig/space.json` lists none); see `.navig/GENESIS.md`.

## Council Agent Archetypes

Add agents to `.navig/store/agents/` representing these archetypes:

| Archetype | Bias | Best for |
|-----------|------|---------|
| `optimist` | Upside, opportunity | Growth decisions |
| `skeptic` | Risk, failure modes | Any high-stakes decision |
| `pragmatist` | Feasibility, constraints | Execution planning |
| `contrarian` | Challenges consensus | When everyone agrees too quickly |
| `domain-expert` | Deep expertise | Technical decisions |
| `user-advocate` | End-user perspective | Product decisions |

## Moderator Role

The moderator agent does not debate. It facilitates, summarizes positions, and extracts the decision card after debate completes.
