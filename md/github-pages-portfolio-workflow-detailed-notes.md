# GitHub Actions Portfolio Deployment Workflow - Detailed Notes

## Complete Workflow

```yaml
name: Portfolio

on:
  push:
    branches:
      - main

  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  deploy:
    runs-on: ubuntu-latest

    environment:
      name: github-pages
      url: ${{ steps.deploy-pages.outputs.page_url }}

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup GitHub Pages
        uses: actions/configure-pages@v4

      - name: Upload static code artifact
        uses: actions/upload-pages-artifact@v4
        with:
          path: .

      - id: deploy-pages
        name: Deploy to GitHub Pages
        uses: actions/deploy-pages@v4
```

---

# 1. Workflow Name

```yaml
name: Portfolio
```

Purpose:
- Defines the workflow name.
- Appears in the GitHub Actions tab.

Example:

```text
Actions
└── Portfolio
```

---

# 2. Trigger Block

```yaml
on:
```

Defines when the workflow should run.

## Automatic Trigger

```yaml
push:
  branches:
    - main
```

Runs whenever code is pushed to the main branch.

Example:

```bash
git add .
git commit -m "Update portfolio"
git push origin main
```

Result:

```text
Workflow Starts Automatically
```

## Manual Trigger

```yaml
workflow_dispatch:
```

Allows manual execution from GitHub UI.

Path:

```text
GitHub
└── Actions
    └── Portfolio
        └── Run Workflow
```

---

# 3. Permissions Block

```yaml
permissions:
  contents: read
  pages: write
  id-token: write
```

Controls what the workflow is allowed to do.

## contents: read

```yaml
contents: read
```

Allows reading repository files.

Examples:

```text
index.html
style.css
script.js
README.md
```

## pages: write

```yaml
pages: write
```

Allows deployment to GitHub Pages.

## id-token: write

```yaml
id-token: write
```

Allows secure authentication during deployment.

---

# 4. Jobs Block

```yaml
jobs:
  deploy:
```

Defines a job named deploy.

Simple Meaning:

```text
Deploy website job
```

---

# 5. Runner

```yaml
runs-on: ubuntu-latest
```

Creates a temporary Ubuntu Linux machine.

Example:

```text
Ubuntu 24.x Runner
```

This machine exists only during workflow execution.

---

# 6. Environment Block

```yaml
environment:
  name: github-pages
  url: ${{ steps.deploy-pages.outputs.page_url }}
```

Associates deployment with GitHub Pages environment.

## Environment Name

```yaml
name: github-pages
```

Environment used by GitHub Pages.

## Website URL

```yaml
url: ${{ steps.deploy-pages.outputs.page_url }}
```

Displays the deployed website URL.

Example:

```text
https://username.github.io/repository-name/
```

---

# 7. Steps Block

```yaml
steps:
```

Contains all actions executed in order.

---

# 8. Checkout Code

```yaml
- name: Checkout code
  uses: actions/checkout@v4
```

Downloads repository files to the runner.

Before:

```text
Runner
└── Empty
```

After:

```text
Runner
├── index.html
├── style.css
├── script.js
└── README.md
```

Purpose:

```text
Make repository files available to the workflow.
```

---

# 9. Setup GitHub Pages

```yaml
- name: Setup GitHub Pages
  uses: actions/configure-pages@v4
```

Configures GitHub Pages deployment environment.

Purpose:

```text
Prepare GitHub Pages deployment settings.
```

---

# 10. Upload Static Code Artifact

```yaml
- name: Upload static code artifact
  uses: actions/upload-pages-artifact@v4
  with:
    path: .
```

Uploads website files for deployment.

## path: .

```yaml
path: .
```

The dot means current repository folder.

Example files uploaded:

```text
index.html
style.css
script.js
images/
```

Purpose:

```text
Package website files for deployment.
```

---

# 11. Deploy to GitHub Pages

```yaml
- id: deploy-pages
  name: Deploy to GitHub Pages
  uses: actions/deploy-pages@v4
```

Publishes uploaded files to GitHub Pages.

## id

```yaml
id: deploy-pages
```

Allows later reference to deployment outputs.

## Deploy

```yaml
uses: actions/deploy-pages@v4
```

Makes website publicly accessible.

Result:

```text
https://username.github.io/repository-name/
```

---

# Workflow Execution Flow

```text
Push to Main Branch
        ↓
Start Ubuntu Runner
        ↓
Checkout Repository
        ↓
Configure GitHub Pages
        ↓
Upload Website Files
        ↓
Deploy Website
        ↓
Generate Live URL
```

---

# Action Summary

| Action | Purpose |
|----------|----------|
| actions/checkout@v4 | Downloads repository code |
| actions/configure-pages@v4 | Configures GitHub Pages |
| actions/upload-pages-artifact@v4 | Uploads website files |
| actions/deploy-pages@v4 | Publishes website to GitHub Pages |

---

# Key Concepts

| Component | Purpose |
|------------|----------|
| Workflow | Automation process |
| Job | Group of steps |
| Step | Individual task |
| Runner | Temporary machine |
| Environment | Deployment target |
| Artifact | Packaged website files |
| GitHub Pages | Static website hosting |
| URL Output | Live website address |

---

# One-Line Summary

**This workflow automatically deploys your portfolio website to GitHub Pages whenever code is pushed to the main branch, and it can also be triggered manually from GitHub Actions.**
