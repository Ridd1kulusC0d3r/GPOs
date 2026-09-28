#!/usr/bin/env python3
import argparse,json,math,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(n): return json.loads((ROOT/"data"/n).read_text(encoding="utf-8"))
def controls(): return load("control-index.json")["controls"]
def show(rs,n=50):
 for c in rs[:n]: print(f'{c["id"]} {c["cti_priority"]} {float(c["cti_score"]):6.2f}  {c["policy_setting"]}')
 print(f"\n{len(rs)} control(s)")
def main():
 p=argparse.ArgumentParser(prog="gpoctl");s=p.add_subparsers(dest="cmd",required=True)
 x=s.add_parser("search");x.add_argument("query",nargs="?");x.add_argument("--priority");x.add_argument("--technique");x.add_argument("--limit",type=int,default=50)
 x=s.add_parser("pack");x.add_argument("name");x.add_argument("--priority");x.add_argument("--limit",type=int,default=200)
 x=s.add_parser("profile");x.add_argument("name");x.add_argument("--limit",type=int,default=200)
 x=s.add_parser("path");x.add_argument("name")
 x=s.add_parser("score");x.add_argument("id");x.add_argument("--asset-criticality",type=int,default=80);x.add_argument("--detection-gap",type=int,default=50)
 x=s.add_parser("drift");x.add_argument("--input",required=True)
 a=p.parse_args();cs=controls()
 if a.cmd=="search":
  rs=cs
  if a.priority: rs=[c for c in rs if c["cti_priority"]==a.priority]
  if a.technique: rs=[c for c in rs if any(a.technique.lower() in (t["id"]+" "+t["name"]).lower() for t in c["attack_techniques"])]
  if a.query: rs=[c for c in rs if a.query.lower() in json.dumps(c).lower()]
  show(rs,a.limit)
 elif a.cmd=="pack":
  z=load("threat-packs.json")["packs"][a.name];ids=set(z["controls"]);rs=[c for c in cs if c["id"] in ids and (not a.priority or c["cti_priority"]==a.priority)];print("# "+z["name"]);show(rs,a.limit)
 elif a.cmd=="profile":
  z=load("profiles.json")["profiles"][a.name];ids=set(z["controls"]);print("# "+z["name"]);show([c for c in cs if c["id"] in ids],a.limit)
 elif a.cmd=="path":
  z=load("attack-paths.json")["paths"][a.name];print("# "+z["title"]);[print(f'→ {n["type"]}: {n["id"]} — {n["label"]}') for n in z["nodes"]]
 elif a.cmd=="score":
  c=next(c for c in cs if c["id"]==a.id);r=c["risk_components"];v=max(0,min(100,15+.35*r["threat_prevalence"]+.25*r["blast_radius"]+.20*a.asset_criticality+.10*a.detection_gap+.10*r["validation_confidence"]-.15*r["deployment_friction"]));print(json.dumps({"id":c["id"],"environment_score":round(v,2),"priority":"P0" if v>=95 else "P1" if v>=89 else "P2" if v>=83 else "P3"},indent=2))
 else:
  raw=Path(a.input).read_text(encoding="utf-8",errors="ignore").lower();present=[];missing=[]
  for c in cs:
   toks=[t for t in re.split(r"[^a-z0-9]+",c["policy_setting"].lower()) if len(t)>4];hit=c["policy_setting"].lower() in raw or (toks and sum(t in raw for t in toks)>=max(2,math.ceil(len(toks)*.7)));(present if hit else missing).append(c["id"])
  print(json.dumps({"mode":"heuristic-presence","present":present,"not_observed":missing,"warning":"Presence does not prove the configured value matches the recommendation."},indent=2))
if __name__=="__main__": main()
