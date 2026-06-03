# GitHub Actions - Python Lint Workflow Notes

## Overview

This workflow automatically checks Python code quality whenever code is pushed to the main branch.

## Workflow

```yaml
name: Python lint

on:
  push:
    branches: [main]

jobs:
  validate:
    runs-on: ubuntu-latest

    steps:
      - name: checkout code
        uses: actions/checkout@v4

      - name: set up python
        uses: actions/setup-python@v4
        with:
          python-version: 3.13

      - name: install dependencies
        run: pip install -r requirements.txt

      - name: run linter
        run: flake8 app.py
```

## Workflow Flow

Push Code → Checkout Code → Setup Python → Install Dependencies → Run flake8 → Pass/Fail

## Step-by-Step Explanation

### 1. Workflow Name

```yaml
name: Python lint
```

Displayed in the GitHub Actions tab.

### 2. Trigger

```yaml
on:
  push:
    branches: [main]
```

Runs whenever code is pushed to the main branch.

### 3. Job

```yaml
jobs:
  validate:
    runs-on: ubuntu-latest
```

Creates a job named validate on an Ubuntu runner.

### 4. Checkout Code

```yaml
uses: actions/checkout@v4
```

Downloads repository files to the runner.

### 5. Setup Python

```yaml
uses: actions/setup-python@v4
```

Installs Python 3.13.

### 6. Install Dependencies

```yaml
pip install -r requirements.txt
```

Installs packages listed in requirements.txt.

### 7. Run Linter

```yaml
flake8 app.py
```

Checks:
- Syntax errors
- PEP 8 violations
- Unused imports
- Indentation issues
- Code quality problems

## Example

Python file:

```python
import os

print("Hello World")
```

flake8 output:

```text
F401 'os' imported but unused
```

## What is a Linter?

A linter automatically reviews code and helps:
- Improve quality
- Enforce standards
- Detect mistakes early
- Maintain consistency

Popular Python linters:
- flake8
- pylint
- black
- ruff

## Recommended Improvement

```yaml
- name: Install Dependencies
  run: |
    pip install -r requirements.txt
    pip install flake8
```

This ensures flake8 is installed.

## Key Concepts

| Component | Purpose |
|------------|----------|
| Workflow | Automation process |
| Job | Group of steps |
| Step | Individual task |
| Runner | Temporary machine |
| checkout@v4 | Downloads repository |
| setup-python@v4 | Installs Python |
| requirements.txt | Package list |
| flake8 | Python linter |

## One-Line Summary

**This workflow installs Python, installs dependencies, and runs flake8 to check code quality whenever code is pushed to the main branch.**
