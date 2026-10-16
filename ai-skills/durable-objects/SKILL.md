---
name: durable-objects
category: cloudflare
tags: [cloudflare, durable-objects, stateful, websockets, coordination]
description: >-
  Build and review Cloudflare Durable Objects — single-owner stateful coordination (chat rooms,
  multiplayer, booking/inventory, per-user state), RPC methods, SQLite storage, alarms, and
  hibernatable WebSockets. Use when the operator says "build a chat room / game / booking system",
  "I need a Durable Object", "coordinate real-time state at the edge", "per-entity state", "add a
  WebSocket to my Worker", or is editing a class extending DurableObject, a migrations block, or a
  durable_objects binding in wrangler.jsonc. Read-and-author: it writes/reviews DO code; the deploy
  is wrangler's. Retrieve the live DO docs before quoting API details — they change.
---

# Durable Objects

One DO = one coordination atom (one room, one game, one user), addressed by name, holding its own
SQLite storage and single-threaded execution. Reach for a DO when plain Workers can't: when requests
to the *same* entity must see a consistent, ordered view of state.

**Retrieve, don't guess.** DO APIs and limits move: `https://developers.cloudflare.com/durable-objects/`
(+ `/api/`, `/best-practices/`, `/examples/`). Fetch the relevant page before implementing.

## Use a DO for / not for

| Reach for a DO | Use a plain Worker instead |
|----------------|----------------------------|
| Coordination — chat, multiplayer, collab docs | Stateless request handling |
| Strong consistency — inventory, booking, turn-based | Maximum global fan-out / distribution |
| Per-entity storage — multi-tenant, per-user | High-volume independent requests |
| Persistent connections — WebSockets, live notifications | |
| Per-entity scheduled work — renewals, timeouts | |

In this tree, `services/lighthouse/` holds the ONE brain's outbound WS uplink over the edge — the
same "single durable coordinator + WebSocket" shape a DO gives you. Study that seam before building
a parallel coordinator.

## wrangler config

```jsonc
{
  "durable_objects": { "bindings": [{ "name": "MY_DO", "class_name": "MyDurableObject" }] },
  "migrations": [{ "tag": "v1", "new_sqlite_classes": ["MyDurableObject"] }]
}
```

Each DO class needs its own binding **and** its own migration entry. **Never edit an old migration
tag** — always add a new one.

## The pattern

```typescript
import { DurableObject } from "cloudflare:workers";

export interface Env { MY_DO: DurableObjectNamespace<MyDurableObject>; }

export class MyDurableObject extends DurableObject<Env> {
  constructor(ctx: DurableObjectState, env: Env) {
    super(ctx, env);
    // schema setup ONLY — never hold this across fetch/external I/O
    ctx.blockConcurrencyWhile(async () => {
      this.ctx.storage.sql.exec(
        `CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY AUTOINCREMENT, data TEXT NOT NULL)`
      );
    });
  }

  // RPC method — preferred over a fetch() handler (compat date >= 2024-04-03)
  async addItem(data: string): Promise<number> {
    return this.ctx.storage.sql
      .exec<{ id: number }>("INSERT INTO items (data) VALUES (?) RETURNING id", data)
      .one().id;
  }
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const stub = env.MY_DO.getByName("room-123");   // deterministic routing
    return Response.json({ id: await stub.addItem("hello") });
  },
};
```

## Critical rules

1. Model around **coordination atoms** — one DO per room/game/user, never one global DO.
2. **`getByName()`** for deterministic routing (same input → same instance). Use `idFromString`
   for a stored ID, `newUniqueId()` when you'll persist the mapping yourself.
3. **SQLite storage** — declare `new_sqlite_classes` in migrations; `sql.exec` is synchronous.
4. **Persist first, cache second** — write to storage *before* updating in-memory state (evictions
   and crashes drop memory).
5. `blockConcurrencyWhile()` is for constructor init only — not per request.
6. **One alarm per DO** — `setAlarm()` replaces any pending alarm.

## Anti-patterns (never)

- A single global DO funneling all requests (bottleneck).
- `blockConcurrencyWhile()` on every request (kills throughput).
- Critical state only in memory.
- `await`ing between related storage writes (breaks atomicity).
- Holding `blockConcurrencyWhile()` across `fetch()` or external I/O.

## Storage & alarms

```typescript
// SQL (sync, recommended)
this.ctx.storage.sql.exec("INSERT INTO t (c) VALUES (?)", value);
const rows = this.ctx.storage.sql.exec<Row>("SELECT * FROM t").toArray();
// KV (async)
await this.ctx.storage.put("key", value);

await this.ctx.storage.setAlarm(Date.now() + 60_000);   // schedule (replaces existing)
async alarm(): Promise<void> { /* process; optionally reschedule */ }
await this.ctx.storage.deleteAlarm();
```

## Testing (Vitest)

```typescript
import { env } from "cloudflare:test";
import { describe, it, expect } from "vitest";

describe("MyDO", () => {
  it("adds an item", async () => {
    const stub = env.MY_DO.getByName("test");
    expect(await stub.addItem("test")).toBe(1);
  });
});
```

Setup: `@cloudflare/vitest-pool-workers`. Adjacent skills: `workers-best-practices` (the DO class
rules — `extends`, `this.env`), `cloudflare-agents` (the Agents SDK is DO-backed), `wrangler`.
