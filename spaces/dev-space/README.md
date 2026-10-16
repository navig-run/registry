# NAVIG Dev Space

**Code authoring, userscript development, and browser extension engineering hub.**

---

## What It Is

A NAVIG space for building client-side automation — Greasemonkey userscripts,
Chrome/Firefox Manifest V3 extensions, and general development projects.
Fork it, configure your target sites, and start shipping in minutes.

---

## Quick Start

1. **Install NAVIG** — see [navig.run/install](https://navig.run/install)
2. **Install and activate this space**
   ```bash
   navig space install github:navig-run/registry/spaces/dev-space
   navig space use dev-space
   ```
   The space ships example state only — copy each `.navig/memory/*.example.json` to
   `*.json` and `.navig/inbox/routes.example.yaml` to `routes.yaml`, then edit them.
3. **Scaffold your first userscript**
   ```bash
   navig skill run scaffold-project --type userscript --name my-script --match "https://example.com/*"
   ```
4. **Scaffold a Chrome extension**
   ```bash
   navig skill run scaffold-project --type chrome-extension --name my-extension
   ```
5. **Run the daily standup** (workflows in `.navig/store/workflows/` are playbooks the agents follow)
   ```bash
   navig ask "run the daily-standup workflow"
   ```

---

## Space Structure

```
dev-space/
├── .navig/
│   ├── store/
│   │   ├── agents/        ← coder · debugger · reviewer · scripter
│   │   ├── formations/    ← dev-workflow · review-cycle · extension-build
│   │   ├── prompts/       ← scaffold-userscript · scaffold-extension · debug-session · code-review
│   │   └── workflows/     ← daily-standup · code-review · run-tests
│   ├── skills/            ← code-lint · run-tests · scaffold-project · publish-extension
│   └── wiki/              ← architecture · agent-guide · runbooks
├── userscripts-workshop/  ← Greasemonkey/Tampermonkey starter template
├── chrome-extensions-workshop/ ← Manifest V3 extension starter
├── scripts/               ← Automation scripts
├── docs/                  ← Documentation
└── tests/                 ← Skill and workflow tests
```

---

## Agents

| Agent | Role | Inbox |
|-------|------|-------|
| coder | Code scaffolding and implementation | `#code` |
| debugger | Bug investigation and tracing | `#debug` |
| reviewer | Code review and quality checks | `#review` |
| scripter | Userscript and extension specialist | `#extensions` |

---

## Formations

| Formation | Lead | Use Case |
|-----------|------|----------|
| dev-workflow | coder | General authoring and debugging |
| review-cycle | reviewer | Code review and refactoring |
| extension-build | scripter | Extension and userscript packaging |

---

## Skills

| Skill | Platform | Description |
|-------|----------|-------------|
| `code-lint` | All | ESLint / flake8 static analysis |
| `run-tests` | All | Jest / pytest test runner |
| `scaffold-project` | All | Generate project skeleton from template |
| `publish-extension` | All | Package and publish browser extensions |

---

## Prompts

| Prompt | Purpose |
|--------|---------|
| `scaffold-userscript` | Generate a complete userscript with metadata block |
| `scaffold-extension` | Generate a complete MV3 extension skeleton |
| `debug-session` | Structured debugging with root-cause analysis |
| `code-review` | Scored code review with actionable findings |

---

## Sub-Workspaces

| Folder | Contents |
|--------|---------|
| `userscripts-workshop/` | Starter `.user.js` template with full metadata block and authoring guide |
| `chrome-extensions-workshop/` | MV3 `manifest.json`, `background.js`, `content.js`, popup, and loading guide |

---

## Requirements

| Tool | Required | Purpose |
|------|----------|---------|
| NAVIG ≥ 2.0.0 | Yes | Space runtime |
| Node.js | Optional | ESLint and Jest |
| Python 3.x | Optional | flake8 and pytest |

---

## Contributing

See [CONTRIBUTING.md](../../CONTRIBUTING.md) and submit issues at [github.com/navig-run/registry](https://github.com/navig-run/registry).

## License

MIT — see [LICENSE](LICENSE)
