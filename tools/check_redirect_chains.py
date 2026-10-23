"""Capture public redirect hops for already-observed own-site links."""
import argparse,json,datetime
from pathlib import Path
from urllib.request import Request,build_opener,HTTPRedirectHandler

class Recorder(HTTPRedirectHandler):
    def __init__(self):super().__init__();self.hops=[]
    def redirect_request(self,req,fp,code,msg,headers,newurl):
        self.hops.append({"from":req.full_url,"status":code,"to":newurl})
        return super().redirect_request(req,fp,code,msg,headers,newurl)

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--out",required=True);a=ap.parse_args()
    urls=["https://evbtms.com/products/high-voltage-coolant-heater/q-series-3/","https://evbtms.com/engineering/","https://evbtms.com/applications/electric-mining-truck/","https://evbtms.com/2026/10/22/"]
    results=[]
    for u in urls:
        h=Recorder()
        try:
            with build_opener(h).open(Request(u,headers={"User-Agent":"EVLINK-ReadOnly-ContentReview/1.0"}),timeout=22) as r:
                row={"url":u,"status":r.status,"final":r.url,"hops":h.hops}
        except Exception as e:row={"url":u,"hops":h.hops,"error":str(e)}
        results.append(row)
    p=Path(a.out);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps({"observed_at":datetime.datetime.now(datetime.timezone.utc).isoformat(),"results":results},ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(results,ensure_ascii=False))
if __name__=="__main__":main()
