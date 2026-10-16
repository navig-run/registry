# Design Pipeline

## Purpose
Generate a complete CI/CD pipeline configuration for a given platform, language, and deployment target.

## Variables
- `{{PLATFORM}}` — e.g. `github-actions`, `gitlab-ci`, `jenkins`
- `{{LANGUAGE}}` — e.g. `python`, `node`, `go`, `java`
- `{{DEPLOY_TARGET}}` — e.g. `kubernetes`, `ecs`, `lambda`, `vm`
- `{{REGISTRY}}` — container registry: `ghcr.io`, `ecr`, `dockerhub`
- `{{BRANCH_STRATEGY}}` — e.g. `trunk-based`, `gitflow`
- `{{TEST_FRAMEWORK}}` — e.g. `pytest`, `jest`, `go test`

## Prompt

You are a senior CI/CD engineer. Design a production-grade pipeline.

Platform: {{PLATFORM}}
Language: {{LANGUAGE}}
Deploy target: {{DEPLOY_TARGET}}
Container registry: {{REGISTRY}}
Branch strategy: {{BRANCH_STRATEGY}}
Test framework: {{TEST_FRAMEWORK}}

Produce a complete pipeline definition in the native format for {{PLATFORM}}.

Requirements:
1. **Stages** (in order): lint → test → build → push → deploy → post-deploy health check
2. **Caching**: cache dependencies and build artefacts between runs
3. **Parallelism**: lint and test can run in parallel; build follows both
4. **Secrets**: all credentials via environment variables — never hardcoded
5. **Rollback**: deployment step must have a rollback trigger on failure
6. **Branch rules**:
   - PR/MR branches: lint + test only
   - Main/trunk: full pipeline
   - Tags (v*): full pipeline + production deploy
7. **Notifications**: post failure to #pipeline channel

After the pipeline definition, provide:
- **Estimated runtime** (cold / warm cache)
- **Top 3 bottlenecks** and how to address them
- **Security considerations** specific to this stack
