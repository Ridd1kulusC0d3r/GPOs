#!/usr/bin/env python3
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1];D=json.loads((R/"data/control-index.json").read_text());O=R/"generated-controls";O.mkdir(exist_ok=True)
for c in D["controls"]:(O/f'{c["id"]}.yml').write_text(json.dumps(c,indent=2)+"\n")
print("generated",len(D["controls"]))
