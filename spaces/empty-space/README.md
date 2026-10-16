# {{space-name}}

> {{one-line description}}

**Owner:** {{owner}}  
**Created:** {{ISO-8601 date}}  
**Tier:** personal · **Status:** planned

<!-- Keep this line in sync with .navig/space.json. Switch the status to `active`
once the space ships something that works. -->

> **Template.** This is the blank skeleton a new space starts from. Every
> `{{placeholder}}` here and in `.navig/space.json` / `.navig/space.config.json`
> is filled on first run (see `.navig/GENESIS.md`).

---

## Purpose

<!-- Write one paragraph in your own voice. What is this space for? What do
you want to stop losing track of? What does it feel like when it's working? -->

---

## Structure

```
.navig/          ← all NAVIG metadata, inbox, memory, plans
  space.json     ← canonical manifest (id, tier, status, agents, skills…)
packages/        ← installable space packages
LICENSE          ← MIT
[your files]     ← this root is yours — add whatever the project needs
```

Optional root symlinks (created by `setup-links.sh` / `setup-links.ps1`):
- `inbox → .navig/inbox`
- `docs  → .navig/inbox/docs`
- `plans → .navig/plans`

---

## Quick Start

```bash
# Drop anything into the inbox
cp my-note.md .navig/inbox/

# Let the agent sort it
navig wiki inbox process

# See what's here
navig wiki list
```

---

*Bootstrap guide for AI agents: [`.navig/GENESIS.md`](.navig/GENESIS.md)*
