# GitHub Pages Deployment with GitHub Actions - A to Z Notes

## Overview

This guide explains how a portfolio website was deployed using **GitHub Actions** and **GitHub Pages**.

Final live URL example:

```text
https://krmaryum.github.io/izma-portfolio/
```

The deployment workflow copied the repository files, prepared GitHub Pages, uploaded the website files as an artifact, deployed them, and generated a live website URL.

---

## 1. What is GitHub Pages?

GitHub Pages is a hosting service from GitHub used to publish static websites directly from a GitHub repository.

It is commonly used for:

- Portfolio websites
- Project documentation
- Personal blogs
- Landing pages
- Static HTML/CSS/JavaScript websites

---

## 2. What is GitHub Actions?

GitHub Actions is an automation tool built into GitHub.

It can automate tasks such as:

- Testing code
- Running linters
- Building applications
- Deploying websites
- Building Docker images
- Pushing images to Docker Hub

In this case, GitHub Actions was used to deploy a portfolio website to GitHub Pages.

---

## 3. Workflow File Location

GitHub Actions only detects workflow files from this folder:

```text
.github/workflows/
```

Your workflow file was created here:

```text
.github/workflows/portfolio-deploy.yml
```

This location is very important.

Correct:

```text
.github/workflows/portfolio-deploy.yml
```

Incorrect:

```text
.github/workflow/portfolio-deploy.yml
github/workflows/portfolio-deploy.yml
portfolio-deploy.yml
```

---

## 4. Complete Workflow

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

---

## 5. Workflow Name

```yaml
name: Portfolio
```

This is the workflow name.

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
This workflow is named Portfolio.
```

---

## 6. Trigger Section

```yaml
on:
  push:
    branches:
      - main

  workflow_dispatch:
```

The trigger section tells GitHub when to run the workflow.

This workflow can run in two ways:

1. Automatically when code is pushed to the `main` branch
2. Manually using the `Run workflow` button

---

## 7. Push Trigger

```yaml
push:
  branches:
    - main
```

This means the workflow runs automatically when code is pushed to the `main` branch.

Example:

```bash
git add .
git commit -m "update portfolio"
git push origin main
```

After this push, the Portfolio workflow starts automatically.

---

## 8. Manual Trigger

```yaml
workflow_dispatch:
```

This enables a manual run button in GitHub Actions.

Path:

```text
GitHub Repository
    ↓
Actions
    ↓
Portfolio
    ↓
Run workflow
```

This is useful when you want to redeploy without making a new commit.

---

## 9. Permissions Block

```yaml
permissions:
  pages: write
  id-token: write
  contents: read
```

This gives the workflow the permissions needed to deploy to GitHub Pages.

---

## 10. contents: read

```yaml
contents: read
```

This allows the workflow to read the files in the repository.

Example files:

```text
index.html
style.css
script.js
images/
README.md
```

Without this permission, the workflow may not be able to access the website files.

---

## 11. pages: write

```yaml
pages: write
```

This allows the workflow to publish files to GitHub Pages.

Simple meaning:

```text
GitHub Actions is allowed to write/deploy to GitHub Pages.
```

---

## 12. id-token: write

```yaml
id-token: write
```

This allows GitHub to securely verify that the deployment is coming from a trusted workflow.

Simple meaning:

```text
GitHub Actions can securely authenticate the Pages deployment.
```

---

## 13. Jobs Section

```yaml
jobs:
  deploy:
```

A workflow contains one or more jobs.

Here, there is one job named:

```text
deploy
```

Simple meaning:

```text
The job's purpose is to deploy the portfolio website.
```

---

## 14. Runner

```yaml
runs-on: ubuntu-latest
```

This tells GitHub to create a temporary Ubuntu Linux machine.

That machine is called a **runner**.

Simple meaning:

```text
GitHub starts a temporary Ubuntu machine to run the deployment.
```

---

## 15. Environment Block

```yaml
environment:
  name: github-pages
  url: ${{ steps.deployment.outputs.page_url }}
```

This connects the job to the GitHub Pages environment.

---

## 16. Environment Name

```yaml
name: github-pages
```

This tells GitHub that the deployment target is GitHub Pages.

---

## 17. Environment URL

```yaml
url: ${{ steps.deployment.outputs.page_url }}
```

This takes the website URL from the deploy step and shows it in the GitHub Actions summary.

Example:

```text
https://krmaryum.github.io/izma-portfolio/
```

---

## 18. Important: id: deployment

This line is very important:

```yaml
id: deployment
```

It is used here:

```yaml
url: ${{ steps.deployment.outputs.page_url }}
```

The word `deployment` must match the step ID.

Correct:

```yaml
environment:
  url: ${{ steps.deployment.outputs.page_url }}

steps:
  - name: Deploy to GitHub Pages
    id: deployment
    uses: actions/deploy-pages@v4
```

If the deploy step does not have `id: deployment`, GitHub cannot find:

```text
steps.deployment.outputs.page_url
```

---

## 19. Steps Section

```yaml
steps:
```

Steps are the actual actions performed inside the job.

This workflow has four main steps:

```text
1. Checkout Code
2. Setup GitHub Pages
3. Upload static files
4. Deploy to GitHub Pages
```

---

## 20. Step 1: Checkout Code

```yaml
- name: Checkout Code
  uses: actions/checkout@v4
```

This downloads the repository files into the GitHub runner.

Before checkout:

```text
Ubuntu runner
└── empty
```

After checkout:

```text
Ubuntu runner
├── index.html
├── style.css
├── script.js
├── images/
└── .github/
```

Simple meaning:

```text
The website files are copied into the runner.
```

---

## 21. Step 2: Setup GitHub Pages

```yaml
- name: Setup GitHub Pages
  uses: actions/configure-pages@v4
```

This prepares the GitHub Pages environment.

Simple meaning:

```text
GitHub Pages deployment settings are configured.
```

---

## 22. Step 3: Upload Static Files

```yaml
- name: Upload static files
  uses: actions/upload-pages-artifact@v4
  with:
    path: "."
```

This uploads the website files as a deployable package.

The dot means:

```text
Current repository folder
```

So GitHub uploads:

```text
index.html
CSS files
JavaScript files
images
other static assets
```

This package is called an **artifact**.

---

## 23. What is an Artifact?

An artifact is a packaged output created during a workflow.

In this case:

```text
Website files → artifact → GitHub Pages deployment
```

Simple meaning:

```text
GitHub packages your static website files before deployment.
```

---

## 24. Step 4: Deploy to GitHub Pages

```yaml
- name: Deploy to GitHub Pages
  id: deployment
  uses: actions/deploy-pages@v4
```

This publishes the uploaded artifact to GitHub Pages.

This is the step that makes the website live.

---

## 25. Full Deployment Flow

```text
Create portfolio-deploy.yml
        ↓
GitHub detects workflow file
        ↓
Workflow starts
        ↓
GitHub creates Ubuntu runner
        ↓
Checkout repository code
        ↓
Configure GitHub Pages
        ↓
Upload website files as artifact
        ↓
Deploy artifact to GitHub Pages
        ↓
Generate live website URL
        ↓
Deployment success
```

---

## 26. What Happened in Your Deployment?

Your workflow ran successfully:

```text
Portfolio #2
Status: Success
Total duration: 17s
Artifacts: 1
```

This means:

```text
Checkout Code ✅
Setup GitHub Pages ✅
Upload static files ✅
Deploy to GitHub Pages ✅
```

---

## 27. Final Live URL

Your portfolio was deployed to:

```text
https://krmaryum.github.io/izma-portfolio/
```

This URL follows the GitHub Pages format:

```text
https://username.github.io/repository-name/
```

For your repository:

```text
username = krmaryum
repository = izma-portfolio
```

So the final URL is:

```text
https://krmaryum.github.io/izma-portfolio/
```

---

## 28. Settings to Check

In repository settings, GitHub Pages should use:

```text
Source: GitHub Actions
```

This is because your workflow uses:

```yaml
actions/upload-pages-artifact@v4
actions/deploy-pages@v4
```

Do not use `Deploy from a branch` for this workflow style.

---

## 29. Common Issue: Workflow Not Showing

If the Actions tab shows:

```text
Get started with GitHub Actions
```

then GitHub does not see the workflow yet.

Possible reasons:

- The workflow file was not committed
- The file is in the wrong folder
- The file path is incorrect
- YAML syntax has an error

Correct path:

```text
.github/workflows/portfolio-deploy.yml
```

---

## 30. Common Issue: Deployment URL Error

If you use:

```yaml
url: ${{ steps.deployment.outputs.page_url }}
```

then you must also have:

```yaml
id: deployment
```

in the deploy step.

Correct:

```yaml
- name: Deploy to GitHub Pages
  id: deployment
  uses: actions/deploy-pages@v4
```

---

## 31. Common Issue: GitHub Pages Disabled

If GitHub Pages says disabled, change source to:

```text
GitHub Actions
```

Path:

```text
Repository
    ↓
Settings
    ↓
Pages
    ↓
Build and deployment
    ↓
Source
    ↓
GitHub Actions
```

---

## 32. Common Warning: Node.js 20 Deprecated

You may see a warning like:

```text
Node.js 20 actions are deprecated
```

This is only a warning from GitHub.

If the workflow status is:

```text
Success
```

then the deployment worked.

For now, you can ignore this warning.

---

## 33. Workflow vs Job vs Step

```text
Workflow
│
└── Job: deploy
    ├── Step 1: Checkout Code
    ├── Step 2: Setup GitHub Pages
    ├── Step 3: Upload static files
    └── Step 4: Deploy to GitHub Pages
```

---

## 34. Key Concepts Table

| Concept | Meaning |
|---|---|
| Workflow | Full automation process |
| Trigger | Event that starts workflow |
| Job | Group of steps |
| Runner | Temporary machine |
| Step | Individual task |
| Action | Reusable automation |
| Artifact | Packaged website files |
| GitHub Pages | Static website hosting |
| Deployment | Publishing the website online |

---

## 35. Commands for Local Git Workflow

```bash
git add .
git commit -m "add portfolio deployment workflow"
git push origin main
```

After pushing, GitHub Actions will start automatically if the workflow has:

```yaml
on:
  push:
    branches:
      - main
```

---

## 36. Manual Deployment Steps

```text
GitHub Repository
    ↓
Actions
    ↓
Portfolio
    ↓
Run workflow
    ↓
Select branch main
    ↓
Run workflow
```

---

## 37. Interview Explanation

You can explain this project like this:

```text
I deployed a static portfolio website using GitHub Actions and GitHub Pages.
I created a workflow under .github/workflows that checks out the code,
configures GitHub Pages, uploads the static files as an artifact,
and deploys the artifact to GitHub Pages.
The workflow can run automatically on push to main and manually using workflow_dispatch.
```

---

## 38. Resume or LinkedIn Sentence

```text
Deployed a portfolio website using GitHub Actions and GitHub Pages with automated workflow-based deployment.
```

Another version:

```text
Configured a GitHub Actions workflow to automate static website deployment to GitHub Pages using artifact-based deployment.
```

---

## 39. Final Summary

Your deployment worked because:

```text
Workflow file was created in the correct folder
        ↓
GitHub Actions detected the workflow
        ↓
The workflow had correct permissions
        ↓
The runner checked out the code
        ↓
GitHub Pages was configured
        ↓
Website files were uploaded as an artifact
        ↓
The artifact was deployed
        ↓
GitHub generated the live portfolio URL
```

---

## 40. One-Line Summary

A GitHub Actions workflow deployed your portfolio website to GitHub Pages by checking out the code, configuring Pages, uploading static files as an artifact, deploying the artifact, and generating a live public URL.
