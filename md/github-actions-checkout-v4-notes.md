# GitHub Actions Checkout v4 (actions/checkout@v4)

## Overview

`actions/checkout@v4` GitHub ki official action hai jo aapki repository ka code GitHub se download karke GitHub Runner machine par le aati hai.

Simple alfaaz mein:

> Jab workflow start hota hai, runner ke paas aapke project ki files nahi hoti. `actions/checkout@v4` repository ko clone karke runner par laati hai taake workflow us code ko use kar sake.

---

# Why Do We Need Checkout?

Workflow runner ek temporary machine hoti hai.

Jab workflow start hota hai:

```text
GitHub Runner
└── Empty Machine
```

Repository ka code abhi available nahi hota.

Checkout action code ko download karti hai.

---

# Basic Syntax

```yaml
steps:
  - name: Checkout Code
    uses: actions/checkout@v4
```

---

# What Happens After Checkout?

Agar repository mein ye files hain:

```text
README.md
index.html
app.py
Dockerfile
```

To checkout ke baad:

```text
GitHub Runner
└── Repository Files
    ├── README.md
    ├── index.html
    ├── app.py
    └── Dockerfile
```

Ab workflow in files ko access kar sakta hai.

---

# Examples

## View Files

```yaml
- run: ls -l
```

## Read a File

```yaml
- run: cat README.md
```

## Build Docker Image

```yaml
- run: docker build .
```

---

# What is $GITHUB_WORKSPACE?

`$GITHUB_WORKSPACE` runner par ek folder hota hai jahan repository checkout hoti hai.

Linux Example:

```text
/home/runner/work/myrepo/myrepo
```

Windows Example:

```text
D:\a\myrepo\myrepo
```

---

# What If We Do Not Use Checkout?

Agar checkout step na ho:

```yaml
- run: ls
```

To repository files available nahi hongi aur commands fail ho sakti hain.

---

# Real CI/CD Example

```yaml
name: Simple CI

on:
  push:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: List Files
        run: ls -l
```

---

# Key Points

- Checkout repository ko runner par download karti hai.
- Workflow ko source code access karne ke liye checkout zaroori hota hai.
- Ye GitHub ki official action hai.
- Zyada tar workflows ka pehla step checkout hota hai.
- Version 4 (`@v4`) latest stable release hai.

---

# One-Line Summary

**actions/checkout@v4 = GitHub repository ka code runner machine par clone/download karna taake workflow us code ko access aur use kar sake.**
