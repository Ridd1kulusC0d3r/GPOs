#!/usr/bin/env python3
import json,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
d=json.loads((R/"data/control-index.json").read_text());c=d["controls"]
assert len(c)==200 and [x["id"] for x in c]==[f"GPO-{i:03d}" for i in range(1,201)]
assert len(list((R/"controls").glob("GPO-*.yml")))==200
assert all(x["attack_techniques"] and x["d3fend"] and x["telemetry"]["channels"] for x in c)
assert all("TA0005 Defense Evasion" not in x["attack_tactics"] for x in c)
print("[OK] v2: 200 controls + ATT&CK + D3FEND + telemetry")
