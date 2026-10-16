---
name: tauri-desktop
description: >
  Recognizes and works inside a Tauri v2 desktop app — a web frontend (Vite + React)
  driving a Rust backend that ships as one native binary. Fires on a repo with a
  `src-tauri/` directory holding `Cargo.toml` + `tauri.conf.json` (+ `src/main.rs`/`lib.rs`)
  and a `package.json` depending on `@tauri-apps/api` / `@tauri-apps/cli` v2, plus
  `src-tauri/capabilities/*.json`. Use when the user says "run the desktop app",
  "the Anchor app", "add a Tauri command", "invoke isn't working", "the window won't
  open", "tauri dev does nothing", "grant a permission", or "build the installer / MSIX".
  Covers the src-tauri layout, the right dev/build command per app, the v2 capability
  model, IPC, multi-window wiring, and the single-instance zombie-process trap. In navig
  this is Anchor (`apps/anchor`), Echo (`apps/echo`), and the OS super-app (`apps/os`).
  Read-only recognition + workflow guidance; the dev/build commands it suggests only
  touch build output, never user data.
category: desktop
tags: [tauri, desktop, rust, vite, react, ipc, windows]
safety: safe
---

# Tauri v2 desktop apps (navig editions)

One web frontend, one Rust backend, one native binary. This skill is the recognition and
workflow layer for navig's Tauri desktop editions. Deep IPC + permission internals live in
[`references/ipc-and-permissions.md`](references/ipc-and-permissions.md) — pull it in when you
add a command, wire a window, or chase a permission-denied error.

## Recognize it

- A **`src-tauri/`** directory: `Cargo.toml`, `tauri.conf.json`, `src/main.rs` (+ usually `lib.rs`
  and a fan of `*_cmd.rs` command modules — Anchor has `neuromancer_cmd.rs`, `command_center.rs`,
  `tools_cmd.rs`, `tray.rs`, …).
- `package.json` with `@tauri-apps/api` **^2** and `@tauri-apps/cli` **^2**.
- A frontend at the repo root: `index.html`, `vite.config.ts`, `src/` (React 18 in Anchor/Echo).
- **`src-tauri/capabilities/*.json`** — the v2 permission grants. If this folder exists, treat the
  app as capability-gated (deny-by-default).

The three navig editions, so you scope to the right one:

| App | Path | Identity | Frontend | Package mgr |
|-----|------|----------|----------|-------------|
| **Anchor** | `apps/anchor` | `dev.navig.anchor` — the Neuromancer AI text tool | Vite + React 18 | npm |
| **Echo** | `apps/echo` | voice / inbox / chat | Vite + React | npm |
| **OS** | `apps/os` | the Tauri super-app + browser sidecar | (dashboard) | **Bun** |

Anchor and Echo share the **`shared-desktop`** Rust crate (keystroke layer, window helpers) — a
change there hits both; grep both before editing it.

## Run it — read the scripts first, names drift

```powershell
# Anchor / Echo (npm). "dev" is FRONTEND-ONLY (a browser, no native shell):
npm run dev            # apps/anchor: node scripts/dev.mjs → Vite on :7174, pure UI work
npm run tauri:dev      # full app: builds frontend + Rust, hot-reloads — use for anything native
npm run tauri:build    # release: bundles the installer (.msi/.exe on Windows)
npm run build          # frontend production build (tsc && vite build) — feeds tauri:build

# apps/os is Bun, not npm:
#   bun install ; bun run tauri dev

# Rust-only fast checks, from inside src-tauri/:
cargo check            # type-check the backend without a full build
cargo clippy           # lint
```

Reach for `tauri:dev` whenever you touch a `#[tauri::command]`, a native plugin, or a window —
`npm run dev` alone loads the UI in a plain browser where `invoke(...)` and native APIs don't exist.

## Layout that matters

- **`tauri.conf.json`** — `productName`/`identifier`, the `app.windows[]` array (Anchor runs **nine**
  labelled windows: `palette`, `quickpaste`, `command`, `loupe`, `settings`, `consult`, `manager`,
  `recbar`, `recframe`), the CSP under `app.security`, `bundle` (installer/MSIX metadata), and the
  frontend hooks `build.beforeDevCommand` / `beforeBuildCommand` / `devUrl` / `frontendDist`.
- **`capabilities/default.json`** — lists which **windows** get which **permissions**. This is the
  gate: a native call that isn't granted here fails at runtime, and the Rust code is usually fine.
- **`src/lib.rs`** — the `invoke_handler` registering every Rust command. New command → register here.
- **Rust ↔ JS** — commands (`invoke("cmd", args)` ⇄ `#[tauri::command]`) for request/response; events
  (`emit` ⇄ `listen`) for streaming/async pushes.

## Traps (navig-verified)

- **Single-instance zombie.** Anchor/Echo load the `single-instance` plugin. A crashed or
  still-running `tauri:dev` leaves a stray `NAVIG Anchor.exe` holding the lock and the dev port, so a
  fresh run silently opens no window. Kill it first:
  ```powershell
  Get-Process "NAVIG Anchor" -ErrorAction SilentlyContinue | Stop-Process -Force
  ```
  Use the `productName` from `tauri.conf.json` as the process name. Do this any time "tauri dev does
  nothing."
- **Capabilities deny by default.** A new command or plugin that "doesn't work" is almost always a
  missing grant in `capabilities/default.json` — and for a **new window**, its label must be added to
  that file's `windows` array or none of its permissions apply. See the references file.
- **Two compilers, two failure shapes.** A Rust compile error aborts the whole `tauri:dev` even when
  the frontend is clean. Read which half failed before debugging the wrong side.
- **First release build is slow** (full Rust release compile) — not a hang.
- **Keep JS and Rust versions in lockstep.** Bumping `@tauri-apps/*` npm packages without matching the
  `tauri`/plugin crate versions in `Cargo.toml` produces IPC mismatches.
- **CSP is real.** `app.security.csp` in `tauri.conf.json` blocks anything not allow-listed; a new
  `connect-src`/`img-src` origin (e.g. a provider endpoint) must be added there.
- **OS uses Bun.** Don't `npm install` in `apps/os` — it's excluded from the pnpm workspace and expects
  `bun install`.

## Ship (Anchor → Microsoft Store)

Anchor packages as MSIX via `npm run store:msix` (dry run: `store:msix:dry`, wraps
`scripts/create-msix.ps1`). Bundle identity, publisher, and the long description live in
`tauri.conf.json` `bundle`. The remaining Store blockers are human-only (Partner Center, logos, WACK).
