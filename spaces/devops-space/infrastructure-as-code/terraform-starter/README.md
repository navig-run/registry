# Terraform Starter

Starter Terraform module with best-practice structure. Replace placeholder values and extend as needed.

## Structure

```
terraform-starter/
├── main.tf            ← Resource definitions
├── variables.tf       ← Input variables
├── outputs.tf         ← Outputs
├── versions.tf        ← Provider version constraints
├── terraform.tfvars.example ← Example variable values (commit this; gitignore terraform.tfvars)
└── README.md
```

## Usage

```bash
# 1. Copy terraform.tfvars.example → terraform.tfvars and fill in values
cp terraform.tfvars.example terraform.tfvars

# 2. Initialise
terraform init

# 3. Plan — review before applying
terraform plan -out=tfplan.txt

# 4. Apply — get operator approval first for prod
terraform apply tfplan.txt
```

## Agent Assistance

```
@infra-architect review --plan terraform-starter/tfplan.txt
@infra-architect scaffold --cloud aws --pattern vpc-3tier --env prod --prefix myapp
```
