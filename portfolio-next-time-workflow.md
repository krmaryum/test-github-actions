# Portfolio Website Next-Time Workflow

## Goal

This note explains what to do next time when you want to add new study notes, PDFs, or MCQ quiz files to your portfolio website.

Website:

```text
https://khalidkhan.me
```

Repo folder:

```text
/c/Linux/test-github-actions
```

---

## Simple One-Line Summary

```text
Add files → run ./portfolio-upload.sh → GitHub Pages updates
```

---

# 1. Go to Your Portfolio Repo

Open Git Bash and run:

```bash
cd /c/Linux/test-github-actions
```

---

# 2. Add Your New Files

## Study Notes

Put Markdown study notes inside:

```text
notes/
```

Example:

```text
notes/nfs/linux-nfs-study-notes.md
notes/bash-scripting/bash-introduction.md
```

---

## PDFs

Put PDF files inside:

```text
pdfs/
```

Example:

```text
pdfs/bash-scripting/shell-scripting-crash-course.pdf
```

---

## MCQ Quizzes

Put MCQ HTML quiz files inside:

```text
mcqs/
```

Example:

```text
mcqs/nfs/nfs-wsl-lab-25-mcq-quiz.html
mcqs/bash-scripting/bash-25-mcq-quiz.html
```

---

# 3. Run the Upload Script

After adding files, run only this command:

```bash
./portfolio-upload.sh
```

---

# 4. What `portfolio-upload.sh` Does

The script automatically does these steps:

```text
1. Goes to /c/Linux/test-github-actions
2. Checks that generate_file_cards.py exists
3. Runs python generate_file_cards.py
4. Updates notes/index.html
5. Updates mcqs/index.html
6. Runs git status
7. Runs git add -A
8. Asks you for a commit message
9. Commits the changes
10. Pushes to GitHub main branch
```

---

# 5. What `generate_file_cards.py` Does

This script creates cards automatically for your website.

It updates:

```text
notes/index.html
mcqs/index.html
```

So you do not need to manually edit index files every time.

---

# 6. Important Folder Rule

Use these folders:

```text
notes/
pdfs/
mcqs/
```

If you decided not to use the `md/` folder, make sure this line inside `generate_file_cards.py` is:

```python
NOTE_ROOTS = ["notes", "pdfs"]
```

Not:

```python
NOTE_ROOTS = ["notes", "md", "pdfs"]
```

---

# 7. First-Time Setup for Upload Script

If you have not done this yet, run:

```bash
chmod +x portfolio-upload.sh
```

This makes the script executable.

---

# 8. Full Next-Time Workflow

```bash
cd /c/Linux/test-github-actions

# Add your files into notes/, pdfs/, or mcqs/

./portfolio-upload.sh
```

---

# 9. After Push

Wait for GitHub Actions deployment to complete.

Then check:

```text
https://khalidkhan.me
https://khalidkhan.me/notes/
https://khalidkhan.me/mcqs/
```

---

# 10. Example: Adding NFS Files

Folder structure:

```text
notes/nfs/linux-nfs-study-notes.md
notes/nfs/nfs-wsl-ubuntu-almalinux-from-scratch-to-hero.md
mcqs/nfs/nfs-wsl-lab-25-mcq-quiz.html
```

Then run:

```bash
cd /c/Linux/test-github-actions
./portfolio-upload.sh
```

The cards will be generated automatically.

---

# 11. Troubleshooting

## Problem: `generate_file_cards.py` not found

Error:

```text
ERROR: generate_file_cards.py not found
```

Fix:

```text
Make sure generate_file_cards.py is inside /c/Linux/test-github-actions
```

---

## Problem: `./portfolio-upload.sh: Permission denied`

Fix:

```bash
chmod +x portfolio-upload.sh
./portfolio-upload.sh
```

---

## Problem: Cards do not show on website

Check:

```bash
python generate_file_cards.py
git status
```

Then push again:

```bash
git add -A
git commit -m "Regenerate cards"
git push origin main
```

---

# 12. Final Memory Line

```text
Add files → run ./portfolio-upload.sh → wait for GitHub Actions → check website
```

Alhamdulillah, this is your automated workflow for next time.
