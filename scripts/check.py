#!/usr/bin/env python3
"""Validate README.md structure and the link ledger. Run from the repo root."""
import json, re, sys
from pathlib import Path

MAX_ENTRIES = 150
root = Path(__file__).resolve().parent.parent
readme = (root / "README.md").read_text()
ledger = json.loads((root / "data" / "links.json").read_text())
errors, urls, rows = [], [], 0

for n, line in enumerate(readme.splitlines(), 1):
    if not line.startswith("|") or line.startswith("| ---") or line.startswith("| Concept"):
        continue
    cells = [c.strip() for c in re.split(r"(?<!\\)\|", line.strip().strip("|"))]
    rows += 1
    if len(cells) != 4:
        errors.append(f"line {n}: expected 4 cells, got {len(cells)}")
        continue
    concept, watch, read, why = cells
    if not concept or not why:
        errors.append(f"line {n}: concept and why are required")
    if watch == read == "–":
        errors.append(f"line {n}: needs a Watch or Read link")
    if watch != "–" and not re.fullmatch(r"\*\*\[[^\]]+\]\(https://www\.youtube\.com/watch\?v=[\w-]+\)\*\*", watch):
        errors.append(f"line {n}: Watch must be one bold YouTube watch link")
    if read != "–" and not re.fullmatch(r"\[[^\]]+\]\(https?://[^)\s]+\)", read):
        errors.append(f"line {n}: Read must be one plain link")
    urls += re.findall(r"\]\((https?://[^)\s]+)\)", watch + read)

for u in urls:
    if "list=" in u or "/playlist" in u:
        errors.append(f"playlist link: {u}")
dups = {u for u in urls if urls.count(u) > 1}
for u in sorted(dups):
    errors.append(f"duplicate link: {u}")
for u in sorted(set(urls) - set(ledger)):
    errors.append(f"missing from data/links.json: {u}")
for u in sorted(set(ledger) - set(urls)):
    errors.append(f"stale ledger entry (not in README): {u}")
for u, e in ledger.items():
    if e.get("status") not in {"carried-over", "verified"}:
        errors.append(f"ledger status must be carried-over or verified: {u}")
    if e.get("status") == "verified" and not (e.get("checked") and e.get("note")):
        errors.append(f"verified entry needs checked date and note: {u}")
if rows > MAX_ENTRIES:
    errors.append(f"{rows} entries exceeds cap of {MAX_ENTRIES}; replace or remove weaker picks")

if errors:
    print("\n".join(errors)); sys.exit(1)
verified = sum(e["status"] == "verified" for e in ledger.values())
print(f"ok: {rows} entries, {len(set(urls))} links, {verified} verified")
