"""Read-only public EVLINK content inventory and bounded link audit.
No authentication, cookies, browser control or production writes.
Generated outputs are evidence snapshots, not live-browser or GSC verification.
"""
import argparse, concurrent.futures, datetime, difflib, hashlib, html, json, re, ssl, time
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse, urldefrag
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import xml.etree.ElementTree as ET

UA = "EVLINK-ReadOnly-ContentReview/1.0"
ALLOWED = {"evbtms.com", "www.evbtms.com", "evptc.com", "www.evptc.com"}

def read(url, limit=5_000_000):
    req=Request(url,headers={"User-Agent":UA,"Accept":"text/html,application/json,application/xml;q=0.9"})
    try:
        with urlopen(req, timeout=22) as r:
            raw=r.read(limit)
            return {"requested":url,"final":r.url,"status":r.status,"content_type":r.headers.get("Content-Type",""),"raw":raw,"error":None}
    except HTTPError as e:
        return {"requested":url,"final":e.url,"status":e.code,"raw":e.read(150000),"content_type":e.headers.get("Content-Type",""),"error":str(e)}
    except Exception as e:
        return {"requested":url,"final":None,"status":None,"raw":b"","content_type":"","error":str(e)}

class Parse(HTMLParser):
    def __init__(self):
        super().__init__();self.links=[];self.canonical=[];self.h1=[];self.title=[];self.description=[];self.robots=[];self.images=[];self.text=[];self.in_title=False;self.in_h1=False;self.skip=0;self.active=None
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag in ("script","style"): self.skip+=1
        if tag=="title":self.in_title=True
        if tag=="h1":self.in_h1=True;self.h1.append("")
        if tag=="a" and a.get("href"):self.active={"href":a["href"],"anchor":""};self.links.append(self.active)
        if tag=="link" and "canonical" in a.get("rel",""):self.canonical.append(a.get("href",""))
        if tag=="meta":
            name=a.get("name","").lower()
            if name=="description":self.description.append(a.get("content",""))
            if name in ("robots","googlebot"):self.robots.append(a.get("content",""))
        if tag=="img":self.images.append({k:a.get(k) for k in ("src","alt","width","height","loading")})
    def handle_endtag(self,tag):
        if tag in ("script","style") and self.skip:self.skip-=1
        if tag=="title":self.in_title=False
        if tag=="h1":self.in_h1=False
        if tag=="a":self.active=None
    def handle_data(self,d):
        if self.in_title:self.title.append(d)
        if self.in_h1 and self.h1:self.h1[-1]+=d
        if self.active:self.active["anchor"]+=d
        if not self.skip:self.text.append(d)

def clean(s):return re.sub(r"\s+"," ",html.unescape(re.sub(r"<[^>]+>"," ",s))).strip()
def normurl(u):return urldefrag(u)[0].rstrip("/")
def parse_result(r):
    raw=r.pop("raw",b"");s=raw.decode("utf-8","replace");r["sha256"]=hashlib.sha256(raw).hexdigest()
    p=Parse()
    try:p.feed(s)
    except Exception as e:r["parse_error"]=str(e)
    r.update(title=clean(" ".join(p.title)),h1=[clean(x) for x in p.h1],description=p.description,canonical=p.canonical,robots=p.robots,images=p.images)
    links=[]
    for x in p.links:
        u=urljoin(r.get("final") or r["requested"],html.unescape(x["href"]))
        if urlparse(u).scheme not in ("http","https"):continue
        links.append({"url":urldefrag(u)[0],"anchor":clean(x["anchor"]),"own_domain":urlparse(u).hostname in ALLOWED})
    r["links"]=links;r["body_text"]=clean(" ".join(p.text))
    return r

def jsonfetch(url,out,name):
    r=read(url)
    (out/(name+".response.json")).write_text(json.dumps({k:v for k,v in r.items() if k!="raw"},ensure_ascii=False,indent=2),encoding="utf-8")
    if r["status"]!=200:return []
    try:data=json.loads(r["raw"])
    except Exception:return []
    if not isinstance(data,list):return []
    (out/(name+".json")).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding="utf-8")
    return data

def old_discovery(out):
    urls=set();logs=[]
    for path in ("/sitemap.xml","/news.html"):
        r=read("https://www.evptc.com"+path);logs.append({k:v for k,v in r.items() if k!="raw"})
        s=r["raw"].decode("utf-8","replace")
        if "xml" in r.get("content_type","") or s.lstrip().startswith("<?xml"):
            try:
                root=ET.fromstring(s)
                locs=[x.text for x in root.iter() if x.tag.endswith("loc") and x.text]
                for u in locs:
                    if "/news/" in u:urls.add(u)
                # Bounded one-level sitemap discovery.
                for u in [u for u in locs if u.endswith(".xml") and urlparse(u).hostname in ALLOWED][:3]:
                    sub=read(u)
                    try:
                        rt=ET.fromstring(sub["raw"])
                        urls.update(x.text for x in rt.iter() if x.tag.endswith("loc") and x.text and "/news/" in x.text)
                    except Exception:pass
            except Exception:pass
        else:
            p=Parse();p.feed(s)
            urls.update(urljoin("https://www.evptc.com",x["href"]) for x in p.links if "/news/" in x["href"])
    (out/"old-discovery.json").write_text(json.dumps({"logs":logs,"urls":sorted(urls)},ensure_ascii=False,indent=2),encoding="utf-8")
    return sorted(urls)

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--out",required=True);ap.add_argument("--check-limit",type=int,default=80);args=ap.parse_args()
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    date=datetime.datetime.now(datetime.timezone.utc).isoformat()
    posts=jsonfetch("https://evbtms.com/wp-json/wp/v2/posts?per_page=100&_fields=id,slug,link,title,date,modified,status",out,"new-posts")
    pages=jsonfetch("https://evbtms.com/wp-json/wp/v2/pages?per_page=100&_fields=id,slug,link,title,date,modified,status",out,"new-pages")
    entries=[{"site":"evbtms","type":typ,"id":x["id"],"url":x["link"],"title":clean(x["title"]["rendered"]),"modified_raw":x.get("modified"),"source":"public_wp_rest"} for typ,rows in (("article",posts),("page",pages)) for x in rows]
    old=old_discovery(out)
    # Explicit published W1 canonical records ensure the important old-site batch is included.
    old+=["https://www.evptc.com/news/"+x for x in [
        "how-to-choose-a-high-voltage-ptc-coolant-heater-7-inputs-oems-must-define-422912.html",
        "can-controlled-vs-thermostat-controlled-hvch-which-architecture-fits-your-vehicle-422917.html",
        "electric-bus-battery-preheating-at-30c-five-planning-mistakes-422919.html",
        "ptc-coolant-heater-vs-heat-pump-for-commercial-evs-where-each-system-wins-422921.html",
        "why-electric-bus-range-falls-in-winter-and-five-levers-fleets-can-control-422923.html"]]
    old=sorted(set(old))
    keyslugs={"battery-thermal-management-system","high-voltage-coolant-heater","three-in-one-controller","electric-mining-truck","applications","contact","high-voltage-coolant-heater-manufacturers"}
    chosen=[x["url"] for x in entries]
    selected=list(dict.fromkeys(chosen+old))
    print("Fetched inventory:",len(posts),"posts,",len(pages),"pages; old discovered",len(old),"; pages queued",len(selected),flush=True)
    cached={}
    if (out/"page-snapshots.json").exists():
        try:
            previous=json.loads((out/"page-snapshots.json").read_text(encoding="utf-8"))
            cached={r["requested"]:r for r in previous["pages"]}
            for r in cached.values():r.setdefault("snapshot_observed_at",previous.get("observed_at"))
        except Exception:pass
    pending=[u for u in selected if u not in cached]
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        fresh=list(pool.map(lambda u:parse_result(read(u)),pending))
    for r in fresh:r["snapshot_observed_at"]=date
    cached.update({r["requested"]:r for r in fresh})
    results=[cached[u] for u in selected]
    for r in results:
        if "evptc.com" in r["requested"]:
            entries.append({"site":"evptc","type":"listing" if r["title"].startswith("News -") else "article","id":None,"url":r["requested"],"title":r["title"],"modified_raw":None,"source":"public_html","status":r["status"],"canonical":r["canonical"]})
    (out/"inventory.json").write_text(json.dumps({"observed_at":date,"entries":entries,"new_post_count":len(posts),"new_page_count":len(pages),"old_discovered":len(old),"old_scope":"sitemap/news listing plus five published W1 records; not a complete backend export"},ensure_ascii=False,indent=2),encoding="utf-8")
    (out/"page-snapshots.json").write_text(json.dumps({"observed_at":date,"pages":results},ensure_ascii=False,indent=2),encoding="utf-8")
    # Cap unique own-site destinations and prefer content-specific destinations over nav repetition.
    counts={};examples={}
    for r in results:
        for x in r["links"]:
            u=normurl(x["url"])
            if not x["own_domain"] or not u:continue
            counts[u]=counts.get(u,0)+1
            examples.setdefault(u,[]).append({"source":r["requested"],"anchor":x["anchor"]})
    existing={normurl(r["requested"]):{"url":r["requested"],"status":r["status"],"final":r["final"],"title":r["title"],"error":r["error"]} for r in results}
    priorchecks={}
    if (out/"link-checks.json").exists():
        try:priorchecks={normurl(r["url"]):r for r in json.loads((out/"link-checks.json").read_text(encoding="utf-8"))["checks"]}
        except Exception:pass
    selectedtargets=[u for u in sorted(counts,key=lambda u:(counts[u],u)) if u not in existing and not any(x in u for x in ("/wp-admin","?","/feed","/author/","/tag/"))][:args.check_limit]
    targets=[u for u in selectedtargets if u not in priorchecks]
    def check(u):
        r=read(u,200000);p=Parse()
        try:p.feed(r["raw"].decode("utf-8","replace"))
        except Exception:pass
        return {"url":u,"status":r["status"],"final":r["final"],"title":clean(" ".join(p.title)),"error":r["error"]}
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        checked=list(pool.map(check,targets))
    checks=list(existing.values())+checked+[priorchecks[u] for u in selectedtargets if u in priorchecks]
    for x in checks:x["incoming_examples"]=examples.get(normurl(x["url"]),[])[:5]
    (out/"link-checks.json").write_text(json.dumps({"observed_at":date,"unique_own_destinations_seen":len(counts),"checked":len(checks),"checks":checks,"note":"GET-based public observations; timeout is unknown, 200 can still be soft404, not browser/mobile/GSC evidence"},ensure_ascii=False,indent=2),encoding="utf-8")
    similar=[]
    articles=[e for e in entries if e["type"]=="article" and e["title"]]
    for i,a in enumerate(articles):
        for c in articles[i+1:]:
            sa=re.sub(r"[^a-z0-9 ]","",a["title"].lower());sc=re.sub(r"[^a-z0-9 ]","",c["title"].lower())
            score=difflib.SequenceMatcher(None,sa,sc).ratio()
            if score>=.58:similar.append({"a":a["url"],"a_title":a["title"],"b":c["url"],"b_title":c["title"],"title_similarity":round(score,3),"status":"candidate_only_requires_intent_review"})
    (out/"title-overlap-candidates.json").write_text(json.dumps(similar,ensure_ascii=False,indent=2),encoding="utf-8")
    lines=["# EVLINK public article inventory","","Observed UTC: "+date,"","Public observations only; published REST records, not drafts or trash. Old-site scope is partial.","","| Site | ID | Title | URL |","|---|---|---|---|"]
    for e in entries:
        if e["type"]=="article":lines.append("| "+e["site"]+" | "+str(e["id"] or "")+" | "+e["title"].replace("|","/")+" | "+e["url"]+" |")
    (out/"article-titles.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    print("DONE",json.dumps({"new_posts":len(posts),"new_pages":len(pages),"old_urls_sampled":len(old),"checked":len(checks),"http_4xx5xx":[x for x in checks if x["status"] and x["status"]>=400],"unknown_count":sum(x["status"] is None for x in checks),"title_overlap_candidates":len(similar)},ensure_ascii=False),flush=True)

if __name__=="__main__":main()
