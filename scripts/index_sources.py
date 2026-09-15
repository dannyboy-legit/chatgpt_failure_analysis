import datetime
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
QUEUE = ROOT / "source_queue"
OUT = ROOT / "SOURCE_INDEX.md"
files = sorted(QUEUE.glob("*.md"))[-24:] if QUEUE.exists() else []

urls = {}
errors = []
for p in files:
    text = p.read_text(encoding="utf-8", errors="replace")
    current_title = None
    for line in text.splitlines():
        if line.startswith("### "):
            current_title = line[4:].strip()
        elif line.startswith("- URL: "):
            url = line[len("- URL: "):].strip()
            if url:
                urls[url] = {"title": current_title or url, "file": p.name}
        elif "COLLECTOR ERROR" in line:
            errors.append(f"{p.name}: {line}")

now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
lines = [
    "# Source Queue Index",
    "",
    f"Updated: {now}",
    "",
    "This is a mechanical index, not an analysis. Sources remain unverified until the hourly ChatGPT research pass reads and evaluates them.",
    "",
    f"Queue files indexed: {len(files)}",
    f"Unique candidate URLs: {len(urls)}",
    "",
    "## Queue files",
    "",
]
for p in reversed(files):
    lines.append(f"- `source_queue/{p.name}`")
lines += ["", "## Unique candidates", ""]
for url, meta in sorted(urls.items(), key=lambda kv: (kv[1]["title"].lower(), kv[0])):
    title = re.sub(r"\s+", " ", meta["title"]).strip()
    lines.append(f"- [{title}]({url}) — discovered in `{meta['file']}`")
if errors:
    lines += ["", "## Collector errors", ""]
    lines.extend(f"- {e}" for e in errors[-30:])
OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(OUT)
