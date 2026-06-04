# Day 39 - Docker on Self-Hosted Runner (A to Z)

## Overview
This project demonstrates how to execute Docker workloads using a GitHub Actions Self-Hosted Runner running on Ubuntu 24.04 WSL2 (ARM64).

## Objectives
- Understand Docker execution in CI/CD
- Execute Docker commands from GitHub Actions
- Use a Self-Hosted Runner
- Validate Docker installation
- Run containers through GitHub workflows

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
Docker Engine
        │
        ▼
Containers
```

## Workflow File

```text
.github/workflows/docker-self-hosted.yml
```

## Workflow

```yaml
name: Docker Self Hosted Test

on:
  workflow_dispatch:

jobs:
  docker-test:
    runs-on: [self-hosted, Linux, ARM64]

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Check Docker version
        run: docker --version

      - name: Run hello-world container
        run: docker run --rm hello-world

      - name: Show running containers
        run: docker ps

      - name: Show all containers
        run: docker ps -a
```

## Result

```text
Connected to GitHub
Listening for Jobs
Running job: docker-test
Job docker-test completed with result: Succeeded
```

## Skills Demonstrated

- GitHub Actions
- Docker
- YAML
- Linux
- Ubuntu WSL2
- Self-Hosted Runner
- CI/CD
- Automation

## Summary

Successfully executed Docker commands through GitHub Actions using a Self-Hosted Runner on Ubuntu 24.04 WSL2 ARM64.
