# Infrastructure as Code

Terraform and Ansible starter projects for provisioning and configuration management.

## Contents

| Folder | Tool | Purpose |
|--------|------|---------|
| `terraform-starter/` | Terraform 1.7+ | VPC, compute, state backend; AWS-default, multi-cloud ready |
| `ansible-starter/` | Ansible 2.15+ | Base server hardening, package management |

## Quick Start — Terraform

```bash
cd terraform-starter
cp terraform.tfvars.example terraform.tfvars  # edit values
terraform init
terraform plan -out=tfplan.txt
terraform apply tfplan.txt
```

## Quick Start — Ansible

```bash
cd ansible-starter
# Edit inventory/hosts.yml
ansible-playbook playbook.yml -i inventory/hosts.yml --check --diff
# Then: ansible-playbook playbook.yml -i inventory/hosts.yml
```

## Agent Assistance

```
@infra-architect review --module terraform-starter/ --env prod
@infra-architect scaffold --cloud aws --pattern vpc-3tier
```
