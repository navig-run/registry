# Current Phase

> Template — replace with your own IoT fleet's current focus.

## Active Goal

Confirm the live broker, IoT VLAN and Home Assistant URL, then run the first discovery sweep.

## In Progress

_Nothing in progress._

## Next Steps

- [ ] **Seed the space state** — copy each `.navig/memory/*.example.json` and `.navig/inbox/routes.example.yaml` to its live name
- [ ] **Confirm the MQTT broker** — update `mqtt_host` in `.navig/config.yaml`; disable anonymous access
- [ ] **Confirm the IoT VLAN/subnet** — update `iot_subnet` and `iot_vlan`; tighten firewall isolation
- [ ] **Set the Home Assistant URL + vault token** — for `ha-entity-sync`
- [ ] **Run the first discovery sweep** — `navig ask "run the morning-mesh-sweep workflow"`
- [ ] **Onboard the first real device** — `navig ask "run the device-onboard workflow"`
- [ ] **Run the first VLAN audit** — `navig skill run vlan-audit`

## Completed

- [x] Space installed (6 agents, 5 formations, 12 skills, 6 workflows, 8 prompts, wiki and example memory)

## Blocked

_Nothing blocked._
