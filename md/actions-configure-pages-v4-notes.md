# GitHub Actions - actions/configure-pages@v4

## Overview

`actions/configure-pages@v4` GitHub ki official action hai jo GitHub Pages deployment environment ko configure karti hai.

Simple alfaaz mein:

> Yeh action GitHub Pages ko batati hai ke website ko deploy karne ke liye kya settings use karni hain aur deployment ke liye environment tayyar karti hai.

---

## What is GitHub Pages?

GitHub Pages ek free hosting service hai jo GitHub repositories se static websites host karti hai.

Examples:
- Portfolio Website
- Documentation Site
- Project Website
- Personal Blog

---

## Why Do We Need configure-pages?

`actions/configure-pages@v4`:

- Pages deployment environment setup karti hai
- Required metadata configure karti hai
- Deployment process ko prepare karti hai
- GitHub Pages deployment ke liye workflow ready karti hai

---

## Basic Syntax

```yaml
- name: Configure GitHub Pages
  uses: actions/configure-pages@v4
```

---

## Typical GitHub Pages Workflow

```yaml
name: Deploy Website

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: actions/configure-pages@v4

      - uses: actions/upload-pages-artifact@v3
        with:
          path: '.'

      - uses: actions/deploy-pages@v4
```

---

## Deployment Flow

```text
1. Checkout Code
        ↓
2. Configure Pages
        ↓
3. Upload Website Files
        ↓
4. Deploy to GitHub Pages
```

---

## Role of Each Action

| Action | Purpose |
|----------|----------|
| actions/checkout@v4 | Repository ka code download karta hai |
| actions/configure-pages@v4 | GitHub Pages environment configure karta hai |
| actions/upload-pages-artifact@v3 | Website files upload karta hai |
| actions/deploy-pages@v4 | Website ko GitHub Pages par publish karta hai |

---

## Real Example

Repository:

```text
index.html
style.css
script.js
images/
```

Workflow:

```yaml
steps:
  - uses: actions/checkout@v4
  - uses: actions/configure-pages@v4
  - uses: actions/upload-pages-artifact@v3
    with:
      path: '.'
  - uses: actions/deploy-pages@v4
```

Result:

```text
https://username.github.io/repository-name
```

Website internet par live ho jayegi.

---

## Simple Analogy

checkout@v4
= Samaan ghar se nikala

configure-pages@v4
= Naye ghar ki tayyari ki

upload-pages-artifact@v3
= Samaan truck mein rakha

deploy-pages@v4
= Samaan naye ghar mein rakh diya

---

## Key Points

- GitHub ki official Pages action hai.
- GitHub Pages environment configure karti hai.
- Deployment se pehle use hoti hai.
- Usually upload-pages-artifact aur deploy-pages ke sath use ki jati hai.
- Static websites deploy karne ke liye zaroori step hai.

---

## One-Line Summary

**actions/configure-pages@v4 GitHub Pages deployment ke liye environment aur settings configure karti hai taake website ko GitHub Pages par deploy kiya ja sake.**
