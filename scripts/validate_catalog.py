#!/usr/bin/env python3
import csv
from pathlib import Path
import sys

CATALOG = Path(__file__).resolve().parents[1] / "catalog" / "top-200-gpos.csv"
REQUIRED = {
    "rank", "id", "cti_score", "cti_priority", "control_type", "category_id",
    "category", "policy_setting", "recommended_state", "rollout_mode",
    "policy_path", "attack_tactics", "threat_scenarios", "applicability", "source_id",
}
PRIORITIES = {"P0", "P1", "P2", "P3"}
FUNCTIONS = {"Prevent", "Detect", "Contain", "Recover"}

def fail(message):
    print(f"[FAIL] {message}")
    sys.exit(1)

def main():
    if not CATALOG.exists():
        fail(f"catalog not found: {CATALOG}")

    with CATALOG.open("r", encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))

    if len(rows) != 200:
        fail(f"expected exactly 200 controls, found {len(rows)}")

    missing = REQUIRED - set(rows[0].keys())
    if missing:
        fail(f"missing columns: {sorted(missing)}")

    ids = [r["id"] for r in rows]
    ranks = [int(r["rank"]) for r in rows]
    scores = [float(r["cti_score"]) for r in rows]

    if len(ids) != len(set(ids)):
        fail("duplicate control IDs")
    if ranks != list(range(1, 201)):
        fail("rank must be contiguous from 1 through 200")
    if ids != [f"GPO-{i:03d}" for i in range(1, 201)]:
        fail("IDs must match rank: GPO-001 ... GPO-200")
    if any(s < 0 or s > 100 for s in scores):
        fail("cti_score must be between 0 and 100")
    if scores != sorted(scores, reverse=True):
        fail("catalog must be sorted by descending cti_score")

    for r in rows:
        if r["cti_priority"] not in PRIORITIES:
            fail(f"{r['id']}: invalid priority")
        if r["control_type"] not in FUNCTIONS:
            fail(f"{r['id']}: invalid control type")
        if not r["policy_setting"].strip() or not r["source_id"].strip():
            fail(f"{r['id']}: required field is empty")

    print(f"[OK] {len(rows)} controls validated")
    print("[OK] ranks, IDs, score order, priorities and required fields are consistent")

if __name__ == "__main__":
    main()
