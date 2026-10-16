# devops-space context

## Purpose
This space is the DevOps and Site Reliability Engineering hub. It owns CI/CD pipeline design,
infrastructure-as-code authoring, cloud provisioning, monitoring, and incident response.

## Domain Coverage
- **CI/CD**: GitHub Actions, GitLab CI, Jenkins, CircleCI — pipeline design and optimisation
- **Infrastructure-as-Code**: Terraform, Ansible, Pulumi — provision and manage cloud/on-prem resources
- **Monitoring & Alerting**: Prometheus, Grafana, PagerDuty, Datadog — observability and alerting
- **Incident Response**: on-call runbooks, incident commander protocols, postmortem templates
- **Security & Compliance**: hardening, secrets management, SAST/DAST integration in pipelines
- **SRE Practice**: SLOs, SLIs, error budgets, reliability reviews

## Operating Principles
- Infrastructure is code — everything version-controlled, nothing manual.
- Pipelines fail fast and loud — flaky tests are bugs.
- Every incident produces a blameless postmortem.
- Runbooks are maintained alongside the systems they describe.
- Every change is rolled back-able.
