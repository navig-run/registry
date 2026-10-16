---
name: nextjs-app
description: >
  Recognizes and works inside a Next.js App Router app — the `app/` directory model with
  React Server/Client Components. Fires on a repo with an `app/` dir (`layout.tsx` +
  `page.tsx`, no `pages/`), `next` at 15/16, `react` 19, and typically Tailwind v4
  (`@tailwindcss/postcss`, `@import "tailwindcss"` in `globals.css`) with optional shadcn/ui.
  Use when the user says "work in the deck", "add a page/route", "Next.js App Router",
  "make a server action", "why is useState erroring in a server component", "the fetch
  fails", "wire the UI to the API", or "deploy the deck". Covers App Router conventions,
  the server/client boundary, data/route handlers, Tailwind v4's config-in-CSS model, and
  navig's static-export-to-Cloudflare path. In navig this is the deck (`apps/deck`) — the
  control UI / Telegram Mini App that talks to core over `/api/deck/*`. Read-only
  recognition + workflow guidance; suggested dev/build commands touch build output only.
category: frontend
tags: [nextjs, react, app-router, tailwind, shadcn, frontend]
safety: safe
---

# Next.js App Router apps (navig deck)

The `app/` directory, Server Components by default, Client Components opt-in. This skill recognizes an
App Router project and gives you the conventions to work in one without tripping the server/client
boundary. navig's live example is the **deck** (`apps/deck`) — the Next.js control UI and Telegram
Mini App.

## Recognize it

- An **`app/`** directory with `layout.tsx` + `page.tsx`, and **no** `pages/` directory (that would be
  the legacy Pages Router).
- `next` at **15 or 16**, `react` / `react-dom` at **19** (the deck: Next 16.1.6, React 19.2.4).
- **Tailwind v4** signature: `@tailwindcss/postcss` in devDeps and `@import "tailwindcss";` in
  `app/globals.css` — config lives in CSS via `@theme`, usually **no `tailwind.config.js`**.
- Optional shadcn/ui: `components.json`, `components/ui/*`, a `cn()` helper in `lib/utils.ts`,
  `class-variance-authority` + `tailwind-merge` + `lucide-react`.

Disambiguate: a `src-tauri/` present → **`tauri-desktop`**. Vite + `react-router-dom` (no `app/`) →
**`vite-react-spa`**.

## Run it — read the scripts, ports drift

```powershell
npm install           # or pnpm install
npm run dev           # apps/deck: next dev on :7432 (dev mode = normal Next, so rewrites work)
npm run build         # next build
npm run start         # serve the production build (deck: -p 7432)
npm run lint          # eslint
npm run typecheck     # tsc --noEmit — keep YOUR changed files at zero errors
```

## App Router conventions

- **Routes are folders under `app/`.** A route renders when the folder has a `page.tsx`. The shared
  shell is `app/layout.tsx`; per-segment `loading.tsx` / `error.tsx` / `not-found.tsx` supply the
  streaming, error, and empty states. A new screen = a new `app/<segment>/page.tsx`.
- **Server Components by default; Client Components opt in.** A file is a Server Component unless it
  starts with `"use client"`. Hooks (`useState`, `useEffect`), event handlers, and browser APIs only
  work in client components. Keep the boundary as low in the tree as possible — mark the small
  interactive leaf, not the whole page.
- **Data & mutations.** Route Handlers live at `app/api/<name>/route.ts` (export `GET`/`POST`/…);
  Server Actions are `"use server"` functions callable from a form or a client component. Check which
  exists before wiring a button to it.
- **Styling (Tailwind v4).** Utilities in JSX; theme tokens declared in `globals.css` via `@theme` and
  CSS variables — **not** a JS config. The deck consumes navig design tokens
  (`app/navig-tokens.generated.css`); edit the token source, not the generated file.
- **Path alias.** `@/` → project root (see `tsconfig.json` `paths`).

## navig deck specifics — where the backend actually is

The deck is a **thin control surface over the local daemon**, not a self-contained app:

- In **dev**, `next.config.mjs` runs a normal Next server and **rewrites** `/api/deck/*`,
  `/api/daemon`, `/runtime`, `/mesh`, `/api/events` to the **gateway on `:8789`** (override with
  `NAVIG_DAEMON_URL`). So `npm run dev` talks to an already-running daemon — no second daemon, no CORS
  layer. Don't add a manual proxy; the rewrite is the seam.
- The gateway (default **8789**) serves the deck API + SSE. This is **not** the IPC/MCP daemon (8765) —
  wiring a call to the wrong port is a classic dead end.
- In **build/prod** the deck is a **static export** (`output: "export"`), deployed by a pure-Python
  uploader (`core/navig/cloud/deck_deploy.py`) to Cloudflare Workers Static Assets. The edge brain URL
  is baked in via `NEXT_PUBLIC_LIGHTHOUSE_URL` at build time.

## Traps

- **Server/Client boundary errors.** "useState is not a function" / "cannot be used in a Server
  Component" means a missing `"use client"` — add it to the interactive file, not the whole subtree.
- **Static export constraints.** Because prod is `output: "export"`, features that need a Node server
  at runtime don't apply: `images.unoptimized` is on (no on-the-fly image optimization), and Route
  Handlers/Server Actions won't run on the static edge — dynamic behavior comes from the daemon the
  deck calls, not from Next server code in prod. Verify a data path works **exported**, not just in
  `next dev`.
- **Browser env vars must be `NEXT_PUBLIC_`-prefixed** or they're `undefined` client-side.
- **Tailwind v4 ≠ v3.** No `tailwind.config.js` to edit — customize via `@theme`/CSS variables. Adding
  a v3-style JS config does nothing.
- **shadcn components are yours.** They're copied into `components/ui/*`, editable source — not a
  version-locked dependency. Edit them directly.
- **React 19 peer-dep lag.** Some libraries trail on peer ranges; prefer pinning a compatible version
  over reaching for `--legacy-peer-deps`.

## Publish discipline

The deck is a public surface. When you change what it renders or how it talks to core, update the
relevant `docs/` page and the deck `CHANGELOG.md` in the same change (MASTER § Publish discipline), and
note where the canonical data/route lives so the next agent doesn't guess the port.
