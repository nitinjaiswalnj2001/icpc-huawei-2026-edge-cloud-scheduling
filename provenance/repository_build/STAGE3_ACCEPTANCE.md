# Stage 3 Acceptance — Experiment Dataset

Stage 3 is complete when all checks below are satisfied.

- [x] Canonical public/historical experiment ledger created.
- [x] Selected archived local diagnostics separated into their own ledger.
- [x] Public/local/historical evidence taxonomy documented.
- [x] Banked score progression reconstructed.
- [x] Per-test public score matrix created across exact reconstructed vectors.
- [x] Case #4 warm/concurrent threshold curve recorded.
- [x] Major target-case breakthroughs summarized.
- [x] Failed and public no-op experiments retained.
- [x] Supporting Stage 0 CSV evidence copied into curated `public_raw/` and `local_raw/` folders.
- [x] Supporting raw files SHA-256 hashed.
- [x] Public-vs-local methodology documented.
- [x] Final 22-case public vector retained unchanged.
- [x] Automated dataset validator added.
- [x] Validator passes all checks.

## Validation snapshot

`python3 experiments/validate_dataset.py`

Expected Stage 3 result:

```text
Stage 3 dataset checks: 111
PASS: 111
FAIL: 0
All dataset consistency checks passed.
```

## Canonical final public score

`16315.7938558663`

The historical ~15595.199 starting baseline remains explicitly approximate because its exact 22-case source/vector was not preserved.
