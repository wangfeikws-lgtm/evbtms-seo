"""Use stored evidence to build reviewable replacements, not automatic redirects."""
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
source=root/'REPORTS/three-hour-2026-10-22/public-audit'
pages=json.loads((source/'page-snapshots.json').read_text(encoding='utf-8'))['pages']
mapping={'https://evbtms.com/engineering/':'https://evbtms.com/engineering-services/',
'https://evbtms.com/applications/electric-mining-truck/':'https://evbtms.com/electric-mining-truck/'}
rows=[]
seen=set()
for p in pages:
    for link in p.get('links',[]):
        u=link.get('url','')
        key=(p['requested'],u,link.get('anchor',''))
        if u in mapping and key not in seen:
            seen.add(key);rows.append({'page':p['requested'],'old':u,'new':mapping[u],'anchor':link.get('anchor',''),'state':'PROPOSED_NOT_CHANGED','evidence_time':p.get('snapshot_observed_at')})
out=root/'REPORTS/2026-10-23';out.mkdir(exist_ok=True)
(out/'internal-link-worklist.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
lines=['# P0LINK-14：已知证据对应的内链候选清单','',
'来源为10月22日公开快照，不是今天后台已修复记录。正式14条源清单尚未入仓，以下仅列证据中可定位的旧地址，不凑够14条。',
'只建议改href，不改锚文本、URL、301或canonical。Q3→Q2涉及型号对应，排除自动替换。实施前检查原编辑结构及最新状态，改后检查真实正文/目标页，不能只看HTTP200。','',
'| 源页面 | 锚文本 | 原href | 建议href |','|---|---|---|---|']
for r in rows:lines.append('| '+' | '.join(str(r[k]).replace('|','/') for k in ('page','anchor','old','new'))+' |')
(out/'internal-link-worklist.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print({'unique_source_link_anchor_candidates':len(rows),'source_pages':len(set(r['page'] for r in rows)),'production_changes':0})
