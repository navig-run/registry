---
name: cloudflare-agents
category: cloudflare
tags: [cloudflare, agents-sdk, ai, durable-objects, websockets, mcp]
description: >-
  Build stateful AI agents on Cloudflare Workers with the Cloudflare Agents SDK (the `agents` npm
  package) — persistent SQLite-backed state, callable RPC over WebSocket, scheduling/cron, durable
  Workflows, built-in queue + retries, MCP client/server, streaming chat agents, and React hooks.
  Use when the operator says "build a Cloudflare agent", "AIChatAgent", "useAgent / useAgentChat",
  "schedule a task in my agent", "MCP server on Workers", "@callable", or is editing a class
  extending `Agent`/`AIChatAgent` with a durable_objects + migrations block. This is the CLOUDFLARE
  Agents SDK, NOT navig's own agents/formations — different system. Read-and-author; wrangler
  deploys. Retrieve the live Agents docs before quoting APIs — the SDK moves fast.
---

# Cloudflare Agents SDK

> **Name note:** this covers the *Cloudflare* `agents` package (Durable-Object-backed agents on
> Workers). It is unrelated to navig's own agents, formations, and `.github/agents/`. Don't conflate
> the two — an `Agent` class here is a Cloudflare DO, not a navig subagent.

Each agent is a Durable Object with a class instance per name: persistent state, its own SQLite,
WebSocket connections, and a scheduler. **Prefer retrieval over memory** — the API surface is large
and evolving: `https://developers.cloudflare.com/agents/` (per-topic pages under
`/api-reference/`). Fetch the specific page when implementing a feature.

## What it gives you

Persistent auto-synced state (`setState`) · callable RPC (`@callable`) · scheduling (once /
`scheduleEvery` / cron) · durable Workflows (`AgentWorkflow`) · durable execution (`runFiber` /
`stash`, survives eviction) · built-in FIFO queue + `retry()` with backoff · MCP client **and**
server (`McpAgent`) · streaming chat (`AIChatAgent`, resumable) · React hooks (`useAgent`,
`useAgentChat`) · email handling · webhooks + push · diagnostics-channel observability.

## First: install

```bash
npm ls agents || npm install agents
# chat agents also need:
npm install agents @cloudflare/ai-chat ai @ai-sdk/react
```

## wrangler config

```jsonc
{
  "compatibility_flags": ["nodejs_compat"],
  "durable_objects": { "bindings": [{ "name": "MyAgent", "class_name": "MyAgent" }] },
  "migrations": [{ "tag": "v1", "new_sqlite_classes": ["MyAgent"] }],
  "ai": { "binding": "AI" }
}
```

**Gotchas:** do NOT enable `experimentalDecorators` in tsconfig (breaks `@callable`); never edit an
old migration tag; each agent class needs its own binding + migration entry.

## The agent class

```typescript
import { Agent, routeAgentRequest, callable } from "agents";

type State = { count: number };

export class Counter extends Agent<Env, State> {
  initialState = { count: 0 };

  validateStateChange(next: State) {
    if (next.count < 0) throw new Error("Count cannot be negative");
  }

  @callable()
  increment() {
    this.setState({ count: this.state.count + 1 });
    return this.state.count;
  }
}

export default {
  fetch: (req, env) => routeAgentRequest(req, env) ?? new Response("Not found", { status: 404 }),
};
```

**Routing:** requests map to `/agents/{agent-name}/{instance-name}` (e.g. `Counter` →
`/agents/counter/user-123`). Custom: `getAgentByName(env.MyAgent, "id")` then `agent.fetch(request)`.

## Core APIs

| Task | API |
|------|-----|
| Read / write state | `this.state.x` · `this.setState({ x })` |
| SQL | `` this.sql`SELECT * FROM t WHERE id = ${id}` `` |
| Schedule (delay / cron / interval) | `this.schedule(60, "task", p)` · `this.schedule("0 * * * *", …)` · `this.scheduleEvery(30, "poll")` |
| RPC / streaming RPC | `@callable() m()` · `@callable({ streaming: true }) s(res)` |
| Workflow / durable fiber | `this.runWorkflow("W", p)` · `this.runFiber("n", async ctx => …)` |
| Queue / retry | `this.queue("handler", p)` · `this.retry(fn, { maxAttempts: 5 })` |
| Broadcast / connections | `this.broadcast(msg)` · `this.getConnections(tag?)` |

## React client

```tsx
import { useAgent } from "agents/react";

const agent = useAgent({
  agent: "Counter",
  name: "my-instance",
  onStateUpdate: (s) => setLocalState(s),
});
// agent.setState({ count: state.count + 1 })
```

## When you want more depth (fetch the doc)

| Topic | Docs page |
|-------|-----------|
| State & sync | `/agents/api-reference/store-and-sync-state/` |
| Callable / streaming RPC | `/agents/api-reference/callable-methods/` |
| Scheduling | `/agents/api-reference/schedule-tasks/` |
| Workflows / durable execution | `/agents/api-reference/run-workflows/` · `/durable-execution/` |
| Queue / retries | `/agents/api-reference/queue-tasks/` · `/retries/` |
| Chat agents (AIChatAgent) | `/agents/api-reference/chat-agents/` |
| Client SDK (hooks) | `/agents/api-reference/client-sdk/` |
| MCP client / server | `/agents/api-reference/mcp-client-api/` · `/mcp-agent-api/` · securing: `/securing-mcp-servers/` |
| Email / webhooks / push | `/agents/api-reference/email/` · `/webhooks/` · `/push-notifications/` |
| Observability | `/agents/api-reference/observability/` |

Adjacent skills: `durable-objects` (the substrate), `workers-best-practices`, `cloudflare-email`
(the agent `onEmail` path), `wrangler`.
