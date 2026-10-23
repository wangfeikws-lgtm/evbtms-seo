"""Format user-provided T12-W2-04; no body rewriting."""
from pathlib import Path
import re,html,json,hashlib
src=Path('C:/Users/Administrator/.codex/attachments/ddab2a93-a494-4731-bbea-518d89155604/已粘贴的文本.txt')
out=Path(__file__).resolve().parents[1]/'REPORTS/2026-10-23'
lines=[s.strip() for s in src.read_text(encoding='utf-8-sig').strip().splitlines() if s.strip()]
label=lines.pop(0)
heads={
'In terms of price, air heaters have a clear advantage—and the difference is significant.',
'The key to installation lies in whether a ready-made circulation loop is available.',
'The battery is the key factor.',
'From an energy consumption perspective, the two are actually on par with each other.',
'What challenges will the fleet face after installing the heating system?',
'Summary Recommendations',
'Frequently Asked Questions on This Topic'}
faq={
'Is it necessary to install a coolant heater in a small electric van?',
'Does a coolant heater take longer to heat the cab?',
'Should we compare these two solutions with a heat pump system?'}
parts=[]
for line in lines:
    tag='h2' if line in heads else 'h3' if line in faq else 'p'
    parts.append(f'<{tag}>'+html.escape(line)+f'</{tag}>')
body='\n'.join(parts)+'\n'
norm=lambda s:re.sub(r'\s+','',s)
assert norm(html.unescape(re.sub('<[^>]*>','',body)))==norm(''.join(lines))
(out/'T12-W2-04-peter-body.html').write_text(body,encoding='utf-8')
title='Air Heater vs Coolant Heater for EV Cabins: A Total Cost Comparison'
page='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+title+'</title><style>body{max-width:920px;margin:30px auto;padding:20px;font:18px/1.8 system-ui;color:#253746}h1,h2,h3{line-height:1.35}h2{margin-top:38px}p{margin:18px 0}</style><h1>'+title+'</h1>'+body+'</html>'
(out/'T12-W2-04-peter-reading.html').write_text(page,encoding='utf-8')
(out/'T12-W2-04-format-check.json').write_text(json.dumps({'source':str(src),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'body_non_whitespace_matches':True,'removed_internal_label':label,'body_h1_count':0,'ai_detection_this_version':'NOT_TESTED','publication':'NOT_PUBLISHED_BY_CODEX','scope':'Formatting only; not a factual or technical approval.'},ensure_ascii=False,indent=2),encoding='utf-8')
print('Full body formatted; text equality verified; no publication.')
