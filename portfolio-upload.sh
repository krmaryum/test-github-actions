#!/bin/bash

# ============================================================
# Portfolio Website Auto Upload Script
# ============================================================
# Project:
#   Khalid Khan Linux & DevOps Portfolio
#
# Repo:
#   /c/Linux/test-github-actions
#
# What this script does:
#   1. Goes to your portfolio repo.
#   2. Runs generate_file_cards.py.
#   3. Automatically updates notes/index.html and mcqs/index.html.
#   4. Shows git status.
#   5. Stages all changes.
#   6. Asks for a commit message.
#   7. Commits and pushes to GitHub.
#
# Use this after adding new files into:
#   notes/
#   md/
#   pdfs/
#   mcqs/
# ============================================================

set -e

REPO_DIR="/c/Linux/test-github-actions"
DEFAULT_COMMIT_MESSAGE="Add new study notes and MCQs"

echo "=========================================="
echo " Portfolio Auto Upload Script"
echo "=========================================="
echo

echo "Going to repo:"
echo "$REPO_DIR"
echo

cd "$REPO_DIR" || {
  echo "ERROR: Repo folder not found: $REPO_DIR"
  exit 1
}

echo "Current folder:"
pwd
echo

echo "Step 1: Checking generator file..."
if [ ! -f "generate_file_cards.py" ]; then
  echo "ERROR: generate_file_cards.py not found in repo root."
  echo "Please place generate_file_cards.py inside:"
  echo "$REPO_DIR"
  exit 1
fi

echo "Generator found."
echo

echo "Step 2: Generating notes and MCQ cards..."
python generate_file_cards.py
echo

echo "Step 3: Git status after generation..."
git status
echo

echo "Step 4: Staging all changes..."
git add -A
echo

if git diff --cached --quiet; then
  echo "No changes to commit."
  echo "Nothing to push."
  exit 0
fi

echo "Step 5: Commit message"
echo "Default commit message:"
echo "$DEFAULT_COMMIT_MESSAGE"
echo

read -p "Enter custom commit message, or press Enter to use default: " USER_COMMIT_MESSAGE

if [ -z "$USER_COMMIT_MESSAGE" ]; then
  COMMIT_MESSAGE="$DEFAULT_COMMIT_MESSAGE"
else
  COMMIT_MESSAGE="$USER_COMMIT_MESSAGE"
fi

echo
echo "Using commit message:"
echo "$COMMIT_MESSAGE"
echo

echo "Step 6: Committing changes..."
git commit -m "$COMMIT_MESSAGE"
echo

echo "Step 7: Pushing to GitHub..."
git push origin main
echo

echo "=========================================="
echo "Done bhai!"
echo "GitHub Pages will deploy your updated website."
echo "Check GitHub Actions, then open:"
echo "https://khalidkhan.me"
echo "=========================================="
