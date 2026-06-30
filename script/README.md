# Portfolio Auto Upload Script

## File

```text
portfolio-upload.sh
```

## Purpose

This script automates your next-time workflow for the portfolio website.

Instead of manually running many commands, you only run:

```bash
./portfolio-upload.sh
```

## What It Does

```text
1. Goes to /c/Linux/test-github-actions
2. Runs generate_file_cards.py
3. Updates notes/index.html automatically
4. Updates mcqs/index.html automatically
5. Stages all changes
6. Asks for a commit message
7. Commits
8. Pushes to GitHub main branch
```

## Where to Put It

Put this file in your repo root:

```text
/c/Linux/test-github-actions/portfolio-upload.sh
```

## First-Time Setup

Run:

```bash
cd /c/Linux/test-github-actions
chmod +x portfolio-upload.sh
```

## Normal Use

After adding new files into:

```text
notes/
md/
pdfs/
mcqs/
```

Run:

```bash
cd /c/Linux/test-github-actions
./portfolio-upload.sh
```

## Example Workflow

Add NFS files:

```text
notes/nfs/linux-nfs-study-notes.md
notes/nfs/nfs-wsl-ubuntu-almalinux-from-scratch-to-hero.md
mcqs/nfs/nfs-wsl-lab-25-mcq-quiz.html
```

Then run:

```bash
./portfolio-upload.sh
```

The script will generate the cards automatically and push everything.

## Important

Your repo must already have:

```text
generate_file_cards.py
```

If that file is missing, the script will stop and show an error.

## Website

After push, wait for GitHub Actions deployment and check:

```text
https://khalidkhan.me
https://khalidkhan.me/notes/
https://khalidkhan.me/mcqs/
```
