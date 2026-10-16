---
name: cloudflare-sandbox
category: cloudflare
tags: [cloudflare, sandbox, code-execution, containers, code-interpreter]
description: >-
  Build isolated code-execution environments on Cloudflare Workers with the Sandbox SDK
  (`@cloudflare/sandbox`) — run untrusted or LLM-generated code, code interpreters, CI/CD steps, and
  interactive dev environments in a container addressed like a Durable Object. Use when the operator
  says "run untrusted code safely", "execute LLM-generated code", "code interpreter", "sandbox this",
  "give the agent a shell/REPL", "expose a port from the sandbox", or is editing a `containers` +
  Sandbox binding in wrangler.jsonc. Local dev REQUIRES Docker. Read-and-author; the code you run is
  the mutating part — treat every input as hostile. Retrieve the live Sandbox docs before quoting
  API details; the base image version and API move.
---

# Cloudflare Sandbox SDK

Secure, isolated execution: each sandbox is a container fronted by a Durable Object, addressed by a
stable id (`getSandbox(env.Sandbox, 'user-123')`). Reach for it when navig-style "let the agent touch
live systems" needs a **blast radius of zero** — untrusted or model-generated code runs in the
sandbox, never on the host.

**Prefer retrieval over memory** — the base image tag and API surface change:
`https://developers.cloudflare.com/sandbox/` (+ `/api/`, `/get-started/`), examples at
`https://github.com/cloudflare/sandbox-sdk/tree/main/examples`.

## First: install (Docker required for local dev)

```bash
npm install @cloudflare/sandbox
docker info   # must succeed — local dev runs the container via Docker
```

## Required config

```jsonc
// wrangler.jsonc — keep this structure
{
  "containers": [{ "class_name": "Sandbox", "image": "./Dockerfile", "instance_type": "lite", "max_instances": 1 }],
  "durable_objects": { "bindings": [{ "class_name": "Sandbox", "name": "Sandbox" }] },
  "migrations": [{ "new_sqlite_classes": ["Sandbox"], "tag": "v1" }]
}
```

```typescript
// Worker entry — the re-export is mandatory or the Worker won't deploy
import { getSandbox } from "@cloudflare/sandbox";
export { Sandbox } from "@cloudflare/sandbox";
```

## Quick reference

| Task | Method |
|------|--------|
| Get a sandbox | `getSandbox(env.Sandbox, 'user-123')` |
| Run a command | `await sandbox.exec('python script.py')` → `{ stdout, stderr, exitCode, success }` |
| Run code (interpreter) | `await sandbox.runCode(code, { language: 'python' })` |
| Write / read file | `await sandbox.writeFile(p, c)` · `await sandbox.readFile(p)` |
| mkdir / list | `await sandbox.mkdir(p, { recursive: true })` · `await sandbox.listFiles(p)` |
| Expose a port | `await sandbox.exposePort(8080)` → `{ url }` |
| Destroy | `await sandbox.destroy()` |

## exec vs runCode

| Need | Use | Why |
|------|-----|-----|
| Shell commands, scripts, build/test | `exec()` | Direct control, exit codes, stderr, streaming |
| LLM-generated code, data analysis | `runCode()` | Rich outputs (charts/tables), **state persists** in a context |

```typescript
// Code interpreter — recommended for AI-generated code
const ctx = await sandbox.createCodeContext({ language: "python" }); // python | javascript | typescript
await sandbox.runCode("import pandas as pd; data = [1,2,3]", { context: ctx });
const r = await sandbox.runCode("sum(data)", { context: ctx }); // r.results[0].text === "6"
```

Create an explicit context in production so state is scoped deliberately.

## Lifecycle

- `getSandbox()` returns immediately; the container starts **lazily** on first operation.
- Idle containers sleep after ~10 min (`sleepAfter`). `destroy()` frees resources now.
- Same `sandboxId` → same instance. Use a **user/session id**, never a hardcoded shared id.

## Extending the image (keep it lean — cold start)

```dockerfile
FROM docker.io/cloudflare/sandbox:0.7.0   # base: Python 3.11, Node 20, common tools
RUN pip install requests beautifulsoup4
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*
EXPOSE 8080   # required for local-dev port exposure
```

## Preview URLs

`await sandbox.exposePort(8080)` returns a preview URL for an HTTP service inside the sandbox. **In
production this needs a custom domain with wildcard DNS (`*.yourdomain.com`)** — `.workers.dev` does
not serve preview subdomains. See `/sandbox/guides/expose-services/`.

## Anti-patterns

- Don't touch internal clients (`CommandClient`, `FileClient`) — use `sandbox.*`.
- Don't drop the `export { Sandbox }` — deploy fails without it.
- Don't hardcode one sandbox id for multi-user — key by user/session.
- Don't forget `destroy()` on temporary sandboxes.
- Don't trust anything the sandboxed code emits — validate outputs before acting on them.

Adjacent skills: `durable-objects` (the substrate), `cloudflare-agents` (give an agent a sandbox
tool), `workers-best-practices`, `wrangler`.
