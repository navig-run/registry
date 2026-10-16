# Cable Log

**Space**: `homelab`  
**Last Updated**: 2026-02-26  
**Maintained by**: Archivist  
**Updated via**: `cable-map-update` workflow

---

## How to Use This Log

This file records all physical cable connections in the space. It is maintained through
the `cable-map-update` workflow which guides you through documenting each cable
interactively.

To add new cables:
```bash
navig ask "run the cable-map-update workflow"
```

To view cables for a specific location:
```bash
navig agent run archivist --task "show cables at desk"
```

---

## Cable Count Summary

| Location | Cat5e/6 | Fibre | USB | HDMI/DP | Power | Total |
|---|---|---|---|---|---|---|
| *(run cable-map-update to populate)* | | | | | | |

---

## Cable Entries

> *(Entries are appended by the cable-map-update workflow)*

<!--
Cable entry format (YAML):

- id: "desk-C001"
  type: Cat6
  colour: blue
  source: "homelab-01:ETH0"
  destination: "switch-01:Port3"
  length_m: 2
  label: "WS01-SW-P3"
  condition: good
  notes: ""
  documented: "YYYY-MM-DD"
-->

### Location: desk
*(No cables documented yet for this location)*

### Location: server-rack
*(No cables documented yet for this location)*

### Location: network-closet
*(No cables documented yet for this location)*

---

## Issues Register

Cables flagged during documentation that need attention:

| Cable ID | Issue | Location | Flagged | Status |
|---|---|---|---|---|
| *(none)* | | | | |

---

## Labelling Convention

All cables should be labelled at both ends using the format:
```
<SOURCE_DEVICE_SHORT>-<DEST_DEVICE_SHORT>-<PORT>
```

Examples:
- `WS01-SW1-P3` → Homelab-01 to Switch-1 Port 3
- `NAS-SW1-P5` → NAS to Switch-1 Port 5
- `PI4-SW1-P7` → Pi4-Server to Switch-1 Port 7

---

## Change Log

| Date | Location | Cables Added | Changed by |
|---|---|---|---|
| 2026-02-26 | — | Initial file created | Archivist |
