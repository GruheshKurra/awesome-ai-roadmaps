"""Build README.md, roadmaps/*.md, and the website (_site/) from data/.

    python3 scripts/build.py           # write README, roadmap pages, and _site/
    python3 scripts/build.py --check   # fail if README or roadmap pages are stale

Roadmaps live in data/roadmaps/NN-slug.json. Video and repo metadata comes from
data/meta.json, which scripts/refresh_meta.py fills in.
"""

import datetime
import json
import re
import shutil
import subprocess
import sys
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = "GruheshKurra/awesome-ai-roadmaps"
REPO_URL = f"https://github.com/{REPO}"
SITE_URL = "https://gruheshkurra.github.io/awesome-ai-roadmaps"
LEVELS = ("Beginner", "Intermediate", "Advanced")
# Search engine ownership tokens. Paste the content value from Google Search Console
# ("HTML tag" method) or Bing Webmaster Tools; empty values are skipped.
SITE_VERIFICATION = {"google-site-verification": "", "msvalidate.01": ""}
# Public key that lets scripts/indexnow.py tell Bing and other IndexNow engines about updated pages.
INDEXNOW_KEY = "0d573565547455f697c44fa5223bcaff"
TAGLINE = "Learn AI from the best free YouTube videos and GitHub repos, in the right order."
PATHS = [
    ("Total beginner", ["foundations", "machine-learning", "deep-learning"]),
    ("Developer building with AI", ["ai-engineering", "ai-agents"]),
    ("How LLMs really work", ["deep-learning", "llms-from-scratch", "fine-tuning"]),
    ("Production and performance", ["machine-learning", "deploy-and-scale"]),
    ("Data scientist", ["machine-learning", "explainable-ml-shap-lime-and-model-debugging", "causal-inference-and-causal-ml"]),
    ("Trustworthy LLM apps", ["ai-engineering", "evaluation-and-benchmarking-for-llms", "llm-security-and-red-teaming"]),
    ("Vision to 3D worlds", ["deep-learning", "computer-vision", "3d-vision-nerfs-and-gaussian-splatting"]),
    ("Inside modern LLMs", ["llms-from-scratch", "mixture-of-experts-and-efficient-llm-architectures", "interpretability"]),
]


# ---------- data ----------

def load():
    meta = json.loads((ROOT / "data/meta.json").read_text())
    roadmaps = [json.loads(p.read_text()) for p in sorted((ROOT / "data/roadmaps").glob("*.json"))]
    upcoming = json.loads((ROOT / "data/upcoming.json").read_text())
    errors = []
    slugs = [r["slug"] for r in roadmaps]
    if len(set(slugs)) != len(slugs):
        errors.append("duplicate roadmap slugs")
    seen = {}
    for r in roadmaps:
        for key in ("slug", "order", "added", "title", "level", "tagline", "prereqs", "steps", "projects"):
            if key not in r:
                errors.append(f"{r.get('slug')}: missing {key}")
        try:
            datetime.date.fromisoformat(r.get("added", ""))
        except ValueError:
            errors.append(f"{r.get('slug')}: added must be a YYYY-MM-DD date")
        if r.get("level") not in LEVELS:
            errors.append(f"{r['slug']}: level must be one of {LEVELS}")
        if not 6 <= len(r.get("steps", [])) <= 16:
            errors.append(f"{r['slug']}: expected 6-16 steps")
        for step in r.get("steps", []):
            vid = step.get("video")
            if vid not in meta["videos"]:
                errors.append(f"{r['slug']}: video {vid} missing from meta.json (run scripts/refresh_meta.py)")
            elif vid in seen:
                errors.append(f"{r['slug']}: video {vid} already used in {seen[vid]}")
            seen[vid] = r["slug"]
            if step.get("repo") and step["repo"] not in meta["repos"]:
                errors.append(f"{r['slug']}: repo {step['repo']} missing from meta.json")
            if not step.get("title") or not step.get("why"):
                errors.append(f"{r['slug']}: every step needs a title and a why")
    for path in PATHS:
        errors += [f"path {path[0]}: unknown roadmap {s}" for s in path[1] if s not in slugs]
    if errors:
        sys.exit("\n".join(errors))
    for r in roadmaps:
        r["seconds"] = sum(meta["videos"][s["video"]]["seconds"] for s in r["steps"])
        r["repos"] = sorted({s["repo"] for s in r["steps"] if s.get("repo")})
    return roadmaps, meta, upcoming


def duration(seconds):
    hours, minutes = divmod(round(seconds / 60), 60)
    return f"{hours}h {minutes:02d}m" if hours else f"{minutes} min"


def total_hours(seconds):
    return f"{seconds / 3600:.0f}"


def stars(n):
    return f"{n / 1000:.1f}k".replace(".0k", "k") if n >= 1000 else str(n)


def yt(video_id):
    return f"https://www.youtube.com/watch?v={video_id}"


def thumb(video_id):
    return f"https://i.ytimg.com/vi/{video_id}/mqdefault.jpg"


def iso_duration(seconds):
    hours, minutes = divmod(round(seconds / 60), 60)
    return f"PT{hours}H{minutes}M"


def last_changed(*paths):
    """Date of the last commit touching paths, for sitemap lastmod. None outside git."""
    try:
        out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", *paths], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None
    return out or None


def json_ld(data):
    text = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return f'<script type="application/ld+json">{text}</script>'


def link_prereqs(text, roadmaps, href, fmt):
    by_title = {escape(r["title"]) if fmt == "html" else r["title"]: r["slug"] for r in roadmaps}
    text = escape(text) if fmt == "html" else text
    pattern = re.compile("|".join(re.escape(t) for t in sorted(by_title, key=len, reverse=True)))
    def repl(m):
        label = m.group(0)
        return f'<a href="{href(by_title[label])}">{label}</a>' if fmt == "html" else f"[{label}]({href(by_title[label])})"
    return pattern.sub(repl, text)


def md_cell(text):
    return text.replace("|", "\\|")


# ---------- markdown ----------

def readme(roadmaps, meta, upcoming):
    by_slug = {r["slug"]: r for r in roadmaps}
    videos = sum(len(r["steps"]) for r in roadmaps)
    seconds = sum(r["seconds"] for r in roadmaps)
    repos = sorted({repo for r in roadmaps for repo in r["repos"]}, key=lambda k: -meta["repos"][k]["stars"])
    out = [
        "<!-- Generated by scripts/build.py from data/. Edit the data, not this file. -->",
        '<h1 align="center">Awesome AI Roadmaps</h1>',
        "",
        f'<p align="center"><b>{TAGLINE}</b><br>No books, no paywalls, no 40-hour playlists. One great video per step, plus the repo to code along with.</p>',
        "",
        '<p align="center">',
        f'<a href="{SITE_URL}/"><img alt="Website" src="https://img.shields.io/badge/website-open-ff5a1f?style=for-the-badge"></a>',
        f'<a href="{REPO_URL}/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/{REPO}?style=for-the-badge&amp;color=ffb000"></a>',
        f'<a href="{REPO_URL}/commits/main"><img alt="Last commit" src="https://img.shields.io/github/last-commit/{REPO}?style=for-the-badge"></a>',
        f'<a href="https://awesome.re"><img alt="Awesome" src="https://awesome.re/badge-flat2.svg" height="28"></a>',
        "</p>",
        "",
        f'<p align="center"><b>{len(roadmaps)} roadmaps · {videos} videos · {total_hours(seconds)} hours of video · {len(repos)} GitHub repos</b></p>',
        "",
        f'<p align="center"><a href="{SITE_URL}/"><b>Open the interactive website →</b></a> (track your progress, step by step)</p>',
        "",
        f'<p align="center"><a href="{SITE_URL}/"><picture>'
        '<source media="(prefers-color-scheme: dark)" srcset=".github/assets/website-dark.jpg">'
        '<img src=".github/assets/website-light.jpg" width="800" alt="The AI Roadmaps website: a short headline, a Start button, and the first roadmap\'s videos in order">'
        '</picture></a></p>',
        "",
        "## Pick a path",
        "",
        f"New here? Follow the path that matches your goal, or browse [all {len(roadmaps)} roadmaps](#roadmaps) below.",
        "",
    ]
    for name, slugs in PATHS:
        chain = " → ".join(f"[{by_slug[s]['title']}](roadmaps/{s}.md)" for s in slugs)
        out.append(f"- **{name}:** {chain}")
    out += ["", "## Roadmaps", "", "| # | Roadmap | Level | Steps | Video time |", "| ---: | --- | --- | ---: | ---: |"]
    for r in roadmaps:
        out.append(f"| {r['order']} | **[{r['title']}](roadmaps/{r['slug']}.md)**<br><sub>{md_cell(r['tagline'])}</sub> | {r['level']} | {len(r['steps'])} | {duration(r['seconds'])} |")
    start = roadmaps[0]
    out += ["", "## Start right now", "", f"The first five steps of **{start['title']}**. Click a thumbnail to watch.", "", "<table><tr>"]
    for step in start["steps"][:5]:
        v = meta["videos"][step["video"]]
        out.append(f'<td align="center" valign="top" width="20%"><a href="{yt(step["video"])}"><img src="{thumb(step["video"])}" alt="{escape(step["title"])}"></a><br><b>{escape(step["title"])}</b><br><sub>{escape(v["channel"])} · {duration(v["seconds"])}</sub></td>')
    out += ["</tr></table>", "", "## Repos worth starring", "", "The GitHub repos the roadmaps use most. Clone them and code along.", "", "| Repo | Stars | Used in |", "| --- | ---: | --- |"]
    for key in repos[:15]:
        used = ", ".join(f"[{r['title']}](roadmaps/{r['slug']}.md)" for r in roadmaps if key in r["repos"])
        out.append(f"| [{key}](https://github.com/{key}) | ★ {stars(meta['repos'][key]['stars'])} | {used} |")
    out += [
        "", "## How it works", "",
        "- **Video first.** Every step is one YouTube video picked for clarity, not a course homepage or a playlist.",
        "- **Code along.** Where it helps, a step links the GitHub repo that goes with it.",
        "- **In order.** Steps build on each other. Follow a roadmap top to bottom.",
        "- **Build something.** Every roadmap ends with small projects. They make a better portfolio than certificates.",
        "- **Checked.** A script verifies every video is still up and every repo still exists.",
        "", "## Coming next", "", "New roadmaps are added regularly. Next up:", "",
    ]
    out += [f"- {item}" for item in upcoming]
    out += [
        "", "Watch or star the repo to get them as they land.", "",
        "## Contributing", "",
        f"Know a better video for a step, or found a dead link? [Open an issue]({REPO_URL}/issues/new/choose) or read [contributing.md](contributing.md).",
        "", "## Star history", "",
        f"[![Star History Chart](https://api.star-history.com/svg?repos={REPO}&type=Date)](https://star-history.com/#{REPO}&Date)",
        "", "## License", "",
        f"[CC0 1.0]({REPO_URL}/blob/main/LICENSE). The videos and repos belong to their creators. Go subscribe to them and star them.",
        "",
    ]
    return "\n".join(out)


def roadmap_md(r, roadmaps, meta):
    index = roadmaps.index(r)
    out = [
        "<!-- Generated by scripts/build.py from data/. Edit the data, not this file. -->",
        f"# {r['title']}",
        "",
        f"**{r['tagline']}**",
        "",
        f"Level: **{r['level']}** · {len(r['steps'])} steps · {duration(r['seconds'])} of video · Prerequisites: {link_prereqs(r['prereqs'], roadmaps, lambda slug: slug + '.md', 'md')}",
        "",
        f"[Track your progress on the website]({SITE_URL}/{r['slug']}/) · [All roadmaps](../README.md)",
        "",
        "| # | Watch | Step | Code along |",
        "| ---: | --- | --- | --- |",
    ]
    for i, step in enumerate(r["steps"], 1):
        v = meta["videos"][step["video"]]
        watch = f'<a href="{yt(step["video"])}"><img src="{thumb(step["video"])}" width="200" alt="{escape(step["title"])}"></a>'
        text = f"**{md_cell(step['title'])}**<br>[{md_cell(v['title'])}]({yt(step['video'])})<br><sub>{md_cell(v['channel'])} · {duration(v['seconds'])}</sub><br>{md_cell(step['why'])}"
        repo = ""
        if step.get("repo"):
            repo = f"[{step['repo']}](https://github.com/{step['repo']})<br><sub>★ {stars(meta['repos'][step['repo']]['stars'])}</sub>"
        out.append(f"| {i} | {watch} | {text} | {repo} |")
    out += ["", "## Build it", ""] + [f"- {p}" for p in r["projects"]] + [""]
    if index + 1 < len(roadmaps):
        nxt = roadmaps[index + 1]
        out += [f"**Next:** [{nxt['title']}]({nxt['slug']}.md)", ""]
    return "\n".join(out)


# ---------- website ----------

def page(title, description, body, path="", depth=0, schema=(), index=True, social=None):
    # Link previews (Slack, X, LinkedIn, Discord) cut titles near 60-70 characters,
    # so pages can pass a shorter (title, description) pair for og: and twitter: tags.
    social_title, social_description = social or (title, description)
    up = "../" * depth
    canonical = f"{SITE_URL}/{path}"
    robots = "max-image-preview:large" if index else "noindex"
    ld = "".join(f"\n{json_ld(s)}" for s in schema)
    verify = "".join(f'\n<meta name="{name}" content="{escape(value)}">' for name, value in SITE_VERIFICATION.items() if value and depth == 0 and index)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(description)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canonical}">{verify}
<meta name="theme-color" content="#ff5a1f">
<meta property="og:type" content="website">
<meta property="og:site_name" content="AI Roadmaps">
<meta property="og:locale" content="en_US">
<meta property="og:title" content="{escape(social_title)}">
<meta property="og:description" content="{escape(social_description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE_URL}/assets/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="AI Roadmaps: learn AI from free YouTube videos and GitHub repos">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{escape(social_title)}">
<meta name="twitter:description" content="{escape(social_description)}">
<meta name="twitter:image" content="{SITE_URL}/assets/og.png">
<link rel="icon" href="{up}assets/favicon.svg" type="image/svg+xml">{ld}
<link rel="stylesheet" href="{up}assets/style.css">
<script>try{{document.documentElement.dataset.theme=localStorage.getItem('theme')||''}}catch(e){{}}</script>
</head>
<body>
<header class="topbar">
  <a class="brand" href="{up or './'}">AI Roadmaps</a>
  <nav>
    <button class="theme-toggle" type="button" aria-label="Toggle dark mode"></button>
    <a class="star-btn" href="{REPO_URL}" target="_blank" rel="noopener"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.75.75 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Z"/></svg>Star on GitHub</a>
  </nav>
</header>
{body}
<footer class="footer">
  <p>Made for everyone learning AI. Videos and repos belong to their creators; go subscribe and star them.</p>
  <p><a href="{REPO_URL}">GitHub</a> · <a href="{REPO_URL}/issues/new/choose">Suggest a video</a> · <a href="{REPO_URL}/blob/main/LICENSE">CC0 license</a></p>
</footer>
<script src="{up}assets/app.js"></script>
</body>
</html>
"""


def home_html(roadmaps, meta, upcoming):
    by_slug = {r["slug"]: r for r in roadmaps}
    videos = sum(len(r["steps"]) for r in roadmaps)
    seconds = sum(r["seconds"] for r in roadmaps)
    repos = sorted({repo for r in roadmaps for repo in r["repos"]}, key=lambda k: -meta["repos"][k]["stars"])
    cards = []
    for r in roadmaps:
        thumbs = "".join(f'<img src="{thumb(s["video"])}" alt="" loading="lazy">' for s in r["steps"][:3])
        search = " ".join([r["title"], r["tagline"], r["level"]] + [s["title"] for s in r["steps"]]).lower()
        ids = " ".join(s["video"] for s in r["steps"])
        cards.append(f"""<a class="card" href="{r['slug']}/" data-slug="{r['slug']}" data-level="{r['level'].lower()}" data-added="{r['added']}" data-total="{len(r['steps'])}" data-ids="{ids}" data-search="{escape(search)}">
  <div class="mosaic">{thumbs}<span class="num">{r['order']:02d}</span></div>
  <div class="card-body">
    <div class="pills"><span class="pill level-{r['level'].lower()}">{r['level']}</span><span class="pill new" hidden>New</span><span class="muted">{len(r['steps'])} steps · {duration(r['seconds'])}</span></div>
    <h3>{escape(r['title'])}</h3>
    <p>{escape(r['tagline'])}</p>
    <div class="progress" aria-hidden="true"><span></span></div>
    <div class="progress-label muted"></div>
  </div>
</a>""")
    paths = []
    for name, slugs in PATHS:
        links = [f'<a href="{s}/">{escape(by_slug[s]["title"])}</a>' for s in slugs]
        # Keep each arrow on the same line as the roadmap it points to, so wrapping never strands it.
        chain = links[0] + "".join(f'<span class="hop"><span class="arrow" aria-hidden="true">→</span>{link}</span>' for link in links[1:])
        paths.append(f'<div class="path"><h3>{escape(name)}</h3><div class="chain">{chain}</div></div>')
    repo_cards = []
    for key in repos[:12]:
        m = meta["repos"][key]
        repo_cards.append(f'<a class="repo" href="https://github.com/{key}" target="_blank" rel="noopener"><span class="repo-name">{escape(key)}</span><span class="repo-desc">{escape(m["description"][:110])}</span><span class="repo-stars">★ {stars(m["stars"])}</span></a>')
    soon = "".join(f"<li>{escape(item)}</li>" for item in upcoming)
    levels = ["Beginner", "Intermediate", "Advanced"]
    chips = f'<button type="button" class="chip" data-level="all" aria-pressed="true">All <span class="muted">{len(roadmaps)}</span></button>' + "".join(
        f'<button type="button" class="chip" data-level="{lv.lower()}" aria-pressed="false">{lv} <span class="muted">{sum(1 for r in roadmaps if r["level"] == lv)}</span></button>' for lv in levels)
    first = roadmaps[0]
    peek = "".join(f'<li><img src="{thumb(st["video"])}" alt="" loading="lazy" width="96" height="54"><span class="peek-title">{escape(st["title"])}</span><span class="muted peek-dur">{duration(meta["videos"][st["video"]]["seconds"])}</span></li>' for st in first["steps"][:5])
    faq = [
        ("How can I learn AI for free?", f"Pick a roadmap and watch its videos in order. All {len(roadmaps)} roadmaps are made of free YouTube videos and open-source GitHub repos, with no sign-up, paywall, or trial."),
        ("Where should a complete beginner start?", f"Start with {first['title']} ({duration(first['seconds'])} of video), then Machine Learning and Deep Learning. After that, choose a roadmap for what you want to build: LLMs, agents, computer vision, generative AI, or deployment."),
        ("How long does each roadmap take?", f"Between {duration(min(r['seconds'] for r in roadmaps))} and {duration(max(r['seconds'] for r in roadmaps))} of video, {total_hours(seconds)} hours in total. Plan for about twice that if you code along and build one of the projects at the end of each roadmap."),
        ("Do I need an account to track my progress?", "No. Tick off each step as you finish it. Your progress is saved in your browser, and nothing is sent anywhere."),
        ("How are the videos chosen?", "One specific video per step, never a whole playlist. Clear and short beats famous and long, every video is free to watch, and links are checked regularly so dead videos get replaced. Anyone can suggest a better one on GitHub."),
    ]
    faq_html = "".join(f"<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>" for q, a in faq)
    body = f"""<main>
<section class="hero">
  <div class="hero-copy">
    <h1>Learn AI from free YouTube videos, in a sensible order.</h1>
    <p class="lead">Every step is one video and, where it helps, one GitHub repo to code along with. No books, no paywalls, no playlists to sort through. Tick steps off as you go; your progress stays in your browser.</p>
    <a class="resume" id="resume" href="#roadmaps" hidden>
      <span class="resume-kicker">Continue learning</span>
      <strong class="resume-title"></strong>
      <span class="resume-meta muted"></span>
    </a>
    <div class="cta">
      <a class="btn primary" href="{roadmaps[0]['slug']}/">Start with {escape(roadmaps[0]['title'])}</a>
      <a class="btn" href="#roadmaps">Browse all roadmaps</a>
    </div>
    <p class="facts muted">{len(roadmaps)} roadmaps · {videos} videos · {total_hours(seconds)} hours · {len(repos)} repos · free, no account</p>
  </div>
  <a class="peek" href="{roadmaps[0]['slug']}/" aria-label="Preview of the {escape(roadmaps[0]['title'])} roadmap">
    <span class="peek-head"><strong>{escape(roadmaps[0]['title'])}</strong><span class="muted">{len(roadmaps[0]['steps'])} steps · {duration(roadmaps[0]['seconds'])}</span></span>
    <ol>{peek}</ol>
  </a>
</section>
<section id="roadmaps" class="section">
  <div class="section-head">
    <h2>Roadmaps</h2>
    <label class="search"><span class="visually-hidden">Search roadmaps</span><input type="search" id="search" placeholder="Search: transformers, RAG, YOLO, CUDA…" autocomplete="off"></label>
  </div>
  <div class="chips" role="group" aria-label="Filter by level">{chips}</div>
  <div class="grid" id="grid">
{''.join(cards)}
  </div>
  <p class="empty muted" id="empty" hidden>No roadmap matches that yet. Try another word.</p>
</section>
<section class="section">
  <h2>Pick a path</h2>
  <div class="paths">{''.join(paths)}</div>
</section>
<section class="section">
  <h2>Repos worth starring</h2>
  <p class="muted">The repositories these roadmaps code along with.</p>
  <div class="repos">{''.join(repo_cards)}</div>
</section>
<section class="section soon">
  <h2>Coming next</h2>
  <p class="muted">New roadmaps land regularly. <a href="{REPO_URL}">Star the repo</a> to catch them.</p>
  <ul>{soon}</ul>
</section>
<section class="section faq">
  <h2>Questions</h2>
  {faq_html}
</section>
</main>"""
    description = f"{len(roadmaps)} free AI roadmaps built from {videos} YouTube videos and {len(repos)} GitHub repos, from Python and ML basics to LLMs, agents, vision, robotics, and AI safety."
    schema = [
        {"@context": "https://schema.org", "@type": "WebSite", "name": "AI Roadmaps", "alternateName": "Awesome AI Roadmaps", "url": f"{SITE_URL}/", "description": description, "inLanguage": "en", "sameAs": [REPO_URL]},
        {"@context": "https://schema.org", "@type": "ItemList", "name": "AI roadmaps", "itemListElement": [{"@type": "ListItem", "position": i, "url": f"{SITE_URL}/{r['slug']}/", "name": r["title"]} for i, r in enumerate(roadmaps, 1)]},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]},
    ]
    return page("Free AI Roadmaps: Learn AI with YouTube Videos & GitHub Repos", description, body, schema=schema)


def roadmap_html(r, roadmaps, meta):
    index = roadmaps.index(r)
    steps = []
    for i, step in enumerate(r["steps"], 1):
        v = meta["videos"][step["video"]]
        repo = ""
        if step.get("repo"):
            m = meta["repos"][step["repo"]]
            repo = f'<a class="repo-chip" href="https://github.com/{step["repo"]}" target="_blank" rel="noopener"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg>{escape(step["repo"])}<span>★ {stars(m["stars"])}</span></a>'
        steps.append(f"""<li class="step" id="step-{i}" data-id="{step['video']}">
  <a class="thumb" href="{yt(step['video'])}" target="_blank" rel="noopener" aria-label="Watch {escape(v['title'])} on YouTube">
    <img src="{thumb(step['video'])}" alt="" loading="lazy"><span class="play" aria-hidden="true"></span><span class="dur">{duration(v['seconds'])}</span>
  </a>
  <div class="step-body">
    <div class="step-top"><span class="step-num">Step {i}</span>
      <label class="done"><input type="checkbox" data-id="{step['video']}"><span>Done</span></label></div>
    <h3>{escape(step['title'])}</h3>
    <p class="why">{escape(step['why'])}</p>
    <a class="vtitle" href="{yt(step['video'])}" target="_blank" rel="noopener">{escape(v['title'])}</a>
    <p class="channel muted">{escape(v['channel'])}</p>
    {repo}
  </div>
</li>""")
    projects = "".join(f"<li>{escape(p)}</li>" for p in r["projects"])
    nav = ""
    if index + 1 < len(roadmaps):
        nxt = roadmaps[index + 1]
        nav = f'<a class="next" href="../{nxt["slug"]}/"><span class="muted">Next roadmap</span><strong>{escape(nxt["title"])} →</strong></a>'
    others = "".join(f'<a href="../{o["slug"]}/">{escape(o["title"])}</a>' for o in roadmaps if o is not r)
    url = f"{SITE_URL}/{r['slug']}/"
    description = f"{r['title']}: {r['tagline']} {len(r['steps'])} free YouTube videos with GitHub repos to code along."
    schema = [
        {"@context": "https://schema.org", "@type": "Course", "name": f"{r['title']} roadmap", "description": r["tagline"], "url": url, "inLanguage": "en",
         "provider": {"@type": "Organization", "name": "AI Roadmaps", "url": f"{SITE_URL}/"},
         "isAccessibleForFree": True, "educationalLevel": r["level"], "coursePrerequisites": r["prereqs"], "timeRequired": iso_duration(r["seconds"]),
         "offers": {"@type": "Offer", "category": "Free", "price": 0, "priceCurrency": "USD"},
         "hasCourseInstance": {"@type": "CourseInstance", "courseMode": "Online", "courseWorkload": iso_duration(r["seconds"])},
         "syllabusSections": [{"@type": "Syllabus", "name": s["title"], "description": s["why"]} for s in r["steps"]]},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "AI Roadmaps", "item": f"{SITE_URL}/"},
            {"@type": "ListItem", "position": 2, "name": r["title"], "item": url}]},
    ]
    body = f"""<main class="roadmap" data-slug="{r['slug']}" data-total="{len(r['steps'])}">
<section class="rm-hero">
  <a class="back muted" href="../">← All roadmaps</a>
  <div class="pills"><span class="pill level-{r['level'].lower()}">{r['level']}</span><span class="muted">Roadmap {r['order']:02d} · {len(r['steps'])} steps · {duration(r['seconds'])} of video</span></div>
  <h1>{escape(r['title'])}</h1>
  <p class="lead">{escape(r['tagline'])}</p>
  <p class="muted"><strong>Before this:</strong> {link_prereqs(r['prereqs'], roadmaps, lambda slug: '../' + slug + '/', 'html')}</p>
  <div class="rm-progress">
    <div class="progress big" aria-hidden="true"><span></span></div>
    <div class="rm-progress-row"><span class="progress-label"></span><button type="button" class="reset">Reset</button></div>
    <a class="continue" href="#step-1" hidden></a>
  </div>
</section>
<ol class="steps">
{''.join(steps)}
</ol>
<section class="build">
  <h2>Build it</h2>
  <p class="muted">Watching isn't learning. Pick one and put it on GitHub.</p>
  <ul>{projects}</ul>
</section>
{nav}
<nav class="more" aria-label="More roadmaps">
  <h2>More free AI roadmaps</h2>
  <div class="more-links">{others}</div>
</nav>
</main>"""
    social = (f"{r['title']}: {len(r['steps'])} free videos", f"{r['tagline']} {r['level']} · {len(r['steps'])} steps · {duration(r['seconds'])} of video.")
    return page(f"{r['title']} Roadmap: Free Video Course in {len(r['steps'])} Steps | AI Roadmaps", description, body, f"{r['slug']}/", 1, schema, social=social)


def build_site(roadmaps, meta, upcoming):
    site = ROOT / "_site"
    shutil.rmtree(site, ignore_errors=True)
    shutil.copytree(ROOT / "site", site)
    (site / "index.html").write_text(home_html(roadmaps, meta, upcoming))
    for r in roadmaps:
        (site / r["slug"]).mkdir()
        (site / r["slug"] / "index.html").write_text(roadmap_html(r, roadmaps, meta))
    (site / "404.html").write_text(page("Page not found | AI Roadmaps", "This page does not exist.", '<main class="notfound"><h1>Lost?</h1><p class="lead">That page doesn\'t exist, or a roadmap moved.</p><a class="btn primary" href="/awesome-ai-roadmaps/">See all roadmaps</a></main>', "404.html", index=False))
    files = sorted((ROOT / "data/roadmaps").glob("*.json"))
    urls = [(f"{SITE_URL}/", last_changed("data", "scripts/build.py", "site"))]
    urls += [(f"{SITE_URL}/{r['slug']}/", last_changed(str(f.relative_to(ROOT)), "data/meta.json")) for r, f in zip(roadmaps, files)]
    entries = "".join(f"  <url><loc>{u}</loc>{f'<lastmod>{d}</lastmod>' if d else ''}</url>\n" for u, d in urls)
    (site / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{entries}</urlset>\n')
    (site / f"{INDEXNOW_KEY}.txt").write_text(INDEXNOW_KEY)
    (site / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
    lines = [f"# AI Roadmaps\n\n> {TAGLINE} Free, video-first learning paths: each step is one YouTube video plus a GitHub repo to code along with.\n\n## Roadmaps\n"]
    lines += [f"- [{r['title']}]({SITE_URL}/{r['slug']}/): {r['level']}, {len(r['steps'])} steps, {duration(r['seconds'])} of video. {r['tagline']}" for r in roadmaps]
    lines += [f"\n## Source\n\n- [GitHub repository]({REPO_URL}): roadmap data, CC0 licensed.\n"]
    (site / "llms.txt").write_text("\n".join(lines))


def main():
    check = "--check" in sys.argv
    roadmaps, meta, upcoming = load()
    files = {ROOT / "README.md": readme(roadmaps, meta, upcoming)}
    files.update({ROOT / "roadmaps" / f"{r['slug']}.md": roadmap_md(r, roadmaps, meta) for r in roadmaps})
    stale = [p for p, text in files.items() if not p.exists() or p.read_text() != text]
    extra = [p for p in (ROOT / "roadmaps").glob("*.md") if p not in files]
    if check:
        if stale or extra:
            sys.exit("Stale generated files, run python3 scripts/build.py: " + ", ".join(str(p.relative_to(ROOT)) for p in stale + extra))
        print(f"Up to date: {len(roadmaps)} roadmaps.")
        return
    (ROOT / "roadmaps").mkdir(exist_ok=True)
    for p in extra:
        p.unlink()
    for p, text in files.items():
        p.write_text(text)
    build_site(roadmaps, meta, upcoming)
    print(f"Built {len(roadmaps)} roadmaps, {sum(len(r['steps']) for r in roadmaps)} steps.")


if __name__ == "__main__":
    main()
