import datetime
import html
import json
import os
import pathlib
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUTDIR = ROOT / "source_queue"
OUTDIR.mkdir(exist_ok=True)
NOW = datetime.datetime.now(datetime.timezone.utc)
STOP = datetime.datetime.fromisoformat("2026-09-15T22:23:00+00:00")
if NOW >= STOP:
    print("Stop time reached; no source collection.")
    raise SystemExit(0)

ARXIV_QUERIES = [
    "large language model instruction following agent tool use",
    "long context language model instruction following",
    "LLM agent reliability tool use",
    "LLM self correction external feedback",
    "identity preserving image generation reference",
    "multi reference image generation identity",
    "subject driven image generation pose expression identity",
    "LLM agent failure recovery tool calling",
]

GITHUB_QUERIES = [
    '"image_gen" reference image ignored',
    '"identity drift" image generation reference',
    '"tool call" retry loop agent',
    '"same tool call" repeated agent',
    '"reference image" ignored generation',
    '"context" instruction ignored agent',
]

UA = "chatgpt-failure-analysis-source-collector/1.0"

def get(url, headers=None, timeout=30):
    h = {"User-Agent": UA, "Accept": "application/json, application/atom+xml, text/xml;q=0.9, */*;q=0.8"}
    if headers:
        h.update(headers)
    req = urllib.request.Request(url, headers=h)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def collect_arxiv():
    ns = {"a": "http://www.w3.org/2005/Atom"}
    rows = []
    for q in ARXIV_QUERIES:
        params = urllib.parse.urlencode({
            "search_query": "all:" + q,
            "start": 0,
            "max_results": 6,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        })
        url = "https://export.arxiv.org/api/query?" + params
        try:
            root = ET.fromstring(get(url))
            for e in root.findall("a:entry", ns):
                title = " ".join((e.findtext("a:title", default="", namespaces=ns)).split())
                summary = " ".join((e.findtext("a:summary", default="", namespaces=ns)).split())
                link = e.findtext("a:id", default="", namespaces=ns)
                published = e.findtext("a:published", default="", namespaces=ns)
                authors = [a.findtext("a:name", default="", namespaces=ns) for a in e.findall("a:author", ns)]
                rows.append({"query": q, "title": title, "url": link, "published": published, "authors": authors, "summary": summary})
        except Exception as ex:
            rows.append({"query": q, "error": f"arXiv collection failed: {type(ex).__name__}: {ex}"})
    return rows


def collect_github():
    token = os.environ.get("GITHUB_TOKEN", "")
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
        headers["X-GitHub-Api-Version"] = "2022-11-28"
    rows = []
    for q in GITHUB_QUERIES:
        params = urllib.parse.urlencode({"q": q + " is:issue", "sort": "updated", "order": "desc", "per_page": 8})
        url = "https://api.github.com/search/issues?" + params
        try:
            data = json.loads(get(url, headers=headers))
            for item in data.get("items", []):
                rows.append({
                    "query": q,
                    "title": item.get("title", ""),
                    "url": item.get("html_url", ""),
                    "state": item.get("state", ""),
                    "updated_at": item.get("updated_at", ""),
                    "repository_url": item.get("repository_url", ""),
                    "body_excerpt": " ".join((item.get("body") or "").split())[:900],
                })
        except Exception as ex:
            rows.append({"query": q, "error": f"GitHub collection failed: {type(ex).__name__}: {ex}"})
    return rows


def dedupe(rows):
    seen = set()
    out = []
    for r in rows:
        key = r.get("url") or (r.get("query"), r.get("error"))
        if key in seen:
            continue
        seen.add(key)
        out.append(r)
    return out

arxiv = dedupe(collect_arxiv())
github = dedupe(collect_github())

ts = NOW.strftime("%Y%m%dT%H%M%SZ")
out = OUTDIR / f"{ts}.md"
lines = [
    f"# Source collection {ts}",
    "",
    "This file is a deterministic discovery queue. It does not contain LLM analysis. The hourly ChatGPT research pass should verify, read deeply, and classify these candidates before treating them as evidence.",
    "",
    "## arXiv candidates",
    "",
]
for r in arxiv:
    if "error" in r:
        lines += [f"- **COLLECTOR ERROR** — {r['query']}: {r['error']}"]
        continue
    authors = ", ".join(r.get("authors", [])[:8])
    lines += [
        f"### {r['title']}",
        f"- Query: `{r['query']}`",
        f"- Published: {r['published']}",
        f"- Authors: {authors}",
        f"- URL: {r['url']}",
        f"- Abstract excerpt: {r['summary'][:1400]}",
        "",
    ]
lines += ["## GitHub issue candidates", ""]
for r in github:
    if "error" in r:
        lines += [f"- **COLLECTOR ERROR** — {r['query']}: {r['error']}"]
        continue
    lines += [
        f"### {r['title']}",
        f"- Query: `{r['query']}`",
        f"- State / updated: {r['state']} / {r['updated_at']}",
        f"- URL: {r['url']}",
        f"- Repository API: {r['repository_url']}",
        f"- Issue excerpt: {r['body_excerpt']}",
        "",
    ]
out.write_text("\n".join(lines), encoding="utf-8")
print(out)
