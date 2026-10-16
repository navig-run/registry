# Ansible Starter

Starter Ansible project for server provisioning and configuration management.

## Structure

```
ansible-starter/
├── playbook.yml              ← Main playbook
├── inventory/
│   └── hosts.yml             ← Inventory template
├── group_vars/
│   └── all.yml               ← Shared variables
└── README.md
```

## Usage

```bash
# Dry run (check + diff — run this first)
ansible-playbook playbook.yml -i inventory/hosts.yml --check --diff

# Apply
ansible-playbook playbook.yml -i inventory/hosts.yml

# Single host
ansible-playbook playbook.yml -i inventory/hosts.yml --limit <hostname>
```

## Agent Assistance

```
@infra-architect scaffold --tool ansible --env prod
```
