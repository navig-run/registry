---
space: iot-space
version: 1.0.0
created: 2026-07-10
---

# Space: iot

## Purpose
Unified command mesh spanning EVERY IoT and smart-home device — discovery, the MQTT
message bus, firmware/OTA, network segmentation and security, telemetry, and automation.
This space gives a single operator full situational awareness and automation authority
over every sensor, plug, bulb, hub, camera, and controller they own.

## Scope
- Protocols: Wi-Fi, Zigbee, Z-Wave, Matter/Thread, BLE, MQTT
- Device classes: plugs, bulbs, sensors, cameras, hubs, controllers, energy monitors
- Firmware ecosystems: Tasmota, ESPHome, WLED, Shelly, Sonoff, Zigbee2MQTT
- Hubs & brokers: Mosquitto (MQTT), Home Assistant, Zigbee/Z-Wave coordinators
- Network: IoT VLAN isolation, mDNS/SSDP discovery, segmentation, CVE audit

## Active Agents
beacon · broker · warden · flux · automa · sensor

## Active Formations
discovery-sweep · mqtt-ops · security-mesh · firmware-fleet · automation-loop

## Key Paths
- Space root:      the folder containing this .navig/ (installed: ~/.navig/spaces/iot-space)
- Config:          .navig/config.yaml
- Device registry: .navig/memory/device-registry.json (copy from device-registry.example.json)
- Wiki:            .navig/wiki/
