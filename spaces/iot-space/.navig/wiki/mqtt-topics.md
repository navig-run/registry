# MQTT Topics

**Space**: `iot`  
**Last Updated**: 2026-07-10  
**Maintained by**: Broker  
**Auto-updated by**: `mqtt-ops` formation (post topic map)

---

## Broker

| Parameter | Value |
|---|---|
| **Host** | `192.168.1.10` *(update to your broker)* |
| **Port** | `1883` (plain) · `8883` (TLS) |
| **Auth** | username/password via space vault — anonymous **disabled** |
| **Base namespace** | `iot` |

> **Update this page** after running your first topic map:
> `navig skill run mqtt-subscribe --topic '#' --duration 30 && navig agent run broker --task "mqtt topic map"`

---

## Topic Tree (convention)

```
cmnd/                       → commands TO devices
  <device>/POWER            → on/off
  <device>/Color            → set color (JSON)
tele/                       → periodic telemetry FROM devices
  <device>/STATE            → uptime, wifi RSSI, heap
  <device>/SENSOR           → ENERGY, temperature, humidity
stat/                       → command acknowledgements
  <device>/RESULT
zigbee2mqtt/                → Zigbee mesh (via Zigbee2MQTT)
  <friendly_name>           → device state
  bridge/devices            → full device list (retained)
  bridge/networkmap         → topology response
homeassistant/              → MQTT discovery config (retained)
$SYS/                       → broker internals (read-only)
  broker/uptime · broker/clients/connected · broker/messages/received
```

---

## Topic → Device Correlation

| Device | Command Topic | Telemetry Topic | Protocol | Retained? |
|---|---|---|---|---|
| *(populate via mqtt-topic-map prompt)* | | | | |

---

## Retained Messages

| Topic | Purpose | Size | Keep? |
|---|---|---|---|
| *(add after first topic map)* | | | |

---

## Silent / Orphan Topics

Topics on the bus with no matching registry device, or devices publishing nothing:

| Topic | First Seen | Verdict |
|---|---|---|
| *(none)* | | |

---

## Topic Map Update Log

| Date | Change | Changed by |
|---|---|---|
| 2026-07-10 | Initial topic map page created | Broker |
