# Tests

Smoke tests, integration tests, and validation scripts for devops-space assets.

## Running Tests

```bash
# All skill smoke tests
pytest tests/ -q

# Single skill test
pytest tests/test_health_probe.py -q
```

## Writing a Test

1. Create `test_<skill_name>.py`
2. Mock external calls (HTTP, SSH, Docker daemon)
3. Assert skill returns expected status string

## Index

| Test File | Covers |
|-----------|--------|
| _(Add test files here)_ | |
