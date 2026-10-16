# GENESIS — Council Space

## Why This Exists

Hard decisions don't have single right answers — they have trade-offs. Council Space lets you assemble a group of AI agents that each argue from a distinct perspective, debate the problem, and synthesize a decision with the dissents intact.

Without it: decisions are made by the last voice heard or the most confident agent. With it: every option gets a real advocate.

## What It Does

Council Space runs structured multi-agent deliberation:
- **Council assembly** — select agents representing different expertise or worldviews
- **Debate rounds** — each agent argues their position; others rebut
- **Decision synthesis** — moderator agent extracts the decision with full reasoning
- **Dissent logging** — minority views recorded alongside the winning path

## Core Pattern

```
1. Define the question or decision
2. Assemble 3-7 agents from the council roster
3. Run debate formation
4. Review decision card + dissents
5. Log decision to memory
```

## Use Cases

- Major strategic pivots with high uncertainty
- Resource allocation between competing priorities
- Architectural or technical direction choices
- Any decision where you want to stress-test your thinking

## Origin

Built because single-agent responses optimize for coherence, not correctness. Sometimes you need the arguments, not just the answer.

---
*Space ID: `council-space` · Runtime: `navig-space-2` · Tier: labs*
