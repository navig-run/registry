---
id: summarise-url
name: Summarise URL
version: 1.0.0
category: research
license: MIT
platforms: [linux, macos, windows]
tags: [web, summarisation, research, nlp]
tools: []
safety: safe
user_invocable: true
soul_hint: "Keep summaries factual and concise. Preserve key figures and proper nouns. Distinguish between opinions and verified facts."
---

# Purpose

Fetch a URL and return a structured summary of its content — title, key points, and a concise prose summary. Preserves factual accuracy over brevity.

# When to use

- User shares a URL and asks for a summary, overview, or key takeaways
- User says "summarise this", "what's on this page", "tldr for this link"
- Trigger type: `/summarise` command or agent task type `research`

# Instructions

1. Fetch the URL content (use browser rendering if JS-gated)
2. Extract: page title, main body text, key entities and figures
3. Produce a concise summary (default max 300 words, configurable)
4. List 3–5 key points as bullet points
5. Flag if the content is paywalled, empty, or non-textual
6. Never fabricate details — only use what is on the page

# Inputs

| Field | Type | Required | Default |
|-------|------|----------|---------|
| `url` | string (URI) | yes | — |
| `max_length` | integer (words) | no | 300 |

# Output format

```json
{
  "title":      "Page Title",
  "summary":    "Concise prose summary...",
  "key_points": ["Point one", "Point two", "Point three"],
  "source_url": "https://example.com/article"
}
```

# Examples

```bash
# Summarise an article
/summarise https://example.com/blog/new-feature

# With a custom word limit
navig skill run summarise-url --url https://docs.example.com --max_length 150
```

# Agent hints

After summarising, offer to extract named entities, translate, or generate a social post from the summary.
If the page is paywalled, offer to search for an archive or alternative source.
