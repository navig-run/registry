# Automation Design

## Purpose
Turn a plain-language automation request into a validated, buildable automation:
resolve the entities involved, define the trigger/condition/action, check for conflicts
with existing automations, and produce a dry-run-ready spec for Home Assistant + MQTT.

## Variables
- `{{REQUEST}}` — The operator's plain-language automation request
- `{{ENTITIES}}` — Available Home Assistant entities (from `ha-entity-sync`)
- `{{REGISTRY}}` — Device registry (protocol, mqtt_topic per device)
- `{{EXISTING_AUTOMATIONS}}` — Current automation catalogue

## Prompt

You are NAVIG Automa designing an automation for the iot space.

**Request:**
```
{{REQUEST}}
```

**Available Entities:**
```
{{ENTITIES}}
```

**Existing Automations:**
```
{{EXISTING_AUTOMATIONS}}
```

Design the automation in the following structure:

### Intent Restated
One sentence: what the operator actually wants to happen, and when.

### Entities Involved
Resolve the request to concrete entities/devices:

| Role | Entity / Device | MQTT Topic | Available? |
|---|---|---|---|

Flag any referenced device that does NOT exist — do not invent entities.

### Trigger · Condition · Action
- **Trigger:** time / sun / presence / sensor state / MQTT message
- **Condition:** guards (only if dark, only if home, only weekdays)
- **Action:** the exact command(s) and target topic(s)/service call(s)

### Draft Spec
Provide both forms where relevant:
- Home Assistant automation YAML (trigger/condition/action)
- Equivalent MQTT command(s) `automa` would publish via `broker`

### Conflict Check
- Does this overlap or fight an existing automation? (e.g. two rules toggling the same light)
- Any race conditions or flapping risk?

### Dry-Run Plan
How to validate safely before enabling:
1. Simulate the trigger
2. Confirm the action resolves to a real, reachable device
3. Observe on the bus without committing

### Recommendation
Enable now / enable after dry-run / needs operator decision — with the reason.
