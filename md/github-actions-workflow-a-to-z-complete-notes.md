# GitHub Actions Workflow - A to Z Complete Notes

## Overview

A **workflow** is the complete automation process in GitHub Actions.

It is written in a YAML file and tells GitHub:

```text
When should automation run?
What tasks should be performed?
Which machine should run the tasks?
In what order should the tasks run?
What should happen if a task succeeds or fails?
```

In simple words:

```text
Workflow = Complete automation plan
```

For example, in a portfolio deployment workflow:

```text
Checkout Code
    ↓
Setup GitHub Pages
    ↓
Upload Static Files
    ↓
Deploy Website
```

This complete process is called a **workflow**.

---

## 1. What is a Workflow?

A workflow is an automated process that runs inside GitHub Actions.

It is usually used for:

- Testing code
- Checking code quality
- Building applications
- Building Docker images
- Deploying websites
- Deploying applications
- Running security scans
- Sending notifications

Example:

```text
Developer pushes code
        ↓
GitHub Actions workflow starts
        ↓
Code is tested
        ↓
Application is built
        ↓
Application is deployed
```

---

## 2. Why Do We Need a Workflow?

Without a workflow, many tasks are manual.

Example without workflow:

```text
Manually check code
Manually run tests
Manually build project
Manually upload files
Manually deploy website
```

With a workflow:

```text
Push code
    ↓
GitHub automatically runs tasks
    ↓
Website or application is deployed
```

Benefits:

- Saves time
- Reduces human mistakes
- Makes deployment consistent
- Helps catch errors early
- Automates repetitive tasks
- Improves DevOps and CI/CD process

---

## 3. Where is a Workflow Stored?

GitHub Actions workflows must be stored in this folder:

```text
.github/workflows/
```

Example:

```text
repository/
├── index.html
├── README.md
└── .github/
    └── workflows/
        └── portfolio-deploy.yml
```

Your workflow file can have names like:

```text
portfolio-deploy.yml
python-lint.yml
docker-build-push.yml
cicd.yml
hello.yml
```

Important:

```text
GitHub only detects workflow files inside .github/workflows/
```

---

## 4. Workflow File Extension

Workflow files normally use:

```text
.yml
```

or:

```text
.yaml
```

Examples:

```text
portfolio-deploy.yml
portfolio-deploy.yaml
```

Both are valid.

---

## 5. Basic Workflow Structure

```yaml
name: My Workflow

on:
  workflow_dispatch:

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Say Hello
        run: echo "Hello from GitHub Actions"
```

This workflow:

```text
Has a name
Can be run manually
Creates one job
Uses Ubuntu runner
Runs one command
```

---

## 6. Main Parts of a Workflow

| Part | Purpose |
|---|---|
| `name` | Name of the workflow |
| `on` | Defines when the workflow runs |
| `jobs` | Defines the work to be done |
| `runs-on` | Defines the runner machine |
| `steps` | Defines tasks inside a job |
| `uses` | Uses a prebuilt GitHub Action |
| `run` | Runs a shell command |
| `permissions` | Gives workflow permissions |
| `env` | Defines environment variables |
| `needs` | Controls job order |
| `if` | Adds conditions |
| `strategy` | Runs job in multiple combinations |

---

# 7. Workflow Name

```yaml
name: Portfolio
```

The `name` field defines the workflow name.

It appears in:

```text
GitHub Repository
    ↓
Actions
    ↓
Portfolio
```

Simple meaning:

```text
This workflow is called Portfolio.
```

Example names:

```yaml
name: Python Lint
name: Docker build and push
name: Deploy Flask App
name: CICD
```

Good workflow names should be clear and meaningful.

---

# 8. Workflow Trigger

The trigger tells GitHub **when to run the workflow**.

Trigger block starts with:

```yaml
on:
```

Example:

```yaml
on:
  push:
    branches:
      - main

  workflow_dispatch:
```

This workflow runs:

```text
When code is pushed to main
OR
When user manually clicks Run workflow
```

---

# 9. Push Trigger

```yaml
on:
  push:
    branches:
      - main
```

This means:

```text
Run workflow automatically when code is pushed to the main branch.
```

Example commands:

```bash
git add .
git commit -m "update website"
git push origin main
```

After pushing to `main`, GitHub starts the workflow.

---

# 10. Manual Trigger: workflow_dispatch

```yaml
on:
  workflow_dispatch:
```

This enables the **Run workflow** button in GitHub Actions.

Path:

```text
GitHub Repository
    ↓
Actions
    ↓
Select Workflow
    ↓
Run workflow
```

This is useful when:

- You want to run a workflow manually
- You do not want workflow to run on every push
- You are testing workflows
- You are learning GitHub Actions
- You want manual deployments

---

# 11. Multiple Triggers

A workflow can have more than one trigger.

```yaml
on:
  push:
    branches:
      - main

  workflow_dispatch:
```

Meaning:

```text
Run automatically on push to main
OR
Run manually from GitHub UI
```

This is common for deployment workflows.

---

# 12. Pull Request Trigger

```yaml
on:
  pull_request:
    branches:
      - main
```

This runs workflow when a pull request is opened or updated.

Useful for:

- Testing changes before merge
- Running lint checks
- Running security scans
- Validating code before production

---

# 13. Path-Based Trigger

You can run workflows only when certain files change.

Example:

```yaml
on:
  push:
    branches:
      - main
    paths:
      - "**.py"
      - "requirements.txt"
```

This means:

```text
Run only when Python files or requirements.txt change.
```

Example for portfolio:

```yaml
on:
  push:
    branches:
      - main
    paths:
      - "**.html"
      - "**.css"
      - "**.js"
```

This avoids unnecessary workflow runs.

---

# 14. Jobs in a Workflow

```yaml
jobs:
  deploy:
```

A workflow contains one or more jobs.

A **job** is a group of steps that run together.

Example:

```yaml
jobs:
  build:
  test:
  deploy:
```

This workflow has three jobs:

```text
build
test
deploy
```

---

# 15. Job Name

```yaml
jobs:
  deploy:
```

Here, the job name is:

```text
deploy
```

You can name jobs based on their purpose:

```yaml
jobs:
  lint:
  build:
  test:
  deploy:
```

Simple meaning:

```text
Each job is a major stage of the workflow.
```

---

# 16. Runner

```yaml
runs-on: ubuntu-latest
```

A runner is the machine that executes the job.

GitHub can provide temporary runners such as:

```text
ubuntu-latest
windows-latest
macos-latest
```

Example:

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
```

Simple meaning:

```text
GitHub creates a temporary Ubuntu machine to run this job.
```

---

# 17. GitHub-Hosted Runner

A GitHub-hosted runner is a runner provided by GitHub.

Example:

```yaml
runs-on: ubuntu-latest
```

GitHub creates a fresh virtual machine for each job.

After the job finishes, the machine is deleted.

---

# 18. Self-Hosted Runner

A self-hosted runner is your own machine connected to GitHub Actions.

Example:

```yaml
runs-on: self-hosted
```

Or with labels:

```yaml
runs-on: [self-hosted, Linux, ARM64]
```

This means:

```text
Run this job on my own registered runner machine.
```

Self-hosted runners are useful when:

- You need access to private servers
- You want to deploy to your own EC2 instance
- You need tools installed on your own machine
- You want to test Docker locally

---

# 19. Steps in a Workflow

```yaml
steps:
```

Steps are the actual tasks inside a job.

Example:

```yaml
steps:
  - name: Checkout Code
    uses: actions/checkout@v4

  - name: Run tests
    run: pytest
```

Steps run from top to bottom.

---

# 20. Step Name

```yaml
- name: Checkout Code
```

The `name` is shown in GitHub Actions logs.

It helps you understand what each step is doing.

Example:

```text
Checkout Code ✅
Setup Python ✅
Install Dependencies ✅
Run Linter ✅
```

---

# 21. uses

```yaml
uses: actions/checkout@v4
```

`uses` means:

```text
Use a prebuilt GitHub Action.
```

Examples:

```yaml
uses: actions/checkout@v4
uses: actions/setup-python@v4
uses: actions/configure-pages@v4
uses: actions/upload-pages-artifact@v4
uses: actions/deploy-pages@v4
```

These actions are already created by GitHub or the community.

---

# 22. run

```yaml
run: echo "Hello"
```

`run` executes a command directly on the runner.

Examples:

```yaml
run: python --version
run: pip install -r requirements.txt
run: flake8 app.py
run: docker compose up -d
```

Simple meaning:

```text
Run this command in the runner terminal.
```

---

# 23. Workflow vs Job vs Step

```text
Workflow
│
└── Job
    │
    ├── Step
    ├── Step
    └── Step
```

Example:

```text
Workflow: Portfolio
│
└── Job: deploy
    ├── Step 1: Checkout Code
    ├── Step 2: Setup GitHub Pages
    ├── Step 3: Upload Static Files
    └── Step 4: Deploy to GitHub Pages
```

Simple difference:

| Term | Meaning |
|---|---|
| Workflow | Full automation process |
| Job | A group of tasks |
| Step | One task inside a job |

---

# 24. Real-Life Example

Think of making tea:

```text
Workflow: Make Tea
│
└── Job: Prepare Tea
    ├── Step 1: Boil water
    ├── Step 2: Add tea
    ├── Step 3: Add milk
    └── Step 4: Serve tea
```

GitHub Actions example:

```text
Workflow: Deploy Portfolio
│
└── Job: Deploy
    ├── Step 1: Checkout Code
    ├── Step 2: Configure Pages
    ├── Step 3: Upload Files
    └── Step 4: Deploy Website
```

---

# 25. Workflow Permissions

Some workflows need permissions.

Example for GitHub Pages:

```yaml
permissions:
  pages: write
  id-token: write
  contents: read
```

Meaning:

| Permission | Purpose |
|---|---|
| `contents: read` | Read repository files |
| `pages: write` | Deploy to GitHub Pages |
| `id-token: write` | Secure authentication for deployment |

Without required permissions, deployment can fail.

---

# 26. Environment Variables

Environment variables store reusable values.

Example:

```yaml
env:
  DOCKERHUB_USER: ${{ vars.DOCKERHUB_USER }}
```

Then commands can use:

```bash
echo $DOCKERHUB_USER
```

Example use in Docker Compose:

```yaml
image: ${DOCKERHUB_USER}/github-actions-app:latest
```

---

# 27. Secrets

Secrets store sensitive information.

Examples:

```text
Docker Hub token
API key
Password
Cloud credentials
```

Usage:

```yaml
password: ${{ secrets.DOCKERHUB_TOKEN }}
```

Secrets should never be hardcoded in workflow files.

---

# 28. Repository Variables

Repository variables store non-sensitive values.

Example:

```text
DOCKERHUB_USER = krmaryum
```

Usage:

```yaml
username: ${{ vars.DOCKERHUB_USER }}
```

Use variables for values that are safe to expose.

---

# 29. Job Dependencies with needs

`needs` controls job order.

Example:

```yaml
jobs:
  code:
    runs-on: ubuntu-latest

  build:
    needs: code
    runs-on: ubuntu-latest

  test:
    needs: build
    runs-on: ubuntu-latest
```

Flow:

```text
code
 ↓
build
 ↓
test
```

Without `needs`, jobs may run in parallel.

---

# 30. Conditional Execution with if

`if` controls whether a job or step should run.

Example:

```yaml
deploy:
  if: inputs.environment == 'production'
```

Meaning:

```text
Run deploy only if environment is production.
```

Example behavior:

```text
development → deploy skipped
staging     → deploy skipped
production  → deploy runs
```

---

# 31. Workflow Inputs

Inputs allow users to provide values when manually running a workflow.

Example:

```yaml
on:
  workflow_dispatch:
    inputs:
      environment:
        description: "Choose environment"
        required: true
        type: choice
        default: development
        options:
          - development
          - staging
          - production
```

This creates a dropdown in GitHub Actions.

---

# 32. Matrix Strategy

Matrix strategy runs the same job with different values.

Example:

```yaml
strategy:
  matrix:
    python-version:
      - "3.9"
      - "3.10"
      - "3.11"
      - "3.12"
      - "3.13"
```

This creates multiple jobs:

```text
validate (3.9)
validate (3.10)
validate (3.11)
validate (3.12)
validate (3.13)
```

Important:

```text
Always quote versions like "3.10"
```

Because YAML may treat `3.10` as `3.1`.

---

# 33. Artifacts

Artifacts are files produced or packaged during a workflow.

Example:

```yaml
uses: actions/upload-pages-artifact@v4
```

In GitHub Pages:

```text
Website files → artifact → deployment
```

Artifacts are useful for:

- Build output
- Test reports
- Logs
- Static website files
- Deployment packages

---

# 34. GitHub Pages Workflow Example

```yaml
name: Portfolio

on:
  push:
    branches:
      - main

  workflow_dispatch:

permissions:
  pages: write
  id-token: write
  contents: read

jobs:
  deploy:
    runs-on: ubuntu-latest

    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}

    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Setup GitHub Pages
        uses: actions/configure-pages@v4

      - name: Upload static files
        uses: actions/upload-pages-artifact@v4
        with:
          path: "."

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

Flow:

```text
Push or manual run
        ↓
Checkout Code
        ↓
Configure Pages
        ↓
Upload Static Files
        ↓
Deploy to GitHub Pages
        ↓
Live URL
```

---

# 35. Python Lint Workflow Example

```yaml
name: Python lint

on:
  push:
    branches:
      - main

  workflow_dispatch:

jobs:
  validate:
    runs-on: ubuntu-latest

    steps:
      - name: checkout code
        uses: actions/checkout@v4

      - name: set up python
        uses: actions/setup-python@v4
        with:
          python-version: "3.13"

      - name: install dependencies
        run: pip install -r requirements.txt

      - name: run linter
        run: flake8 app.py
```

Flow:

```text
Checkout Code
    ↓
Setup Python
    ↓
Install Dependencies
    ↓
Run flake8
```

---

# 36. Docker Build and Push Workflow Example

```yaml
name: Docker build and push

on:
  workflow_dispatch:

jobs:
  build-and-push:
    runs-on: ubuntu-latest

    steps:
      - name: checkout code
        uses: actions/checkout@v4

      - name: Login to Docker Hub
        uses: docker/login-action@v4
        with:
          username: ${{ vars.DOCKERHUB_USER }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}

      - name: Build and push
        uses: docker/build-push-action@v7
        with:
          context: .
          push: true
          tags: |
            ${{ vars.DOCKERHUB_USER }}/github-actions-app:${{ github.ref_name }}
            ${{ vars.DOCKERHUB_USER }}/github-actions-app:latest
            ${{ vars.DOCKERHUB_USER }}/github-actions-app:${{ github.sha }}
```

Flow:

```text
Manual run
    ↓
Checkout Code
    ↓
Login to Docker Hub
    ↓
Build Docker Image
    ↓
Push Image to Docker Hub
```

---

# 37. Self-Hosted Deploy Workflow Example

```yaml
name: Deploy Flask App

on:
  workflow_dispatch:

jobs:
  deploy:
    runs-on: self-hosted

    env:
      DOCKERHUB_USER: ${{ vars.DOCKERHUB_USER }}

    steps:
      - name: checkout code
        uses: actions/checkout@v4

      - name: deploy with docker compose
        run: docker compose up -d --build
```

Flow:

```text
Manual run
    ↓
Run job on self-hosted runner
    ↓
Checkout Code
    ↓
Run Docker Compose
    ↓
Deploy Flask App
```

---

# 38. Common Workflow Flow

```text
Trigger
   ↓
Workflow starts
   ↓
Runner is created or selected
   ↓
Job starts
   ↓
Steps run one by one
   ↓
Success or failure
```

---

# 39. What Happens When a Workflow Runs?

Step by step:

```text
1. GitHub checks the workflow trigger
2. GitHub reads YAML file
3. GitHub creates job
4. GitHub chooses runner
5. Runner starts
6. Repository code is checked out
7. Workflow steps execute
8. Logs are generated
9. Job succeeds or fails
10. Workflow result appears in Actions tab
```

---

# 40. How to Read Workflow Logs

Go to:

```text
GitHub Repository
    ↓
Actions
    ↓
Select Workflow
    ↓
Select Run
    ↓
Click Job
    ↓
Open Step Logs
```

Logs help you troubleshoot errors.

Examples:

```text
YAML syntax error
Dependency install failed
Docker login failed
Port already in use
Missing secret
Wrong image tag
```

---

# 41. Common Error: Workflow Not Showing

If Actions tab says:

```text
Get started with GitHub Actions
```

Possible reasons:

- Workflow file not committed
- Wrong folder
- Wrong file path
- YAML syntax error
- File not on selected branch

Correct path:

```text
.github/workflows/workflow-name.yml
```

---

# 42. Common Error: Wrong Indentation

YAML is indentation sensitive.

Correct:

```yaml
on:
  workflow_dispatch:
```

Incorrect:

```yaml
on:
    workflow_dispatch:
```

Some indentation may still work, but inconsistent indentation can break YAML.

Use 2 spaces consistently.

---

# 43. Common Error: Wrong Runner Name

Correct:

```yaml
runs-on: ubuntu-latest
```

Incorrect:

```yaml
runs-on: ubutu-latest
```

A typo in runner label can make the job wait or fail.

---

# 44. Common Error: Missing Secret or Variable

Example:

```yaml
username: ${{ vars.DOCKERHUB_USER }}
password: ${{ secrets.DOCKERHUB_TOKEN }}
```

If these are not created in GitHub settings, workflow can fail.

Path:

```text
Settings
    ↓
Secrets and variables
    ↓
Actions
```

---

# 45. Common Error: Docker Compose Variable Not Set

If compose uses:

```yaml
image: ${DOCKERHUB_USER}/github-actions-app:latest
```

Then workflow must pass:

```yaml
env:
  DOCKERHUB_USER: ${{ vars.DOCKERHUB_USER }}
```

Otherwise Docker Compose may show:

```text
The "DOCKERHUB_USER" variable is not set
invalid reference format
```

---

# 46. Common Error: Python Version Parsing

Incorrect:

```yaml
python-version: [3.9, 3.10, 3.11]
```

YAML may convert `3.10` into `3.1`.

Correct:

```yaml
python-version: ["3.9", "3.10", "3.11"]
```

Always quote version numbers.

---

# 47. Common Error: Docker Cleanup Step

This can fail:

```bash
docker stop $(docker ps -q)
```

If no containers are running.

Safer version:

```bash
if [ "$(docker ps -q)" ]; then
  docker stop $(docker ps -q)
fi
```

Meaning:

```text
If running containers exist, stop them.
Otherwise do nothing.
```

---

# 48. Best Practices

- Use clear workflow names
- Keep workflow files inside `.github/workflows/`
- Use 2 spaces for indentation
- Use meaningful job names
- Use meaningful step names
- Use secrets for passwords and tokens
- Use variables for reusable non-sensitive values
- Use `workflow_dispatch` while learning
- Use `push` for automatic checks
- Use `needs` for job order
- Use `if` for conditions
- Use matrix strategy for multiple versions
- Read logs carefully when workflows fail

---

# 49. Interview Explanation

You can explain workflow like this:

```text
A GitHub Actions workflow is an automation process defined in a YAML file.
It is stored under .github/workflows.
A workflow is triggered by events such as push, pull_request, or workflow_dispatch.
It contains jobs, and each job runs on a runner such as ubuntu-latest or self-hosted.
Each job contains steps that either run shell commands or use prebuilt actions.
I used workflows for Python linting, Docker image build and push, GitHub Pages deployment, and self-hosted deployment.
```

---

# 50. Resume Sentence

```text
Created GitHub Actions workflows to automate linting, Docker image builds, Docker Hub publishing, GitHub Pages deployment, and self-hosted application deployment.
```

Another version:

```text
Implemented CI/CD workflows using GitHub Actions with manual triggers, job dependencies, matrix strategy, Docker build automation, and GitHub Pages deployment.
```

---

# 51. One-Line Summary

A GitHub Actions workflow is a YAML-based automation process that tells GitHub when to run, which runner to use, what jobs to execute, and what steps to perform for testing, building, deploying, and automating software delivery.
