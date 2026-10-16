# OSINT collection — sources, pivots, hygiene

Passive, open, lawful sources only. Respect platform ToS and privacy law; minimize collection;
separate fact from assessment. Feed everything into the entity graph (`add-entity`).

## Source map (by entity type)
| Seed | Pivot to | Sources |
|---|---|---|
| **Person** | accounts, employer, contacts, infra | search engines, social platforms (public), professional networks, public records, gravatar, conference/talk listings |
| **Username** | other platforms, email, real name | cross-platform username search, breach-exposure (HIBP), code-host profiles |
| **Email** | accounts, breaches, name, domain | HIBP, gravatar, account-existence (where lawful), the domain it belongs to |
| **Org** | people, domains, brands, filings | company registries, job posts, press, brand/trademark, leadership pages |
| **Domain** | subdomains, IPs, certs, tech, owner | WHOIS/RDAP, crt.sh (cert transparency), passive DNS, BuiltWith-style tech, web archive |
| **IP / ASN** | hosts, services, org, neighbors | RDAP, passive DNS, Shodan/Censys (passive), ASN lookup |
| **Image** | location, source, reuse, metadata | reverse image search, EXIF (if present), landmark/shadow geolocation, archive |
| **Crypto wallet** | flows, exchanges, clusters | public block explorers, address clustering (open tooling) |

## Pivot recipes (the graph is the truth)
- **Identity spine:** person → username → reused username across platforms → email → breach context
  → real name confirmation. Score each hop's confidence; beware coincidental handle collisions.
- **Infra spine:** brand → domain → crt.sh subdomains → passive DNS IPs → ASN/org → neighboring
  hosts (passive). Stop at the scope fence.
- **Org→people:** company → job posts (tech stack + team) → named staff (public) → their public
  profiles → external footprint.
- **Corroborate before you commit:** ≥2 independent sources before a node/edge is "confirmed".

## Sock-puppet & operational hygiene (for lawful research accounts)
- Research from a clean, compartmented browser profile; don't log into target-adjacent accounts
  with your real identity. Don't interact with / tip off the subject.
- Never use fake identities to bypass access controls or to deceive real people into giving up
  info — that's social engineering and needs explicit scope. Passive viewing of public content
  only.
- Keep collection logged and reproducible; archive volatile pages (timestamped) as evidence.

## Anti-patterns (don't)
- Treating a single source as fact. Merging two people because they share a handle. Collecting
  private-life data on a person beyond the legitimate objective. Anything requiring login bypass,
  scraping against ToS at scale, or paid data of dubious legality.
