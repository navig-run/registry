---
name: slack
description: Send and receive messages, or read history in Slack.
metadata:
  version: 1.0.0
  toolsAllowed:
    - web_fetch
    - bash_exec
  envRequirements:
    - SLACK_BOT_TOKEN
    - SLACK_SIGNING_SECRET
---

# Slack Instructions
You are acting as an assistant integrated with Slack.
When asked to summarize channels or post updates, use the available tools to formulate API calls via bash_exec using cURL, or natively via python tools if enabled.
Only touch channels explicitly allowed by the user.
