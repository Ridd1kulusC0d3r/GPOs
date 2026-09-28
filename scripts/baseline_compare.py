#!/usr/bin/env python3
import argparse,csv,html,json,re,sys
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]

def catalog():
    return json.loads((ROOT/"data/control-index.json").read_text(encoding="utf-8"))["controls"]

def flatten_json(obj):
    if isinstance(obj,dict): return " ".join(str(k)+" "+flatten_json(v) for k,v in obj.items())
    if isinstance(obj,list): return " ".join(flatten_json(v) for v in obj)
    return str(obj)

def read_observed(path):
    p=Path(path); suf=p.suffix.lower()
    if suf==".csv":
        with p.open(encoding="utf-8-sig",errors="ignore",newline="") as f:
            rows=list(csv.DictReader(f))
        by_id={}
        for r in rows:
            cid=(r.get("id") or r.get("ID") or r.get("control_id") or "").strip()
            state=(r.get("current_state") or r.get("state") or r.get("value") or r.get("setting_value") or "").strip()
            if cid: by_id[cid]=state
        text=" ".join(" ".join(str(v) for v in r.values()) for r in rows).lower()
        return text,by_id,"csv"
    raw=p.read_text(encoding="utf-8",errors="ignore")
    if suf==".json":
        try: raw=flatten_json(json.loads(raw))
        except json.JSONDecodeError: pass
    elif suf in {".xml",".policyrules"}:
        try:
            root=ET.fromstring(raw)
            raw=" ".join((e.tag+" "+(e.text or "")+" "+" ".join(e.attrib.values())) for e in root.iter())
        except ET.ParseError: pass
    elif suf in {".html",".htm"}:
        raw=html.unescape(re.sub(r"<[^>]+>"," ",raw))
    return raw.lower(),{},suf.lstrip(".") or "text"

def norm(s): return re.sub(r"\s+"," ",str(s).strip().lower())

def present(name,text):
    n=norm(name)
    if n in text:return True
    toks=[t for t in re.split(r"[^a-z0-9]+",n) if len(t)>4]
    return bool(toks) and sum(t in text for t in toks)>=max(2,(len(toks)*2+2)//3)

def compare(path):
    text,by_id,mode=read_observed(path);out=[]
    for c in catalog():
        if c["id"] in by_id:
            cur=by_id[c["id"]]
            status="match" if norm(cur)==norm(c["recommended_state"]) else "different"
            evidence=cur
        else:
            status="observed" if present(c["policy_setting"],text) else "not_observed"
            evidence=""
        out.append({"id":c["id"],"priority":c["cti_priority"],"policy":c["policy_setting"],"recommended":c["recommended_state"],"status":status,"observed":evidence})
    return mode,out

def self_test():
    cs=catalog()
    sample=(cs[0]["policy_setting"]+"\n"+cs[1]["policy_setting"]).lower()
    assert present(cs[0]["policy_setting"],sample)
    assert not present(cs[-1]["policy_setting"],sample)
    print("[OK] baseline comparator self-test")

def main():
    p=argparse.ArgumentParser(description="Compare the Top 200 against exported GPO/baseline evidence.")
    p.add_argument("--observed");p.add_argument("--format",choices=["json","csv"],default="json");p.add_argument("--output");p.add_argument("--self-test",action="store_true")
    a=p.parse_args()
    if a.self_test:return self_test()
    if not a.observed:p.error("--observed is required unless --self-test is used")
    mode,rows=compare(a.observed)
    summary={s:sum(r["status"]==s for r in rows) for s in ["match","different","observed","not_observed"]}
    if a.format=="json":
        body=json.dumps({"input_mode":mode,"summary":summary,"results":rows,"warning":"Heuristic presence does not prove an exact GPO value unless an ID/current_state CSV is supplied."},indent=2)
    else:
        import io
        b=io.StringIO();w=csv.DictWriter(b,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows);body=b.getvalue()
    if a.output:Path(a.output).write_text(body+"\n",encoding="utf-8")
    else:print(body)
if __name__=="__main__":main()
