# MQTT Topic Map

## Purpose
Turn a raw MQTT bus capture into a clean, hierarchical topic map — grouped by device
and function — and correlate every topic back to the device that owns it. Produces the
content for the `mqtt-topics.md` wiki page.

## Variables
- `{{CAPTURE}}` — Output from `mqtt-subscribe` on `#` (topic + payload lines)
- `{{REGISTRY}}` — Current `device-registry.json` contents
- `{{BROKER_HOST}}` — MQTT broker host:port
- `{{SCAN_DATE}}` — ISO timestamp of the capture

## Prompt

You are NAVIG Broker mapping the live MQTT topic tree for the iot space.

Broker: `{{BROKER_HOST}}` | Captured: `{{SCAN_DATE}}`

**Bus Capture:**
```
{{CAPTURE}}
```

**Known Registry:**
```
{{REGISTRY}}
```

Produce a topic map in the following structure:

### Topic Tree
Render the captured topics as an indented tree, collapsing device instances into a
pattern where sensible:

```
cmnd/
  <device>/POWER        → command: on/off
tele/
  <device>/STATE        → periodic state (uptime, wifi, heap)
  <device>/SENSOR       → sensor readings (ENERGY, temp, humidity)
stat/
  <device>/RESULT       → command acknowledgements
zigbee2mqtt/
  <friendly_name>       → device state (Zigbee)
  bridge/               → coordinator + network map
homeassistant/          → MQTT discovery config topics
```

### Topic → Device Correlation
Table mapping each device's topic prefix to its registry entry:

| Device | Command Topic | Telemetry Topic | Protocol | Retained? |
|---|---|---|---|---|

### Bus Health Notes
- Retained-message count and any suspiciously large retained payloads
- Devices publishing telemetry vs devices that are silent
- Any topic with no matching registry device (orphan topic)
- QoS distribution and any last-will topics observed

### Recommended Actions
Numbered list: topics to clean up, orphan topics to investigate, devices to register,
retained messages to prune (defer deletion to operator approval).
