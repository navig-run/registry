# Entity Graph Pivot

## Purpose
Given the current state of the entity graph, generate the next best investigative pivots
and rank them by expected value, so collection effort goes where it pays off instead of
sprawling. A pivot is a hypothesis ("this identifier should lead to that account/infra/
person"); this prompt turns the graph into a prioritized worklist. Run it whenever the
graph stalls or after each collection sweep.

## Variables
- `{{CASE_ID}}` — the case whose graph you're pivoting on
- `{{GRAPH_SNAPSHOT}}` — current nodes + edges (from `entities.json`, scoped to the case)
- `{{OBJECTIVE}}` — what the case must answer (a pivot only counts if it moves this)
- `{{CONSTRAINTS}}` — passive-only? authorization status? time budget? legal no-go zones?

## Prompt
You are the `osint-analyst` working the graph for `{{CASE_ID}}`. The graph is the truth —
pivot on it, not in your head. Your job: read `{{GRAPH_SNAPSHOT}}`, find the highest-value
next moves toward `{{OBJECTIVE}}`, and rank them. Stay within `{{CONSTRAINTS}}`; if a pivot
needs active recon or contact, flag that it is **gated** on authorization, do not assume it.

1. **Map the frontier.** Inventory the graph: which nodes are confirmed vs leads, which
   edges are corroborated vs single-source, and where the dangling/under-explored nodes
   are. The frontier is where leads sit unconfirmed or a node has obvious un-followed edges.
2. **Generate pivots across the four planes.** For each frontier node, propose concrete
   pivots along the standard chain:
   **identifiers → accounts → infrastructure → people** (e.g. email → breach/registration
   footprint → reused on which platforms → which domains it registered → who else operates
   them). Name the exact source/method for each.
3. **Score expected value.** Rate each pivot on **(a)** likelihood it resolves (how
   reachable the data is, passively), **(b)** impact on `{{OBJECTIVE}}` if it lands, **(c)**
   cost/risk (time, legality, whether it's passive or gated-active). Combine into an
   expected-value score and a one-line rationale.
4. **Guard against false merges.** For any "same_as" pivot (claiming two nodes are one
   identity), require a corroboration plan of **≥2 independent signals** before merging —
   note the risk of a wrong merge and how you'll disconfirm it (→ `username-identity-correlation`).
5. **Flag legality per pivot.** Tag each as **passive/open** (run now) or
   **active/gated** (needs an engagement + scope; do not run without it). Out-of-scope or
   ToS-violating pivots are dropped with a reason, not queued.
6. **Rank and recommend.** Produce a ranked worklist (highest EV first). Mark the top 3 as
   "do next" with the exact method, the source, and the corroboration each will need.
7. **Note expected graph writes.** For each top pivot, state which `add-entity`
   nodes/edges it would create if it lands — so the graph stays the system of record.

## Output
A ranked pivot worklist for `{{CASE_ID}}`: each pivot with its plane
(identifier/account/infra/person), method+source, expected-value score with rationale,
passive-vs-gated tag, and (for identity merges) a ≥2-signal corroboration plan. Top 3
marked "do next" with their projected graph writes. Facts and assessments kept distinct.
