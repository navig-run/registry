# Social Circle Space — Agent Guide

> **Planned roles — not shipped yet.** No agent definitions exist in `.navig/store/agents/`
> for this space; the roles below describe the intended design. Today, use the built-in
> contact book (`navig contacts …`).

## relationship-intel (Lead)
The primary relationship intelligence agent. Surfaces warm-up alerts, suggests circles for new contacts, and synthesizes interaction patterns.

## contact-organizer
Handles imports, deduplication, circle placement, and contact record maintenance.

## interaction-logger
Records interactions, updates lastContact timestamps, and manages follow-up notes.

## network-mapper
Builds and queries the relationship graph. Answers "who do I know in X?" and "how am I connected to Y?"
