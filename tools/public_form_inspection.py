"""Inspect public form markup without submitting, reading inboxes or credentials."""
import argparse,datetime,json,re
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request,urlopen

class Forms(HTMLParser):
    def __init__(self):super().__init__();self.forms=[];self.current=None
    def handle_starttag(self,t,attrs):
        a=dict(attrs)
        if t=="form":
            self.current={"id":a.get("id"),"class":a.get("class"),"method":a.get("method"),"action":a.get("action"),"fields":[]};self.forms.append(self.current)
        if t in ("input","textarea","select","button") and self.current is not None:
            # Do not persist nonce/token/default field values; only public layout.
            self.current["fields"].append({k:a.get(k) for k in ("name","id","type","placeholder","required","autocomplete","inputmode","pattern")}|{"element":t})
    def handle_endtag(self,t):
        if t=="form":self.current=None

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--out",required=True);a=ap.parse_args();out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    u="https://evbtms.com/contact/"
    with urlopen(Request(u,headers={"User-Agent":"EVLINK-ReadOnly-ContentReview/1.0"}),timeout=22) as r:s=r.read().decode("utf-8","replace")
    p=Forms();p.feed(s)
    d={"observed_at":datetime.datetime.now(datetime.timezone.utc).isoformat(),"url":u,"forms":p.forms,"boundary":"Public field markup only. No submission performed. Does not verify mobile usability, database save or email delivery."}
    (out/"contact-form-public-fields.json").write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(d,ensure_ascii=False))

if __name__=="__main__":main()
