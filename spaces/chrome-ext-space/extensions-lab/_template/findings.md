# Findings Report — [Extension Name]

**Extension:** _(fill in)_
**Version:** _(fill in)_
**Risk Rating:** `LOW` / `MEDIUM` / `HIGH` / `CRITICAL` ← _(pick one)_
**Date:** _(fill in)_

---

## 1. Manifest Analysis

### Manifest Version
- [ ] MV2 (deprecated — background pages, broad webRequest)
- [ ] MV3 (current — service worker, declarativeNetRequest)

### Declared Permissions

| Permission | Purpose Claimed | Risk |
|-----------|----------------|------|
| _(paste permissions here)_ | | |

### Host Permissions

| Pattern | Scope |
|---------|-------|
| | |

### Content Scripts

| Match Pattern | Script | Run At |
|--------------|--------|--------|
| | | |

### web_accessible_resources
_(list any, note if accessible from untrusted pages)_

### CSP
```
_(paste content_security_policy value here)_
```
Flags: `'unsafe-eval'` present: ☐  External script sources: ☐

---

## 2. Execution Flow

_(Summary of what happens from install → background worker start → content script injection → user interaction)_

### Background / Service Worker
_(what it does on startup, what events it listens to)_

### Content Scripts
_(what pages they inject into, what they read/modify, what they send back)_

### Message Passing
_(background ↔ content ↔ popup communication flows)_

### External Requests
| Endpoint | When | What's Sent | What's Received |
|---------|------|------------|----------------|
| | | | |

---

## 3. Security Findings

| # | Finding | Location | Severity | Recommendation |
|---|---------|----------|----------|---------------|
| 1 | | | | |

### Over-Privilege Assessment
_(Are claimed permissions actually used? Which ones are unnecessary?)_

### Data Exfiltration Risk
_(Does the extension send user data to external servers? What data?)_

### Code Quality Red Flags
- `eval()` usage: ☐
- Dynamic `import()` from external URLs: ☐
- `innerHTML` with unsanitized data: ☐
- `chrome.storage` storing sensitive data: ☐

---

## 4. Summary

_(2-3 sentence executive summary of what this extension does and whether it's safe to use)_

**Recommendation:** Install ☐  Avoid ☐  Investigate Further ☐
