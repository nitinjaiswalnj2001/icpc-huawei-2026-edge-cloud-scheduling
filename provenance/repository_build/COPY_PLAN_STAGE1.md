# Stage 1 Copy Plan

## What to copy now

Copy the **contents of this directory** into a new local repository folder, for example:

```text
ICPC-Huawei-2026-Edge-Cloud-Scheduling/
```

The Stage 1 pack already contains:

- the clean folder structure,
- the exact final resubmitted solver as `final/final_submission.cpp`,
- the frozen final 22-case public result CSV,
- the final Codeforces submission screenshot,
- Stage 0 final-source hashes,
- starter README/index files,
- `.gitignore`.

## What NOT to copy from Stage 0 yet

Do **not** manually copy these into the GitHub repository:

- `raw_exports/`
- the entire `raw_history/`
- old ZIP packs
- temporary binaries
- every threshold/probe variant

Stage 2 will select only the code versions that materially explain the final architecture.

## Suggested Git setup

After copying this skeleton locally:

```bash
git init
git add .
git commit -m "chore: initialize edge-cloud scheduling case study"
```

You may keep the repository private while the documentation is being assembled and until you are comfortable publishing the full solution.
