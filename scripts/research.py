import json, os, pathlib, urllib.request, datetime

ROOT = pathlib.Path(__file__).resolve().parents[1]
STOP = datetime.datetime.fromisoformat("2026-09-15T22:23:00+00:00")
NOW = datetime.datetime.now(datetime.timezone.utc)
if NOW >= STOP:
    print("Stop time reached; no new worker output.")
    raise SystemExit(0)

case = (ROOT / "case/FAILURE_RECORD.md").read_text(encoding="utf-8")
master = (ROOT / "MASTER_DIAGNOSIS.md").read_text(encoding="utf-8")

def ask(system, user, max_tokens=4500):
    token = os.environ["GITHUB_TOKEN"]
    payload = {
        "model": "openai/gpt-4.1",
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "temperature": 0.2,
        "max_tokens": max_tokens,
    }
    req = urllib.request.Request(
        "https://models.github.ai/inference/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=180) as r:
        data = json.load(r)
    return data["choices"][0]["message"]["content"]

base_system = """You are an adversarial research analyst investigating failures in an LLM agent workflow. Do not defend the system, do not invent inaccessible internal architecture, and do not treat speculation as fact. Separate direct observations, plausible mechanisms, competing explanations, and actionable controls. Focus on mechanisms that would have prevented the user from having to babysit the process. Prefer concrete gates, state checks, and falsifiable tests over vague advice. Where public research concepts are relevant, name them accurately (for example instruction hierarchy failures, tool-use planning errors, context neglect, retry loops, evaluator/controller separation), but do not fabricate citations."""

p1 = ask(base_system, f"""CASE FILE:\n{case}\n\nCURRENT MASTER:\n{master}\n\nPASS 1 — EVIDENCE EXTRACTION. Build a rigorous evidence table from the case. For each failure, identify: observed behavior, information available beforehand, decision that should have been made, and the earliest preventable point. Identify repeated patterns across failures. Do not yet propose a final root cause.""")

p2 = ask(base_system, f"""CASE FILE:\n{case}\n\nPASS 1:\n{p1}\n\nPASS 2 — ROOT-CAUSE HYPOTHESES. Produce 5-10 competing mechanistic hypotheses that could explain the observed execution gap. Rank them by explanatory power. For each: supporting evidence, contradicting evidence, a falsification test, and whether the mechanism is likely local to this workflow or general to tool-using LLM agents.""")

p3 = ask(base_system, f"""CASE FILE:\n{case}\n\nPASS 1:\n{p1}\n\nPASS 2:\n{p2}\n\nPASS 3 — ADVERSARIAL CRITIQUE. Attack the leading hypotheses. Look for excuses masquerading as explanations, post-hoc rationalization, unsupported capability claims, and controls that merely restate the user's instructions. Identify what would still fail even if every written rule were present. State which hypotheses survive and why.""")

p4 = ask(base_system, f"""CASE FILE:\n{case}\n\nPASS 1:\n{p1}\n\nPASS 2:\n{p2}\n\nPASS 3:\n{p3}\n\nPASS 4 — CORRECTIVE PIPELINE. Design a practical controller for future image/tool workflows. It must include prerequisite discovery, source-authority resolution, tool-path verification, acceptance tests, QA, retry termination, and evidence-based capability statements. Give exact gates and failure conditions, not generic advice. Finish with 3-7 highest-value changes ranked by expected impact.""")

ts = NOW.strftime("%Y%m%dT%H%M%SZ")
outdir = ROOT / "runs"
outdir.mkdir(exist_ok=True)
out = outdir / f"{ts}.md"
out.write_text(f"# Research run {ts}\n\n## Pass 1 — Evidence\n\n{p1}\n\n## Pass 2 — Hypotheses\n\n{p2}\n\n## Pass 3 — Adversarial critique\n\n{p3}\n\n## Pass 4 — Corrective pipeline\n\n{p4}\n", encoding="utf-8")
print(out)
