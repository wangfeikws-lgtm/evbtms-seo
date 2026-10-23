"""Read-only discovery and content matching for user-reported publications."""
import re,json,html,datetime
from pathlib import Path
from urllib.request import urlopen,Request
from urllib.parse import urljoin,urlparse
root=Path(__file__).resolve().parents[1];out=root/'REPORTS/2026-10-23'
def fetch(u):
    with urlopen(Request(u,headers={'User-Agent':'EVLINK-ReadOnly-Verification/1.0'}),timeout=25) as r:return r.geturl(),r.status,r.read().decode('utf-8','replace')
links=set();errors=[]
for u in ['https://www.evptc.com/news.html','https://www.evptc.com/sitemap.xml']:
    try:
        _,_,s=fetch(u)
        links.update(urljoin(u,x) for x in re.findall(r'''href=["']([^"']+)["']''',s))
        links.update(html.unescape(x) for x in re.findall(r'<loc>(.*?)</loc>',s))
    except Exception as e:errors.append({'url':u,'error':str(e)})
keys=['35kw','35-kw','ip67','emc','hydrogen','fuel-cell','total-cost','swapping','air-heater-vs']
candidates=sorted(u for u in links if urlparse(u).hostname in ('www.evptc.com','evptc.com') and '/news/' in u and any(k in u.lower() for k in keys))
rows=[]
for u in candidates[:20]:
    try:
        final,status,s=fetch(u)
        title=re.search(r'<title[^>]*>(.*?)</title>',s,re.S|re.I)
        plain=html.unescape(re.sub('<[^>]+>',' ',s));plain=re.sub(r'\s+',' ',plain)
        matches=[]
        for n in range(1,6):
            files=list(out.glob(f'T12-W2-0{n}-peter*body.html'))
            if not files:continue
            body=files[0].read_text(encoding='utf-8')
            paras=re.findall(r'<p[^>]*>(.*?)</p>',body,re.S)
            clean=lambda x:re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>',' ',x))).strip()
            tests=[clean(x) for x in paras if len(clean(x))>100]
            hit=sum(t in plain for t in tests)
            if hit:matches.append({'task':f'T12-W2-0{n}','matching_long_paragraphs':hit,'tested':len(tests)})
        rows.append({'url':u,'final':final,'status':status,'title':html.unescape(title.group(1)) if title else None,'paragraph_matches':matches})
    except Exception as e:errors.append({'url':u,'error':str(e)})
result={'observed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'discovered_links':len(links),'candidate_count':len(candidates),'pages':rows,'errors':errors,'limits':'Public HTML only. No backend/mobile/form/index verification. HTTP200 alone is not proof of correct article.'}
(out/'old-site-recent-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
