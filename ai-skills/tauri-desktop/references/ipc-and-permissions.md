# Tauri v2 — IPC, capabilities, and multi-window wiring

Deep detail for adding commands, windows, and permissions to a navig Tauri edition
(Anchor / Echo / OS). Load when the router in `SKILL.md` sends you here. This describes
Tauri v2 patterns as used in this repo — verify exact API names against the official
Tauri v2 docs when in doubt; do not invent permission identifiers.

## IPC — commands vs events

Two channels, chosen by shape:

- **Command** = request → response. A Rust `#[tauri::command] fn foo(...) -> Result<T, E>` registered
  in the `invoke_handler`; the frontend calls `invoke("foo", { arg })` and awaits a value. Use for
  "do X and give me the answer" (e.g. run a Neuromancer action, read config).
- **Event** = fire-and-forget push, either direction. Rust `app.emit("channel", payload)`; JS
  `listen("channel", cb)` (and the reverse). Use for streaming tokens, progress, recording state — no
  reply expected.

### Add a Rust command — checklist

1. Write `#[tauri::command] async fn my_cmd(...) -> Result<Out, String>` in the right `*_cmd.rs`
   module (group by feature: `neuromancer_cmd.rs`, `tools_cmd.rs`, `loupe_cmd.rs`).
2. **Register it** in the `invoke_handler![...]` list in `src/lib.rs`. Forgetting this is the #1 cause
   of `Command my_cmd not found`.
3. Call from the frontend: `import { invoke } from "@tauri-apps/api/core"; await invoke("my_cmd", {...})`.
4. Argument names are camelCase on the JS side, snake_case in Rust — Tauri bridges the case. Mismatched
   names surface as missing/`undefined` args, not an error.
5. Return `Result<_, String>` (or a serde-serializable error) so failures reject the JS promise instead
   of panicking the backend.

## The v2 capability model

Tauri v2 is **deny-by-default**. A window can only touch a plugin/core API if a capability file grants
that permission **to that window**. Anchor's grants live in `src-tauri/capabilities/default.json`:

```jsonc
{
  "identifier": "default",
  "windows": ["palette", "command", "quickpaste", "loupe", "settings", "consult",
              "manager", "recbar", "recframe"],   // which windows this capability applies to
  "permissions": [
    "core:default",
    "core:window:allow-set-focus",
    "core:window:allow-show",
    "clipboard-manager:allow-read-text",
    "global-shortcut:allow-register",
    "autostart:allow-enable"
    // …
  ]
}
```

Permission identifier grammar:

- **`core:<module>:<permission>`** — built-in surfaces: `core:window:allow-show`,
  `core:event:default`, `core:app:default`.
- **`<plugin>:<permission>`** — a plugin's grants: `clipboard-manager:allow-write-text`,
  `global-shortcut:allow-register`, `notification:default`, `fs:default`, `shell:allow-execute`.
- **`<scope>:default`** — the plugin author's recommended baseline bundle.

### Add a permission — checklist

1. Identify the failing call. A runtime error like *"clipboard-manager.read_text not allowed"* names the
   exact permission you're missing.
2. Add the identifier (e.g. `"clipboard-manager:allow-read-text"`) to the `permissions` array in
   `capabilities/default.json`.
3. Confirm the calling **window's label** is in that capability's `windows` array (see below).
4. Restart `tauri:dev` — capability files are read at build/start, not hot-reloaded.

## Multi-window wiring (Anchor runs nine)

Each window is a `tauri.conf.json` `app.windows[]` entry with a unique `label`, its own `url`
(`index.html?win=<label>` — the frontend reads `win` to pick which surface to render), and geometry
(most Anchor windows are `decorations: false`, `transparent: true`, `alwaysOnTop: true`, `visible:
false` and get shown on demand).

### Add a window — checklist

1. Append a `{ "label": "myWin", "url": "index.html?win=myWin", ... }` object to `app.windows[]` in
   `tauri.conf.json`.
2. **Add `"myWin"` to the `windows` array in `capabilities/default.json`** — omit this and the window
   opens but every native call from it is silently denied.
3. Branch on `?win=myWin` in the frontend router so it renders the right component.
4. Show it from Rust (`window.show()` / a command) or from JS via the window API. Windows start hidden
   (`visible: false`) by design — the app reveals them on hotkey/tray action.

## Plugins in play (Anchor)

`tauri.conf.json` `plugins`: `window-state` (remembers window geometry), `log`, `single-instance`
(one running app — the source of the zombie-process trap), `shell`. Each plugin needs its crate in
`Cargo.toml`, its init in `lib.rs`, and its permissions in the capability file — three places, keep them
in sync.
