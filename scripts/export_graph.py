#!/usr/bin/env python3
import argparse,json,uuid
from pathlib import Path
R=Path(__file__).resolve().parents[1];D=json.loads((R/"data/control-index.json").read_text());NS=uuid.UUID("1ed0ab65-12a6-4fbd-92a4-878b30ee3180")
def u(k):return str(uuid.uuid5(NS,k))
def graph():
 n={};e=[]
 for c in D["controls"]:
  n[c["id"]]={"id":c["id"],"type":"gpo","label":c["policy_setting"]}
  for t in c["attack_techniques"]:n[t["id"]]={"id":t["id"],"type":"attack","label":t["name"]};e.append({"source":c["id"],"target":t["id"],"relationship":"reduces"})
 return {"nodes":list(n.values()),"edges":e}
def stix():
 o=[]
 for c in D["controls"]:
  cid="x-gpo-control--"+u("gpo:"+c["id"]);o.append({"type":"x-gpo-control","spec_version":"2.1","id":cid,"created":"2026-09-27T00:00:00.000Z","modified":"2026-09-27T00:00:00.000Z","name":c["policy_setting"],"x_gpo_id":c["id"]})
 return {"type":"bundle","id":"bundle--"+u("bundle:gpo-v2"),"objects":o}
p=argparse.ArgumentParser();p.add_argument("--format",choices=["graph","stix"],default="graph");p.add_argument("--check",action="store_true");a=p.parse_args();z=graph() if a.format=="graph" else stix()
if a.check:print("OK",a.format,len(z.get("nodes",z.get("objects",[]))))
else:
 out=R/"exports"/("graph.json" if a.format=="graph" else "gpo-controls.stix.json");out.parent.mkdir(exist_ok=True);out.write_text(json.dumps(z,indent=2));print(out)
