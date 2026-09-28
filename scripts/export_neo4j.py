#!/usr/bin/env python3
import argparse,csv,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(n):return json.loads((ROOT/"data"/n).read_text(encoding="utf-8"))
def build():
    d=load("control-index.json")["controls"];profiles=load("profiles.json")["profiles"];packs=load("threat-packs.json")["packs"];actors=load("actor-overlays.json")["actors"]
    nodes={};rels=[]
    def node(i,label,typ,**props):nodes[i]={"id":i,"label":label,"type":typ,**props}
    for c in d:
        node(c["id"],c["policy_setting"],"GPO",priority=c["cti_priority"],score=c["cti_score"],category=c["category"])
        for t in c["attack_techniques"]:
            node(t["id"],t["name"],"ATTACK");rels.append((c["id"],"REDUCES",t["id"]))
        for x in c["d3fend"]:
            node(x["id"],x["name"],"D3FEND");rels.append((c["id"],"ALIGNS_WITH",x["id"]))
        for e in c["telemetry"]["event_ids"]:
            eid="EVENT-"+e;node(eid,e,"EVENT");rels.append((c["id"],"OBSERVED_BY",eid))
    for pid,p in profiles.items():
        nid="PROFILE-"+pid;node(nid,p["name"],"PROFILE")
        rels += [(nid,"INCLUDES",x) for x in p["controls"]]
    for pid,p in packs.items():
        nid="PACK-"+pid;node(nid,p["name"],"THREAT_PACK")
        rels += [(nid,"PRIORITIZES",x) for x in p["controls"]]
    for aid,a in actors.items():
        nid="ACTOR-"+aid;node(nid,a["name"],"ACTOR_OVERLAY",attack_id=a["attack_group_id"])
        rels += [(nid,"PRIORITIZES",x) for x in a["controls"]]
    return list(nodes.values()),rels
def main():
    p=argparse.ArgumentParser();p.add_argument("--output",default="exports/neo4j");p.add_argument("--check",action="store_true");a=p.parse_args();nodes,rels=build()
    if a.check:print(f"[OK] neo4j export: {len(nodes)} nodes / {len(rels)} relationships");return
    out=ROOT/a.output;out.mkdir(parents=True,exist_ok=True)
    with (out/"nodes.csv").open("w",newline="",encoding="utf-8") as f:
        fields=["id","label","type","priority","score","category","attack_id"];w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows({k:n.get(k,"") for k in fields} for n in nodes)
    with (out/"relationships.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.writer(f);w.writerow(["source","relationship","target"]);w.writerows(rels)
    print(out)
if __name__=="__main__":main()
