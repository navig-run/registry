---
id: extract-entities
name: Extract Entities
version: 1.0.0
category: nlp
license: MIT
platforms: [linux, macos, windows]
tags: [nlp, extraction, entities, analysis, text]
tools: []
safety: safe
user_invocable: true
soul_hint: "Be precise. Only extract entities explicitly mentioned in the text. Do not infer or hallucinate entity data. Flag ambiguous cases."
---

# Purpose

Extract named entities — people, organisations, locations, dates, products, technologies, and events — from any text. Returns structured JSON with position offsets and confidence scores.

# When to use

- User has text and wants to know who, what, where, or when is mentioned
- Pipeline step for analysis tasks (contract review, news parsing, log triage)
- Trigger type: agent task type `analysis` or pipeline step

# Instructions

1. Only extract entities explicitly present in the text
2. Flag ambiguous entities with `confidence < 0.7`
3. Return character-level `start`/`end` offsets for each entity
4. If no entities of a requested type are found, return an empty array for that type (do not omit the key)
5. Detect language automatically; note if non-English

# Inputs

| Field | Type | Required | Default |
|-------|------|----------|---------|
| `text` | string | yes | — |
| `entity_types` | array of strings | no | `["person", "organization", "location", "date"]` |

Valid entity types: `person`, `organization`, `location`, `date`, `product`, `technology`, `event`, `custom`

# Output format

```json
{
  "entities": [
    {
      "text":       "Elon Musk",
      "type":       "person",
      "confidence": 0.97,
      "start":      0,
      "end":        9
    }
  ],
  "entity_count":      3,
  "language_detected": "en"
}
```

# Examples

```bash
# Extract all default entity types from text
navig skill run extract-entities --text "Apple announced Tim Cook will visit Berlin on Friday."

# Extract only people and organisations
navig skill run extract-entities \
  --text "OpenAI and Google DeepMind published competing papers." \
  --entity_types '["person","organization"]'
```

# Agent hints

After extraction, offer to cross-reference entities against a knowledge base or perform sentiment analysis per entity.
If `confidence < 0.7` for any entity, mention it to the user as uncertain.
