# Day 39 - Ansible on Self-Hosted Runner (A to Z)

## Overview
This project demonstrates how to execute Ansible playbooks through GitHub Actions using a Self-Hosted Runner running on Ubuntu 24.04 WSL2 (ARM64).

## Objectives
- Understand Ansible execution in CI/CD
- Execute playbooks from GitHub Actions
- Use a Self-Hosted Runner
- Automate Linux tasks
- Verify workflow execution

## Architecture

```text
GitHub Repository
        │
        ▼
GitHub Actions
        │
        ▼
Self-Hosted Runner
(khalid-wsl-runner)
        │
        ▼
Ubuntu 24.04 WSL2
        │
        ▼
Ansible Playbook
        │
        ▼
Linux Automation
```
## Step  – Create Project Structure

Inside your repository:

```test
test-github-actions
│
├── ansible
│   ├── inventory.ini
│   └── test.yml
│
└── .github
    └── workflows
        └── ansible-test.yml
```

## Inventory

```ini
[local]
localhost ansible_connection=local
```

## Playbook

```yaml
---
- name: Test Ansible Playbook
  hosts: local
  gather_facts: yes

  tasks:
    - name: Show hostname
      debug:
        msg: "Hostname is {{ ansible_hostname }}"

    - name: Show operating system
      debug:
        msg: "{{ ansible_distribution }} {{ ansible_distribution_version }}"

    - name: Create test file
      file:
        path: /tmp/github-actions-ansible.txt
        state: touch
```

## Workflow

```yaml
name: Ansible Self Hosted Test

on:
  workflow_dispatch:

jobs:
  ansible-test:
    runs-on: [self-hosted, Linux, ARM64]

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Verify Ansible
        run: ansible --version

      - name: Run Playbook
        run: ansible-playbook -i ansible/inventory.ini ansible/test.yml
```

## Validation

```bash
ls -l /tmp/github-actions-ansible.txt
```

Result:

```text
-rw-r--r-- 1 khalid khalid 0 Jun 4 12:33 /tmp/github-actions-ansible.txt
```

## Skills Demonstrated

- GitHub Actions
- Ansible
- YAML
- Linux Administration
- Ubuntu WSL2
- Self-Hosted Runner
- CI/CD
- Automation

## Summary

Successfully executed Ansible playbooks through GitHub Actions using a Self-Hosted Runner on Ubuntu 24.04 WSL2 ARM64.
