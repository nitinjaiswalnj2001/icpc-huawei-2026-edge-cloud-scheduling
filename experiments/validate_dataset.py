#!/usr/bin/env python3
"""Validate the curated experiment dataset using only Python's standard library."""

from pathlib import Path
import csv
import math
import sys

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
TOL = 2e-8

checks = []

def ok(name, condition, detail=""):
    checks.append((name, bool(condition), detail))

def rows(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

# 1) Final public vector sums exactly to preserved TOTAL within floating tolerance.
final_rows = rows(DATA / "final_public_22_cases.csv")
case_rows = [r for r in final_rows if r["case"] != "TOTAL"]
total_row = next(r for r in final_rows if r["case"] == "TOTAL")
calc_final = sum(float(r["points_exact"]) for r in case_rows)
decl_final = float(total_row["points_exact"])
ok("final vector total", abs(calc_final - decl_final) <= TOL,
   f"calculated={calc_final:.13f}, declared={decl_final:.13f}")

# 2) Matrix columns reproduce their tidy TOTAL rows.
matrix = rows(DATA / "public_score_matrix.csv")
columns = [c for c in matrix[0].keys() if c != "case"]
tidy = rows(DATA / "public_vectors_tidy.csv")
tidy_total = {r["milestone"]: float(r["points"]) for r in tidy if r["case"] == "TOTAL"}
for c in columns:
    s = sum(float(r[c]) for r in matrix)
    ok(f"matrix total {c}", c in tidy_total and abs(s - tidy_total[c]) <= TOL,
       f"matrix={s:.13f}, tidy={tidy_total.get(c, float('nan')):.13f}")

# 3) Canonical score progression exact rows correspond to matrix totals when vector exists.
progress = rows(DATA / "score_progression.csv")
for r in progress:
    if r["confidence"] != "exact_public":
        continue
    k = r["key"]
    if k not in tidy_total:
        ok(f"progression vector {k}", False, "missing matrix/tidy vector")
    else:
        p = float(r["total_score"])
        ok(f"progression total {k}", abs(p - tidy_total[k]) <= TOL,
           f"progression={p:.13f}, vector={tidy_total[k]:.13f}")

# 4) final65 matrix column matches the frozen final file case-by-case.
final_by_case = {int(r["case"]): float(r["points_exact"]) for r in case_rows}
matrix_by_case = {int(r["case"]): r for r in matrix}
for c in range(1, 23):
    ok(f"final65 case {c}", abs(float(matrix_by_case[c]["final65"]) - final_by_case[c]) <= TOL)

# 5) Protected #20 canary remains exact across the reconstructed public matrix.
CANARY = 998.0785092863
row20 = matrix_by_case[20]
for c in columns:
    ok(f"#20 canary {c}", abs(float(row20[c]) - CANARY) <= TOL,
       f"value={float(row20[c]):.13f}")

# 6) Public exact ledger deltas recompute where both numbers exist.
ledger = rows(DATA / "experiment_ledger.csv")
for r in ledger:
    if r["evidence"] != "public_exact":
        continue
    if not r["control_points"] or not r["variant_points"] or not r["delta_points"]:
        continue
    a, b, d = map(float, (r["control_points"], r["variant_points"], r["delta_points"]))
    ok(f"ledger delta {r['id']}", abs((b-a)-d) <= TOL)

# 7) Final case4 threshold is the best score in the recorded public threshold curve.
curve = rows(DATA / "case4_threshold_curve.csv")
best = max(curve, key=lambda r: float(r["case4_points"]))
ok("case4 best threshold", best["mode"] == "concurrent" and float(best["threshold_percent"]) == 65.0,
   f"best={best['mode']} {best['threshold_percent']}%, score={best['case4_points']}")

failed = [x for x in checks if not x[1]]
print(f"Stage 3 dataset checks: {len(checks)}")
print(f"PASS: {len(checks)-len(failed)}")
print(f"FAIL: {len(failed)}")
for name, passed, detail in checks:
    if not passed:
        print(f"FAIL | {name} | {detail}")

if failed:
    sys.exit(1)
print("All dataset consistency checks passed.")
