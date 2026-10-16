---
name: vite-react-spa
description: >
  Recognizes and works inside a Vite + React single-page app — a client-rendered React
  app built by Vite, usually routed with React Router, sometimes paired with a small
  Express server sharing a typed contract. Fires on a repo with `vite.config.ts` + an
  `index.html` entry + `react`/`react-dom`, and (for the full-stack shape) side-by-side
  `client/` `server/` `shared/` directories, `react-router-dom`, TanStack Query, and Zod.
  Use when the user says "run the Vite app", "add a page/route", "the dev server won't
  start", "wire this component to the API", "where do the shared types live", or "the
  Express endpoint 404s". Covers dev/build/test commands, where UI vs server vs shared
  contract lives, the single-origin dev server, and the "don't trust the template
  scaffolding" rule for cloned starters. Read-only recognition + workflow guidance;
  suggested dev/build/test commands touch build output only.
category: frontend
tags: [vite, react, spa, react-router, express, frontend]
safety: safe
---

# Vite + React SPA (± Express)

A client-rendered React app that Vite builds, often with a thin Express server behind a shared, typed
contract. This skill recognizes the shape fast and — crucially — reads **past** identical starter
scaffolding to the app's real intent. It covers both the pure-frontend SPA and the full-stack
`client/server/shared` variant.

## Recognize it

- **`vite.config.ts`** (or `.js`) + an **`index.html`** entry + `react` / `react-dom` in
  `package.json`. That's the SPA baseline.
- Client-side routing via **`react-router-dom`** (a route table in `App.tsx`/`main.tsx`) — an SPA, not
  file-system routing.
- **Full-stack variant:** top-level `client/`, `server/`, `shared/` dirs side by side; `express` in
  deps; a `vite.config.ts` that mounts the Express app as dev middleware; often TanStack Query + Zod,
  a `@radix-ui/*`/shadcn cluster, and an `AGENTS.md` instead of a `README.md`.

Disambiguate: an `app/` dir with Next → **`nextjs-app`**. A `src-tauri/` → **`tauri-desktop`** (the
navig Anchor/Echo frontends *are* Vite + React, but wrapped by Tauri — use that skill for the native
side; the Vite patterns here still apply to their UI).

## Run it — read `package.json` scripts first (names drift)

```bash
npm install           # or pnpm install
npm run dev           # Vite dev server (full-stack variant: Vite + Express on ONE port)
npm run build         # production build (client + server bundle in the full-stack variant)
npm start             # run the built server (full-stack) / preview the build
npm test              # Vitest, if present
npm run typecheck     # tsc --noEmit (sometimes "type-check")
```

In the full-stack variant there is **no separate backend port** in dev — Express runs *inside* Vite as
middleware, so `/api/*` calls hit the same origin with no proxy and no CORS layer. Don't add one; check
`vite.config.ts` first.

## Where things live

| Concern | Pure SPA | Full-stack (`client/server/shared`) |
|---------|----------|-------------------------------------|
| Pages | `src/pages/*` | `client/pages/*` |
| Components | `src/components/*` (`ui/` = shadcn primitives) | `client/components/*` |
| Route table | `src/App.tsx` / `main.tsx` | `client/App.tsx` |
| API handlers | — | `server/` (Express app + routes; `server/index.ts` exports the app) |
| Shared contract | — | `shared/` — types + Zod schemas imported by **both** sides |
| Path alias | `@/` → `src/` | `@/` → `client/`, `@shared/` → `shared/` (check `tsconfig.json` + `vite.config.ts`) |

- **Routing** is a React Router table — a new screen is a `pages/*` file wired into it.
- **Data fetching** — TanStack Query on the client; validate payloads with the Zod schemas from
  `shared/` so the client and server agree on shape.
- **Styling** — Tailwind (v3 with a `tailwind.config.ts` `content` glob, or v4 config-in-CSS) plus CSS
  variables for theming.

## Traps

- **Don't trust the scaffolding — derive intent from the code.** Cloned starters (Builder.io Fusion,
  bootstrap templates) share identical files, names, and `AGENTS.md` across many repos; the template
  metadata tells you nothing about *this* app. Read the actual `pages/*` and `server/routes/*` to learn
  what it does. Two repos off the same starter are not related.
- **`AGENTS.md` over a missing README.** Many starters ship guidance in `AGENTS.md` and no `README.md` —
  read it before assuming conventions.
- **The Express server is often half-wired** in prototypes — endpoints may be stubs. Confirm a route
  exists in `server/` before calling it from the client.
- **One origin in dev.** Don't add a manual proxy or CORS expecting a split front/back — the Vite
  middleware serves both.
- **Keep new routes in `server/`** so both the dev middleware and any deploy wrapper (a Netlify/edge
  function importing the same Express app) pick them up — don't duplicate a handler in the function
  entry.
- **SPA routing needs a fallback.** A client-routed build serves `index.html` for unknown paths; a
  static host without a rewrite-to-index rule will 404 on deep links — configure the fallback.
