# Security Segmentation Brief

## Purpose
Generate a concise, human-readable security situation report for the iot space,
focused on network segmentation, default credentials, firmware CVE exposure, and rogue
devices — suitable for the weekly review or incident awareness.

## Variables
- `{{VLAN_AUDIT_DATA}}` — Output from `vlan-audit`
- `{{CREDENTIAL_DATA}}` — Output from `credential-audit`
- `{{FIRMWARE_CVE_DATA}}` — Output from `firmware-check` + CVE correlation
- `{{ROGUE_DATA}}` — Unregistered devices from `device-discover`
- `{{SCAN_DATE}}` — ISO timestamp of collection
- `{{SCOPE}}` — Hosts/subnets covered

## Prompt

You are NAVIG Warden producing the security segmentation brief for the iot space.

Collected: `{{SCAN_DATE}}` | Scope: `{{SCOPE}}`

**VLAN / Segmentation Audit:**
```
{{VLAN_AUDIT_DATA}}
```

**Default Credential Audit:**
```
{{CREDENTIAL_DATA}}
```

**Firmware / CVE:**
```
{{FIRMWARE_CVE_DATA}}
```

**Rogue / Unregistered:**
```
{{ROGUE_DATA}}
```

Produce a security brief in the following structure:

### 🟢/🟡/🔴 Overall Security Posture
One-sentence verdict with colour indicator:
- 🟢 **Clean** — isolation holds, no default creds, no CVEs
- 🟡 **Monitor** — anomalies present, not yet confirmed threats
- 🔴 **Action Required** — segment leak, default creds accepted, or active CVE

### Segmentation
- Devices confirmed inside the IoT VLAN vs devices leaking to the trusted subnet
- Whether the isolation probe held (IoT segment cannot reach trusted hosts)
- Flag any 🚨 **boundary crossing** with the exact device + IP

### Default Credentials
Table of devices probed and result:
- 🚨 **Default creds accepted** — device + the accepted pair (redact in shared reports)
- ⚠️ **Anonymous MQTT allowed** — broker accepted an unauthenticated client
- ✅ **Hardened** — rejected all default pairs

### Firmware CVE Exposure
- Devices on firmware with a known CVE: device, version, CVE id, severity
- Recommended: hand to `flux` for a prioritised OTA plan

### Rogue / Unregistered Devices
- Any device on the mesh not in the registry — investigate vs onboard

### Threat Assessment
Rate each finding **Low / Medium / High / Critical**. For each High/Critical: the
recommended immediate action.

### Recommended Actions (Prioritised)
Numbered, most urgent first. Be specific: which device, which control (VLAN rule,
credential rotation, OTA update, quarantine).
