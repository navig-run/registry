#!/usr/bin/env bash
# PURPOSE:       Snapshot the live MQTT topic tree and print a sorted, unique topic list
# USAGE:         ./scripts/dump-mqtt-topics.sh [host] [port] [seconds]
# PREREQUISITES: mosquitto-clients (mosquitto_sub)
# REQUIRES:      none

set -u
HOST="${1:-192.168.1.10}"
PORT="${2:-1883}"
SECONDS_LISTEN="${3:-20}"

if ! command -v mosquitto_sub >/dev/null 2>&1; then
  echo "mosquitto_sub not found — install mosquitto-clients" >&2
  exit 2
fi

echo "=== MQTT Topic Dump ==="
echo "Broker: $HOST:$PORT  |  Listening ${SECONDS_LISTEN}s"
echo

# -v prints "<topic> <payload>"; keep only the topic column, sort unique
mosquitto_sub -h "$HOST" -p "$PORT" -t '#' -v -W "$SECONDS_LISTEN" 2>/dev/null \
  | awk '{print $1}' \
  | sort -u \
  | tee /tmp/iot-topics.txt

COUNT=$(wc -l < /tmp/iot-topics.txt | tr -d ' ')
echo
echo "Unique topics: $COUNT"
echo "Saved to /tmp/iot-topics.txt"
