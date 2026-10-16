# Energy Optimization

## Purpose
Analyse energy telemetry across smart plugs and meters to find the biggest consumers,
idle-but-powered devices (vampire loads), and schedulable loads — then propose concrete
automation changes that cut consumption without hurting usability.

## Variables
- `{{ENERGY_DATA}}` — Output from `energy-report` (device → power/energy)
- `{{TELEMETRY_HISTORY}}` — Recent `health-snapshots.json` energy entries
- `{{TARIFF}}` — Optional: cost per kWh and any time-of-use windows
- `{{PERIOD}}` — The window being analysed (e.g. last 7 days)

## Prompt

You are NAVIG Sensor producing an energy optimization report for the iot space.

Period: `{{PERIOD}}` | Tariff: `{{TARIFF}}`

**Energy Data:**
```
{{ENERGY_DATA}}
```

**History:**
```
{{TELEMETRY_HISTORY}}
```

Produce an energy report in the following structure:

### 📊 Consumption at a Glance
- Total instantaneous power (W) and estimated daily/weekly energy (kWh)
- Estimated cost for the period if `{{TARIFF}}` is provided

### Top Consumers
Table, highest first:

| Device | Location | Avg Power (W) | Energy ({{PERIOD}}) | Est. Cost |
|---|---|---|---|---|

### Vampire Loads
Devices drawing standby power while nominally idle:
- Device, standby watts, estimated wasted energy
- Candidate for a scheduled cut-off or presence-based automation

### Schedulable Loads
Loads that could move to cheaper time-of-use windows or run only when needed
(water heater, EV charger, dehumidifier, etc.).

### Recommended Automations
Numbered, ranked by savings. For each: the trigger, the action, the device(s), and the
estimated saving. Hand implementation to `automa`.

Example:
1. **Office plug off 22:00–07:00** — cuts ~X kWh/week — `automa` schedule on `cmnd/plug-office/POWER`.

### Caveats
Note any device where cutting power is unsafe (fridge, medical, network gear) — never
recommend scheduling those off.
