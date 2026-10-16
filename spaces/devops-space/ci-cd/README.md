# CI/CD Templates

Pipeline templates and workflow definitions for common project types.

## Contents

| File/Folder | Purpose |
|-------------|---------|
| `github-actions-python.yml` | GitHub Actions CI for Python projects |

## Adding a New Template

1. Author the pipeline file in this folder
2. Test it in a real project
3. Add an entry to this README
4. If complex — add a prompt to `.navig/store/prompts/design-pipeline.md`

## Agent Assistance

```
@pipeline-engineer design --platform github-actions --language <lang> --deploy <target>
```
