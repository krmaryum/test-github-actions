#!/usr/bin/env python3
"""
Auto-generate Study Notes and MCQ index cards.

Important fix:
- Markdown (.md) files open through notes/viewer.html so they look styled.
- They will NOT open as raw plain text.

Use from repo root:
    python generate_file_cards.py
"""

from pathlib import Path
from datetime import datetime
import html
import os
import re

ROOT = Path(__file__).resolve().parent

# Use only these folders for your portfolio library
NOTE_ROOTS = ["notes", "pdfs"]
MCQ_ROOT = "mcqs"

NOTE_EXTS = {".md", ".html", ".pdf", ".docx", ".xlsx", ".xls", ".pptx", ".txt", ".png", ".jpg", ".jpeg", ".webp"}
MCQ_EXTS = {".html"}

IGNORE_FILE_NAMES = {"index.html", "viewer.html"}
IGNORE_DIRS = {".git", ".github", "assets", "images", "templates", "backup", "old", "__pycache__"}


def clean_title(path: Path) -> str:
    name = path.stem
    name = re.sub(r"[-_]+", " ", name)
    name = re.sub(r"\s+", " ", name).strip()
    return name.title() if name else path.name


def category_from_path(path: Path, root_name: str) -> str:
    try:
        rel = path.relative_to(ROOT / root_name)
    except ValueError:
        return "General"

    parts = rel.parts
    if len(parts) >= 2:
        return parts[0].replace("-", " ").replace("_", " ").title()
    return "General"


def file_type_label(path: Path) -> str:
    labels = {
        ".md": "Markdown",
        ".html": "HTML",
        ".pdf": "PDF",
        ".docx": "DOCX",
        ".xlsx": "Spreadsheet",
        ".xls": "Spreadsheet",
        ".pptx": "Slides",
        ".txt": "Text",
    }
    return labels.get(path.suffix.lower(), path.suffix.replace(".", "").upper())


def should_skip(path: Path) -> bool:
    if path.name in IGNORE_FILE_NAMES:
        return True
    if any(part in IGNORE_DIRS for part in path.parts):
        return True
    return False


def rel_link(from_dir: Path, target: Path) -> str:
    return Path(os.path.relpath(target, start=from_dir)).as_posix()


def notes_href(path: Path, root_name: str) -> str:
    notes_dir = ROOT / "notes"

    # Important: Markdown inside notes/ should open with styled viewer.
    # Example:
    # notes/nfs/file.md -> viewer.html?file=nfs/file.md
    if path.suffix.lower() == ".md" and root_name == "notes":
        file_for_viewer = path.relative_to(notes_dir).as_posix()
        return "viewer.html?file=" + file_for_viewer

    # PDFs and other files open directly.
    return rel_link(notes_dir, path)


def scan_study_files():
    items = []
    for root_name in NOTE_ROOTS:
        root = ROOT / root_name
        if not root.exists():
            continue

        for path in sorted(root.rglob("*")):
            if not path.is_file():
                continue
            if should_skip(path):
                continue
            if path.suffix.lower() not in NOTE_EXTS:
                continue

            items.append({
                "title": clean_title(path),
                "href": notes_href(path, root_name),
                "category": category_from_path(path, root_name),
                "type": file_type_label(path),
                "source_root": root_name,
                "extension": path.suffix.lower(),
            })
    return items


def scan_mcq_files():
    items = []
    root = ROOT / MCQ_ROOT
    if not root.exists():
        return items

    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if should_skip(path):
            continue
        if path.suffix.lower() not in MCQ_EXTS:
            continue

        items.append({
            "title": clean_title(path),
            "href": rel_link(ROOT / "mcqs", path),
            "category": category_from_path(path, MCQ_ROOT),
            "type": "Quiz",
        })
    return items


def group_items(items):
    grouped = {}
    for item in items:
        grouped.setdefault(item["category"], []).append(item)
    return dict(sorted(grouped.items(), key=lambda kv: kv[0].lower()))


BASE_CSS = """
    * { margin:0; padding:0; box-sizing:border-box; scroll-behavior:smooth; }
    body { font-family: Arial, Helvetica, sans-serif; background:#06111f; color:#fff; overflow-x:hidden; line-height:1.7; }
    body::before { content:""; position:fixed; inset:0; background: radial-gradient(circle at 10% 10%, rgba(34,211,238,.25), transparent 28%), radial-gradient(circle at 90% 25%, rgba(139,92,246,.22), transparent 32%), radial-gradient(circle at 50% 95%, rgba(16,185,129,.16), transparent 30%); z-index:-2; }
    body::after { content:""; position:fixed; inset:0; background-image: linear-gradient(rgba(255,255,255,.03) 1px,transparent 1px), linear-gradient(90deg,rgba(255,255,255,.03) 1px,transparent 1px); background-size:45px 45px; z-index:-1; mask-image:linear-gradient(to bottom,black,transparent 90%); }
    a { color:inherit; text-decoration:none; }
    .container { width:min(1180px,92%); margin:auto; }
    header { padding:24px 0; position:sticky; top:0; z-index:10; background:rgba(6,17,31,.65); backdrop-filter:blur(18px); border-bottom:1px solid rgba(255,255,255,.08); }
    .nav { display:flex; justify-content:space-between; align-items:center; gap:18px; }
    .brand { display:flex; align-items:center; gap:12px; }
    .logo { width:46px; height:46px; display:grid; place-items:center; border-radius:16px; background:rgba(255,255,255,.12); border:1px solid rgba(255,255,255,.15); color:#67e8f9; font-weight:900; }
    .brand h3 { font-size:18px; letter-spacing:.4px; }
    .brand p { color:#cbd5e1; font-size:12px; margin-top:3px; }
    nav ul { display:flex; list-style:none; gap:24px; color:#cbd5e1; font-size:14px; }
    nav a:hover { color:#67e8f9; }
    .hero { padding:74px 0 44px; }
    .badge { display:inline-block; padding:10px 18px; border-radius:999px; background:rgba(255,255,255,.10); border:1px solid rgba(255,255,255,.14); color:#a5f3fc; font-size:14px; margin-bottom:22px; }
    h1 { font-size:clamp(42px,7vw,72px); line-height:1.05; letter-spacing:-2px; margin-bottom:20px; }
    .gradient-text { background:linear-gradient(90deg,#67e8f9,#38bdf8,#a78bfa); -webkit-background-clip:text; background-clip:text; color:transparent; }
    .hero p { color:#cbd5e1; font-size:18px; line-height:1.8; max-width:760px; }
    .section { padding:35px 0 75px; }
    .section-label { color:#67e8f9; text-transform:uppercase; letter-spacing:4px; font-size:13px; margin-bottom:14px; font-weight:700; }
    .category { margin-top:34px; }
    .category h2 { font-size:clamp(26px,4vw,42px); margin-bottom:18px; }
    .grid { display:grid; grid-template-columns:repeat(3,1fr); gap:22px; }
    .card { min-height:210px; padding:28px; display:flex; flex-direction:column; justify-content:space-between; background:rgba(255,255,255,.10); border:1px solid rgba(255,255,255,.16); backdrop-filter:blur(20px); -webkit-backdrop-filter:blur(20px); border-radius:28px; box-shadow:0 25px 70px rgba(0,0,0,.28); transition:.35s ease; }
    .card:hover { transform:translateY(-8px); border-color:rgba(103,232,249,.55); background:rgba(255,255,255,.15); box-shadow:0 30px 85px rgba(34,211,238,.14); }
    .tag { display:inline-block; padding:8px 12px; border-radius:999px; background:rgba(103,232,249,.13); color:#a5f3fc; font-size:12px; font-weight:800; margin-bottom:16px; }
    .card h3 { font-size:22px; margin-bottom:12px; }
    .card p { color:#cbd5e1; line-height:1.7; }
    .buttons { display:flex; flex-wrap:wrap; gap:12px; margin-top:22px; }
    .btn { padding:13px 18px; border-radius:16px; font-weight:700; transition:.3s; display:inline-flex; align-items:center; gap:8px; cursor:pointer; background:#67e8f9; color:#06111f; }
    .btn:hover { transform:translateY(-4px); box-shadow:0 18px 38px rgba(103,232,249,.18); }
    .empty { padding:26px; border-radius:22px; background:rgba(255,255,255,.08); color:#cbd5e1; border:1px solid rgba(255,255,255,.14); }
    footer { text-align:center; padding:28px; color:#94a3b8; border-top:1px solid rgba(255,255,255,.08); }
    @media (max-width:900px) { nav ul { display:none; } .grid { grid-template-columns:1fr; } }
"""


def build_notes_html(items):
    grouped = group_items(items)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    sections = []

    if not grouped:
        sections.append('<div class="empty">No study notes found yet. Add files under notes/ or pdfs/ and run the generator again.</div>')
    else:
        for category, category_items in grouped.items():
            cards = []
            for item in category_items:
                title = html.escape(item["title"])
                href = html.escape(item["href"])
                file_type = html.escape(item["type"])
                root = html.escape(item["source_root"])
                open_label = "Open Notes →" if item["extension"] == ".md" else "Open →"

                cards.append(f"""
          <article class="card">
            <div>
              <span class="tag">{file_type}</span>
              <h3>{title}</h3>
              <p>Source folder: {root}/</p>
            </div>
            <div class="buttons">
              <a class="btn" href="{href}">{open_label}</a>
            </div>
          </article>""")

            sections.append(f"""
        <div class="category">
          <h2>{html.escape(category)}</h2>
          <div class="grid">
{''.join(cards)}
          </div>
        </div>""")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Study Notes | Khalid Khan</title>
  <style>{BASE_CSS}</style>
</head>
<body>
  <header>
    <div class="container nav">
      <a class="brand" href="../index.html">
        <div class="logo">KK</div>
        <div>
          <h3>Khalid Khan</h3>
          <p>Linux • DevOps • Cloud</p>
        </div>
      </a>
      <nav>
        <ul>
          <li><a href="../index.html">Home</a></li>
          <li><a href="index.html">Study Notes</a></li>
          <li><a href="../mcqs/index.html">MCQs</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <main class="container">
    <section class="hero">
      <span class="badge">Auto-generated</span>
      <h1>Study <span class="gradient-text">Notes</span></h1>
      <p>Markdown files open through the styled notes viewer. Last generated: {html.escape(now)}</p>
    </section>

    <section class="section">
      <p class="section-label">Library</p>
{''.join(sections)}
    </section>
  </main>

  <footer>© 2026 Khalid Khan. Auto-generated Study Notes index.</footer>
</body>
</html>
"""


def build_mcqs_html(items):
    grouped = group_items(items)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    sections = []

    if not grouped:
        sections.append('<div class="empty">No MCQ quizzes found yet. Add HTML quiz files under mcqs/ and run the generator again.</div>')
    else:
        for category, category_items in grouped.items():
            cards = []
            for item in category_items:
                title = html.escape(item["title"])
                href = html.escape(item["href"])
                cards.append(f"""
          <article class="card">
            <div>
              <span class="tag">Quiz</span>
              <h3>{title}</h3>
              <p>Interactive browser-based MCQ practice.</p>
            </div>
            <div class="buttons">
              <a class="btn" href="{href}">Start Quiz →</a>
            </div>
          </article>""")

            sections.append(f"""
        <div class="category">
          <h2>{html.escape(category)}</h2>
          <div class="grid">
{''.join(cards)}
          </div>
        </div>""")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>MCQs | Khalid Khan</title>
  <style>{BASE_CSS}</style>
</head>
<body>
  <header>
    <div class="container nav">
      <a class="brand" href="../index.html">
        <div class="logo">KK</div>
        <div>
          <h3>Khalid Khan</h3>
          <p>Linux • DevOps • Cloud</p>
        </div>
      </a>
      <nav>
        <ul>
          <li><a href="../index.html">Home</a></li>
          <li><a href="../notes/index.html">Study Notes</a></li>
          <li><a href="index.html">MCQs</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <main class="container">
    <section class="hero">
      <span class="badge">Auto-generated</span>
      <h1>Practice <span class="gradient-text">MCQs</span></h1>
      <p>These quiz cards are generated automatically from HTML quiz files inside mcqs/. Last generated: {html.escape(now)}</p>
    </section>

    <section class="section">
      <p class="section-label">Practice Center</p>
{''.join(sections)}
    </section>
  </main>

  <footer>© 2026 Khalid Khan. Auto-generated MCQ index.</footer>
</body>
</html>
"""


def main():
    (ROOT / "notes").mkdir(exist_ok=True)
    (ROOT / "mcqs").mkdir(exist_ok=True)
    (ROOT / "pdfs").mkdir(exist_ok=True)

    study_items = scan_study_files()
    mcq_items = scan_mcq_files()

    (ROOT / "notes" / "index.html").write_text(build_notes_html(study_items), encoding="utf-8")
    (ROOT / "mcqs" / "index.html").write_text(build_mcqs_html(mcq_items), encoding="utf-8")

    print(f"Generated notes/index.html with {len(study_items)} study files.")
    print(f"Generated mcqs/index.html with {len(mcq_items)} quiz files.")
    print("Markdown links now use notes/viewer.html, not raw .md pages.")


if __name__ == "__main__":
    main()
