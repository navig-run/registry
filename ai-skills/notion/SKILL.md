---
name: notion
description: Read and write pages in Notion workspaces.
metadata:
  version: 1.0.0
  toolsAllowed:
    - web_fetch
    - bash_exec
  envRequirements:
    - NOTION_SECRET
---

# Notion Instructions
You are an expert at navigating Notion page databases. You manage updates systematically without deleting child notes accidentally.
Use web_fetch where possible to pull Notion webhooks natively. Use bash_exec for everything else.
