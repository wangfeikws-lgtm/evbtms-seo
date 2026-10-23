"""Fetch approved-scope public article evidence; produce proposals, never write WP."""
import argparse,difflib,hashlib,json,re,datetime
from pathlib import Path
from urllib.request import Request,urlopen

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--out",required=True);a=ap.parse_args();out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    rows=[]
    for id in (10113,10116,9949,9951,10074):
        u=f"https://evbtms.com/wp-json/wp/v2/posts/{id}?_fields=id,link,title,content,modified,status"
        with urlopen(Request(u,headers={"User-Agent":"EVLINK-ReadOnly-ContentReview/1.0"}),timeout=22) as r:data=json.load(r)
        original=data["content"]["rendered"]
        (out/f"post-{id}-public.json").write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding="utf-8")
        (out/f"post-{id}-rendered-before.html").write_text(original,encoding="utf-8")
        headings=re.findall(r"<h1\b[^>]*>([\s\S]*?)</h1>",original,re.I)
        row={"id":id,"link":data["link"],"title":data["title"]["rendered"],"modified_raw":data["modified"],"body_h1":headings,"sha256_utf8":hashlib.sha256(original.encode()).hexdigest(),"note":"public rendered body, not authenticated raw editor/Elementor source"}
        if id in (10116,9949,9951) and headings:
            tag="p" if id==10116 else "h2"
            proposed=re.sub(r"<(/?)h1\b",rf"<\1{tag}",original,flags=re.I)
            diff="".join(difflib.unified_diff(original.splitlines(True),proposed.splitlines(True),fromfile=f"post-{id}-rendered-before",tofile=f"post-{id}-heading-proposal"))
            (out/f"post-{id}-heading-proposal.diff").write_text(diff,encoding="utf-8")
            row["proposal"]=f"Change body-only h1 tags to {tag} while retaining the theme article H1; review hierarchy and frontend first. Do not paste rendered HTML over Elementor source. 10116 is a paragraph sentence, not a section heading."
        rows.append(row)
    (out/"post-evidence-index.json").write_text(json.dumps({"observed_at":datetime.datetime.now(datetime.timezone.utc).isoformat(),"posts":rows},ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(rows,ensure_ascii=False))

if __name__=="__main__":main()
