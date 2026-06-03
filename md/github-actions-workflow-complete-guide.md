# GitHub Actions Workflow - Complete A to Z Guide

## What is a Workflow?

A workflow is an automated process executed by GitHub Actions.

It tells GitHub:
- When to run
- What to do
- In what order
- On which machine

A workflow is defined in a YAML file.

---

## Why Use Workflows?

Workflows automate:
- Testing
- Linting
- Building applications
- Deployments
- Security scans
- Notifications

Benefits:
- Automation
- Consistency
- Reliability
- Faster delivery

---

## Workflow File Location

```text
.github/workflows/
```

Example:

```text
.github/
└── workflows/
    ├── hello.yml
    ├── portfolio.yml
    ├── python-lint.yml
    └── cicd.yml
```

---

## Basic Workflow Structure

```yaml
name: My Workflow

on:
  push:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - run: echo "Hello World"
```

---

## Main Components

| Component | Purpose |
|-----------|---------|
| Workflow | Entire automation |
| Trigger | When workflow runs |
| Job | Group of tasks |
| Step | Individual task |
| Action | Reusable automation |
| Runner | Machine executing workflow |

---

## Triggers

### Push

```yaml
on:
  push:
```

### Pull Request

```yaml
on:
  pull_request:
```

### Manual Run

```yaml
on:
  workflow_dispatch:
```

---

## Jobs

Example:

```yaml
jobs:
  build:
```

Pipeline example:

```text
Code
 ↓
Build
 ↓
Test
 ↓
Deploy
```

---

## Runners

```yaml
runs-on: ubuntu-latest
```

Other examples:

```yaml
runs-on: windows-latest
runs-on: macos-latest
```

---

## Steps

```yaml
steps:
  - run: echo "Hello"
```

Steps are the actual tasks executed.

---

## Actions

Examples:

```yaml
uses: actions/checkout@v4
uses: actions/setup-python@v4
uses: actions/configure-pages@v4
```

Actions are reusable workflow components.

---

## Matrix Strategy

```yaml
strategy:
  matrix:
    python-version:
      - '3.9'
      - '3.10'
      - '3.11'
      - '3.12'
      - '3.13'
```

Creates multiple jobs:

```text
validate (3.9)
validate (3.10)
validate (3.11)
validate (3.12)
validate (3.13)
```

---

## Dependencies

```yaml
build:
  needs: code
```

Flow:

```text
code
 ↓
build
```

---

## Conditions

```yaml
if: inputs.environment == 'production'
```

Runs only when production is selected.

---

## Inputs

```yaml
inputs:
  environment:
```

Example dropdown:

```text
development
staging
production
```

---

## Artifacts

Example:

```yaml
uses: actions/upload-pages-artifact@v4
```

Used to transfer files between jobs or deployments.

---

## Environment Variables

```yaml
env:
  APP_ENV: production
```

Usage:

```bash
echo $APP_ENV
```

---

## Secrets

Store:
- Passwords
- Tokens
- API Keys

Usage:

```yaml
${{ secrets.MY_SECRET }}
```

---

## Real Examples

### Hello Workflow

```text
Push
 ↓
Hello Message
```

### Python Lint

```text
Push
 ↓
Setup Python
 ↓
Install Dependencies
 ↓
Run flake8
```

### Portfolio Deployment

```text
Push
 ↓
Checkout Code
 ↓
Configure Pages
 ↓
Upload Artifact
 ↓
Deploy Website
```

---

## Workflow vs Job vs Step

```text
Workflow
│
├── Job
│   ├── Step
│   ├── Step
│   └── Step
│
└── Job
    ├── Step
    └── Step
```

---

## Best Practices

- Use meaningful names
- Keep workflows simple
- Store secrets securely
- Use matrix testing when needed
- Reuse actions
- Test workflows regularly

---

## Interview Questions

### What is a Workflow?

An automated process defined in YAML.

### What is a Job?

A group of related steps.

### What is a Step?

An individual task executed in a job.

### What is a Runner?

The machine executing workflow jobs.

### What is Matrix Strategy?

Running the same job across multiple versions.

### What is workflow_dispatch?

Manual workflow execution.

---

## Final Summary

```text
Trigger
   ↓
Workflow
   ↓
Job(s)
   ↓
Step(s)
   ↓
Result
```

### One-Line Summary

A GitHub Actions Workflow is an automated process that defines when GitHub should run, what jobs should execute, and what steps should be performed to automate testing, building, and deployment.
