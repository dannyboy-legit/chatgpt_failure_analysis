# ChatGPT Failure Analysis

Automated evidence-driven investigation into recurring LLM/tool-use failures observed in the Susan wallpaper workflow.

## Research cadence

- Worker runs: `:07, :22, :37, :52` UTC each hour.
- Each run performs four independent passes: evidence extraction, root-cause analysis, adversarial critique, and corrective-method design.
- Runs are append-only under `runs/` and maintain a rolling `MASTER_DIAGNOSIS.md`.
- The workflow stops creating new analysis after **2026-09-15T22:23:00Z** unless the stop time is edited.

## Investigation requirements

The pipeline distinguishes observed behavior from speculation. It must not excuse a failure by inventing inaccessible-context or technical-limit claims without evidence. It should test competing explanations and focus on concrete mechanisms that would have prevented the failure.

The initial case file is in `case/FAILURE_RECORD.md`.
