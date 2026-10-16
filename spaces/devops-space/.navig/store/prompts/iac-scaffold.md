# IaC Scaffold

## Purpose
Generate a complete Infrastructure-as-Code scaffold for a given cloud provider and pattern.
Used by the Infra Architect agent.

## Variables
- `{{CLOUD}}` — `aws`, `gcp`, `azure`, `hetzner`, `digitalocean`
- `{{PATTERN}}` — e.g. `vpc-3tier`, `single-server`, `k8s-cluster`, `serverless-api`
- `{{REGION}}` — e.g. `us-east-1`, `eu-west-1`
- `{{TOOL}}` — `terraform`, `pulumi`, `ansible`
- `{{ENVIRONMENT}}` — `dev`, `staging`, `prod`
- `{{NAMING_PREFIX}}` — e.g. `navig-prod`

## Prompt

You are a senior infrastructure architect. Generate a complete IaC scaffold.

Cloud: {{CLOUD}}
Pattern: {{PATTERN}}
Region: {{REGION}}
Tool: {{TOOL}}
Environment: {{ENVIRONMENT}}
Naming prefix: {{NAMING_PREFIX}}

Produce the following files:

For Terraform:
1. `main.tf` — resource definitions
2. `variables.tf` — all input variables with descriptions and defaults
3. `outputs.tf` — useful outputs (IDs, endpoints, ARNs)
4. `versions.tf` — required providers and version constraints
5. `terraform.tfvars.example` — example values (real values never in repo)

For Ansible:
1. `playbook.yml` — main playbook
2. `inventory/hosts.yml` — inventory template
3. `group_vars/all.yml` — shared variables

Requirements:
- All resources tagged with: `env={{ENVIRONMENT}}`, `managed-by=terraform`, `prefix={{NAMING_PREFIX}}`
- No hardcoded credentials — all from variables or environment
- Include security group / firewall rules — deny by default, explicit allows only
- Add comments explaining non-obvious decisions
- Backend config (S3/GCS/Azure Blob for Terraform state) stub included
