# How to Add Future Study Notes and MCQs

This portfolio is organized for GitHub Pages.

## Add a new MCQ quiz

1. Put the HTML quiz file inside the correct folder under `mcqs/`.
2. Add one new card/link in `mcqs/index.html`.
3. Commit and push.

Example:

```bash
mkdir -p mcqs/github-actions
cp day-47-mcq.html mcqs/github-actions/
```

Then edit `mcqs/index.html` and add a new card that links to:

```text
github-actions/day-47-mcq.html
```

## Add a new study note

1. Put the Markdown file inside the correct folder under `notes/`.
2. Add one new card/link in `notes/index.html`.
3. Commit and push.

Example:

```bash
mkdir -p notes/github-actions
cp day-47-scheduled-workflows.md notes/github-actions/
```

Then edit `notes/index.html` and add a card that links to:

```text
github-actions/day-47-scheduled-workflows.md
```

## Push changes

```bash
git add .
git commit -m "Add new study notes and MCQs"
git push origin main
```

## Recommended future folders

```text
notes/linux/
notes/git-github/
notes/github-actions/
notes/docker/
notes/kubernetes/
notes/web-servers/

mcqs/linux/
mcqs/git-github/
mcqs/github-actions/
mcqs/docker/
mcqs/kubernetes/
mcqs/web-servers/
```
