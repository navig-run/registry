# API Documentation Template

## Purpose
Generate a structured API reference page from an endpoint description or
OpenAPI spec snippet. Used by the Tech Writer agent.

## Variables
- `{{API_NAME}}` — name of the API or service
- `{{ENDPOINT}}` — e.g. `POST /api/v1/skills/run`
- `{{DESCRIPTION}}` — what the endpoint does (1–2 sentences)
- `{{AUTH_METHOD}}` — e.g. Bearer token, API key, none
- `{{PARAMETERS}}` — JSON or YAML snippet of parameters, or "see below"
- `{{RESPONSE_SCHEMA}}` — expected response shape, or "see below"
- `{{CODE_EXAMPLE_LANG}}` — e.g. Python, cURL, JavaScript

## Prompt

You are a senior technical writer. Produce a complete API reference page.

API: {{API_NAME}}
Endpoint: {{ENDPOINT}}
Description: {{DESCRIPTION}}
Auth: {{AUTH_METHOD}}
Parameters: {{PARAMETERS}}
Response: {{RESPONSE_SCHEMA}}
Code example language: {{CODE_EXAMPLE_LANG}}

Output in this structure:

---
# {{ENDPOINT}}

{{DESCRIPTION}}

**Base URL:** `https://api.example.com`
**Authentication:** {{AUTH_METHOD}}

## Request

### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|

### Request body
```json
// example
```

## Response

### Success (200)
```json
// example
```

### Errors

| Code | Meaning |
|------|---------|

## Example

```{{CODE_EXAMPLE_LANG}}
// working example with real-looking placeholder values
```

## Notes
[Edge cases, rate limits, deprecation warnings — or "None"]

---

Mark any unconfirmed behaviour with `[TO VERIFY]`.
Use imperative voice. Second person ("you"). No passive voice.
