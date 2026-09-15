import json, os, pathlib, urllib.request, datetime

ROOT = pathlib.Path(__file__).resolve().parents[1]
runs_dir = ROOT / "runs"
files = sorted(runs_dir.glob("*.md"))[-8:]
if not files:
    print("No runs to synthesize.")
    raise SystemExit(0)

runs = "\n\n".join(f"===== {p.name} =====\n{p.read_text(encoding='utf-8')}" for p in files)
old = (ROOT / "MASTER_DIAGNOSIS.md").read_text(encoding="utf-8")

def ask(system, user, max_tokens=6000):
    payload = {
        "model": "openai/gpt-4.1",
        "messages": [{"role":"system","content":system},{"role":"user","content":user}],
        "temperature": 0.15,
        "max_tokens": max_tokens,
    }
    req = urllib.request.Request(
        "https://models.github.ai/inference/chat/completions",
        data=json.dumps(payload).encode(),
        headers={"Authorization":f"Bearer {os.environ['GITHUB_TOKEN']}","Content-Type":"application/json","Accept":"application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.load(r)["choices"][0]["message"]["content"]

system = """You are the synthesis controller for an adversarial investigation of LLM/tool-use failures. Merge only findings supported by the supplied runs. Preserve disagreements and uncertainty. Reject repeated claims that add no evidence. Do not invent internal architecture. Distinguish observed facts, strong inferences, weak hypotheses, falsification tests, and practical controls. The objective is to reduce user babysitting by making prerequisite discovery, authority resolution, tool verification, QA, and correction automatic."""

prompt = f"""PREVIOUS MASTER:\n{old}\n\nRECENT RUNS:\n{runs}\n\nRewrite the master diagnosis as a self-contained research document. Include: (1) strongest supported failure mechanisms ranked by confidence, (2) evidence and counterevidence, (3) rejected or weakened explanations, (4) concrete controller/pipeline changes, (5) unresolved questions and next experiments, and (6) a short 'delta since prior synthesis' section. Avoid generic advice."""

new = ask(system, prompt)
(ROOT / "MASTER_DIAGNOSIS.md").write_text("# Master Diagnosis\n\n" + new + "\n", encoding="utf-8")
print("MASTER_DIAGNOSIS.md updated")
