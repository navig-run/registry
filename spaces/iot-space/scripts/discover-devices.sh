#!/usr/bin/env bash
# PURPOSE:       Discover IoT devices on the LAN via SSDP (UPnP) + mDNS (avahi) + ARP
# USAGE:         ./scripts/discover-devices.sh [range]
# PREREQUISITES: python3; avahi-utils (avahi-browse) optional; iproute2 (ip)
# REQUIRES:      none

set -u
RANGE="${1:-192.168.20.0/24}"
echo "=== IoT Device Discovery ==="
echo "Range: $RANGE"
echo

echo "[ SSDP / UPnP ]"
python3 - <<'PY'
import socket
msg = "\r\n".join([
  'M-SEARCH * HTTP/1.1','HOST:239.255.255.250:1900',
  'MAN:"ssdp:discover"','MX:2','ST:ssdp:all','','']).encode()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.settimeout(3)
s.sendto(msg, ('239.255.255.250', 1900))
seen={}
try:
  while True:
    data, addr = s.recvfrom(2048)
    ip = addr[0]
    if ip in seen: continue
    seen[ip]=True
    server=""
    for line in data.decode(errors='ignore').splitlines():
      if line.lower().startswith('server:'): server=line.split(':',1)[1].strip()
    print(f"  {ip:16s} {server}")
except socket.timeout:
  pass
print(f"  SSDP devices: {len(seen)}")
PY
echo

echo "[ mDNS ]"
if command -v avahi-browse >/dev/null 2>&1; then
  avahi-browse -art 2>/dev/null | grep -E "hostname|address|port" | head -40
else
  echo "  avahi-browse not installed — install avahi-utils for mDNS discovery"
fi
echo

echo "[ ARP neighbours ]"
if command -v ip >/dev/null 2>&1; then
  ip neigh show | awk '{printf "  %-16s %s\n", $1, $5}'
else
  arp -a | awk '{print "  "$2, $4}' | tr -d '()'
fi

echo
echo "Discovery complete."
