# Tests

Skill and workflow tests for the dev space.

## Naming Convention

`test-<skill-or-workflow-id>.<ext>` — e.g. `test-code-lint.js`, `test-run-tests.sh`

## Running Tests

```bash
# Run via npm (if package.json configured)
npm test

# Run directly (JS)
node tests/test-code-lint.js

# Run directly (Python)
py -3 -m pytest tests/
```
