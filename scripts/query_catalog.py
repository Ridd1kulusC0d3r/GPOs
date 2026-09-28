#!/usr/bin/env python3
import argparse
import csv
from pathlib import Path

CATALOG = Path(__file__).resolve().parents[1] / "catalog" / "top-200-gpos.csv"

def main():
    p = argparse.ArgumentParser(description="Query the threat-informed GPO catalog")
    p.add_argument("--priority", choices=["P0", "P1", "P2", "P3"])
    p.add_argument("--tactic")
    p.add_argument("--search")
    p.add_argument("--rollout")
    p.add_argument("--limit", type=int, default=50)
    args = p.parse_args()

    with CATALOG.open("r", encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))

    def match(row):
        if args.priority and row["cti_priority"] != args.priority:
            return False
        if args.tactic and args.tactic.lower() not in row["attack_tactics"].lower():
            return False
        if args.rollout and args.rollout.lower() not in row["rollout_mode"].lower():
            return False
        if args.search:
            haystack = " ".join([
                row["policy_setting"], row["category"], row["threat_scenarios"],
                row["policy_path"], row["recommended_state"],
            ]).lower()
            if args.search.lower() not in haystack:
                return False
        return True

    found = [r for r in rows if match(r)][:max(args.limit, 0)]
    if not found:
        print("No matching controls.")
        return

    for r in found:
        print(
            f"{r['rank']:>3} {r['id']} {r['cti_priority']} "
            f"{float(r['cti_score']):>5.2f}  {r['policy_setting']} "
            f"[{r['rollout_mode']}]"
        )

if __name__ == "__main__":
    main()
