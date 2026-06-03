# GitHub Actions CI/CD Workflow - Block by Block Explanation

## Complete Workflow

```yaml
name: CICD

on:
  workflow_dispatch:
    inputs:
      environment:
        description: 'This is the environment where this workflow runs'
        required: true
        type: choice
        default: development
        options:
          - development
          - staging
          - production

jobs:

  code:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        run: echo "Code cloned from GitHub"

  build:
    needs: code
    runs-on: ubuntu-latest

    steps:
      - name: Build Docker Container
        run: echo "Docker Container Build"

  test:
    needs: [code, build]
    runs-on: ubuntu-latest

    steps:
      - name: Test the Container
        run: echo "Testing the Container"

  deploy:
    if: inputs.environment == 'production'
    needs: test
    runs-on: ubuntu-latest

    steps:
      - name: Deploy the app
        run: echo "Docker compose deployed the app"
```

---

# Overview

This workflow demonstrates a complete CI/CD pipeline.

Stages:

```text
Code → Build → Test → Deploy
```

Deployment occurs only when the selected environment is Production.

---

# Block 1: Workflow Name

```yaml
name: CICD
```

## Purpose

Defines the workflow name.

## Where It Appears

```text
GitHub
└── Actions
    └── CICD
```

## Meaning

```text
This is the name shown in the GitHub Actions tab.
```

---

# Block 2: Trigger Section

```yaml
on:
```

Determines when the workflow runs.

---

# Block 3: workflow_dispatch

```yaml
workflow_dispatch:
```

## Purpose

Allows manual execution.

## Usage

```text
GitHub
└── Actions
    └── CICD
        └── Run Workflow
```

## Meaning

```text
Workflow runs only when the user clicks Run Workflow.
```

---

# Block 4: Inputs

```yaml
inputs:
```

Creates user inputs displayed before workflow execution.

---

# Block 5: Environment Input

```yaml
environment:
```

Input variable name.

This value can later be accessed as:

```yaml
inputs.environment
```

---

# Block 6: Description

```yaml
description: 'This is the environment where this workflow runs'
```

Displayed to the user.

Example:

```text
Environment
Select the environment where this workflow runs.
```

---

# Block 7: Required

```yaml
required: true
```

The workflow cannot start until a value is selected.

---

# Block 8: Choice Type

```yaml
type: choice
```

Creates a dropdown menu.

---

# Block 9: Default Value

```yaml
default: development
```

Automatically selected option.

---

# Block 10: Available Options

```yaml
options:
  - development
  - staging
  - production
```

User sees:

```text
development
staging
production
```

---

# Block 11: Jobs Section

```yaml
jobs:
```

Container for all jobs.

---

# Block 12: Code Job

```yaml
code:
```

First job in the pipeline.

---

# Block 13: Runner

```yaml
runs-on: ubuntu-latest
```

Creates a temporary Ubuntu machine.

Example:

```text
Ubuntu Linux Runner
```

---

# Block 14: Code Step

```yaml
steps:
  - name: Checkout code
    run: echo "Code cloned from GitHub"
```

Purpose:

```text
Represents source code retrieval.
```

Output:

```text
Code cloned from GitHub
```

---

# Block 15: Build Job

```yaml
build:
```

Second stage of the pipeline.

---

# Block 16: Job Dependency

```yaml
needs: code
```

Build waits for Code.

Flow:

```text
code
 ↓
build
```

---

# Block 17: Build Step

```yaml
run: echo "Docker Container Build"
```

Purpose:

```text
Represents container build process.
```

Output:

```text
Docker Container Build
```

---

# Block 18: Test Job

```yaml
test:
```

Third stage of the pipeline.

---

# Block 19: Multiple Dependencies

```yaml
needs: [code, build]
```

Test starts only when both jobs finish successfully.

Flow:

```text
code
 ↓
build
 ↓
test
```

---

# Block 20: Test Step

```yaml
run: echo "Testing the Container"
```

Purpose:

```text
Represents application testing.
```

Output:

```text
Testing the Container
```

---

# Block 21: Deploy Job

```yaml
deploy:
```

Final stage of the pipeline.

---

# Block 22: Conditional Execution

```yaml
if: inputs.environment == 'production'
```

Deploy runs only when Production is selected.

---

# Block 23: Deploy Dependency

```yaml
needs: test
```

Deployment starts only after tests pass.

Flow:

```text
code
 ↓
build
 ↓
test
 ↓
deploy
```

---

# Block 24: Deploy Step

```yaml
run: echo "Docker compose deployed the app"
```

Purpose:

```text
Represents application deployment.
```

Output:

```text
Docker compose deployed the app
```

---

# Workflow Behavior

## Development Selected

```text
code
 ↓
build
 ↓
test

deploy skipped
```

---

## Staging Selected

```text
code
 ↓
build
 ↓
test

deploy skipped
```

---

## Production Selected

```text
code
 ↓
build
 ↓
test
 ↓
deploy
```

---

# CI/CD Pipeline Diagram

```text
Manual Trigger
       ↓
Select Environment
       ↓
Code Job
       ↓
Build Job
       ↓
Test Job
       ↓
Production?
   /         \
 No           Yes
 |             |
Skip Deploy    Deploy
```

---

# Key Concepts Summary

| Component | Purpose |
|------------|----------|
| workflow_dispatch | Manual execution |
| inputs | User-provided values |
| environment | Selected deployment target |
| jobs | Main workflow stages |
| needs | Job dependencies |
| if | Conditional execution |
| runs-on | Runner operating system |
| steps | Individual tasks |
| deploy | Final deployment stage |

---

# One-Line Summary

**This workflow is a manually triggered CI/CD pipeline where the user selects an environment, then GitHub Actions executes Code, Build, Test, and optionally Deploy stages depending on the selected environment.**
