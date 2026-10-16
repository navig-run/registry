# Lab — the isolated practice range

The lab is where **dangerous tradecraft is practiced safely**: exploit development, tooling,
malware/sample triage, and CTF-style skill-building — against intentionally vulnerable targets,
**never** production or third parties. Hard rule: **no network egress** from the lab segment.

## Isolation model
```
host ── hypervisor (VirtualBox/Hyper-V/VMware/Proxmox) or Docker
          └── lab network: HOST-ONLY / INTERNAL — no route to LAN or internet
                ├── attacker box   (Kali / Parrot / your toolbox)
                └── target boxes    (deliberately vulnerable — below)
```
- **Snapshot before and after** every session; revert to a clean baseline between exercises.
- **Malware analysis**: separate, disposable VM, no shared folders, no clipboard, no egress;
  detonate only with a sink (INetSim/FakeNet) — assume anything can try to escape.
- Keep the lab **offline**; pull tools/targets in on the host, then move them into the isolated net.

## Target catalog (intentionally vulnerable, free)
| Target | Focus | Get it |
|---|---|---|
| OWASP **Juice Shop** | modern web app | `docker run -p 3000:3000 bkimminich/juice-shop` |
| **DVWA** | classic web vulns | `docker run -p 8080:80 vulnerables/web-dvwa` |
| **WebGoat** | web app lessons | `docker run -p 8081:8080 webgoat/webgoat` |
| **Metasploitable 2/3** | full vulnerable host | VM image |
| **VulnHub** | boot-to-root VMs | downloadable VMs |
| **HackTheBox / TryHackMe** | guided ranges | online (their infra = their authorization) |
| **GOAD** (Game of Active Directory) | AD attack paths | Ludus/Vagrant lab |

> HTB/THM run on *their* infrastructure under *their* terms — that IS your authorization there.
> Everything else stays inside the host-only lab net.

## Suggested layout
```
lab/
├── README.md            (this file)
├── targets/             notes per target: setup, goals, walkthroughs, your solutions
├── tooling/             your toolbox notes (installed tools, configs, wordlists pointers)
├── ctf/                 per-CTF/box writeups (sanitized), flags log
├── samples/             malware triage notes (NEVER live samples in git — pointers + hashes only)
└── snapshots.md         snapshot/revert log per VM
```
`.gitignore` the heavy/dangerous bits: `targets/**/vm/`, `samples/**` (binaries), any captured creds.

## Lab → arsenal feedback loop
A technique that works in the lab becomes a playbook in `arsenal/cyber/` (with its ATT&CK mapping);
a tool you adopt gets registered via the `arsenal-search` skill. The lab is where capability is
*earned* before it's ever pointed at an authorized real target.
