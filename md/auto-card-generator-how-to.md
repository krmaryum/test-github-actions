# Auto Card Generator for Study Notes and MCQs

## Goal

Whenever you add new study notes or MCQ quiz files, the website should create cards automatically.

This automation script scans your folders and generates:

```text
notes/index.html
mcqs/index.html
```

So you do not need to manually edit index pages every time.

---

## Files Created

Place this file in your repo root:

```text
generate_file_cards.py
```

Repo root example:

```text
/c/Linux/test-github-actions
```

---

## Supported File Types

### Study Notes

The script scans these folders:

```text
notes/
md/
pdfs/
```

Supported extensions:

```text
.md
.html
.pdf
.docx
.xlsx
.xls
.pptx
.txt
```

### MCQs

The script scans:

```text
mcqs/
```

Supported extension:

```text
.html
```

---

## Recommended Folder Structure

Example for NFS:

```text
notes/nfs/linux-nfs-study-notes.md
notes/nfs/nfs-wsl-ubuntu-almalinux-from-scratch-to-hero.md

mcqs/nfs/nfs-wsl-lab-25-mcq-quiz.html
```

You can also keep Markdown notes in:

```text
md/nfs/
```

And PDFs in:

```text
pdfs/nfs/
```

---

## How to Use

Go to repo:

```bash
cd /c/Linux/test-github-actions
```

Run:

```bash
python generate_file_cards.py
```

Check result:

```bash
git status
```

Push:

```bash
git add -A
git commit -m "Auto-generate study notes and MCQ cards"
git push origin main
```

---

## Daily Workflow

Whenever you add new files:

```bash
cd /c/Linux/test-github-actions

# 1. Add/copy your files into notes/, md/, pdfs/, or mcqs/

# 2. Regenerate cards
python generate_file_cards.py

# 3. Push
git add -A
git commit -m "Add new study notes and MCQs"
git push origin main
```

---

## Optional: Add to upload.sh

If you already have an upload script, add this line before `git add -A`:

```bash
python generate_file_cards.py
```

Example:

```bash
#!/bin/bash

echo "Generating cards..."
python generate_file_cards.py

echo "Checking status..."
git status

read -p "Enter commit message: " msg

git add -A
git commit -m "$msg"
git push origin main
```

---

## Optional: GitHub Actions Automation

If your GitHub Actions deployment runs on every push, add this step before upload/deploy:

```yaml
- name: Generate notes and MCQ cards
  run: python generate_file_cards.py
```

That way, when GitHub Pages deploys, it generates fresh cards automatically.

---

## Important Note

GitHub Pages is static hosting.

That means cards do **not** magically update in the browser just because a file exists.

Cards update when one of these happens:

```text
1. You run python generate_file_cards.py locally and push
2. GitHub Actions runs python generate_file_cards.py during deployment
```

---

## Summary

Old method:

```text
Add file
Manually edit notes/index.html
Manually edit mcqs/index.html
Push
```

New method:

```text
Add file
Run python generate_file_cards.py
Push
```

Best method:

```text
Add file
Push
GitHub Actions runs generator automatically
Deploys updated website
```
