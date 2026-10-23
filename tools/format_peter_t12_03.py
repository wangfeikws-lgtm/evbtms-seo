"""Format Peter's supplied article, without rewriting its body."""
from pathlib import Path
import html,re,json,hashlib
src=Path('C:/Users/Administrator/.codex/attachments/1d8b7211-a0d5-42d3-ac95-1d432437d05c/已粘贴的文本.txt')
out=Path(__file__).resolve().parents[1]/'REPORTS/2026-10-23'
raw=src.read_text(encoding='utf-8-sig').strip()
lines=[line.strip() for line in raw.splitlines() if line.strip()]
label=lines.pop(0)
h2={
'During a cold start, the fuel cell itself acts as a “heat load.”',
'Constant-speed driving is merely the easiest part of operations',
'Coolant Systems Are Often Overlooked Until Late in the Project',
'Total Load Shortfall as High as 20 kW',
'Our Configuration Recommendations',
'Frequently Asked Questions on This Topic'}
h3={
'Can the fuel cell stack independently heat the passenger compartment when weather conditions are favorable?',
'Why not simply install a diesel parking heater to solve the problem?',
'All right. But wouldn’t a 20-kilowatt heater significantly reduce the driving range?'}
parts=[]
for line in lines:
    tag='h2' if line in h2 else 'h3' if line in h3 else 'p'
    parts.append(f'<{tag}>'+html.escape(line)+f'</{tag}>')
body='\n'.join(parts)+'\n'
norm=lambda text:re.sub(r'\s+','',text)
assert norm(html.unescape(re.sub('<[^>]*>','',body)))==norm(''.join(lines))
(out/'T12-W2-03-peter-body.html').write_text(body,encoding='utf-8')
title='Hydrogen Fuel Cell Bus Heating: 20 kW-Class Coolant Heater Selection'
page='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+title+'</title><style>body{max-width:920px;margin:30px auto;padding:20px;font:18px/1.8 system-ui;color:#253746}h1,h2,h3{line-height:1.35}h2{margin-top:38px}p{margin:18px 0}</style><h1>'+title+'</h1>'+body+'</html>'
(out/'T12-W2-03-peter-reading.html').write_text(page,encoding='utf-8')
(out/'T12-W2-03-format-check.json').write_text(json.dumps({'source':str(src),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'body_non_whitespace_matches':True,'removed_internal_label':label,'body_h1_count':0,'ai_detection_this_version':'NOT_TESTED','publication':'NOT_PUBLISHED_BY_CODEX','fact_review':'Formatting does not verify technical claims or model applicability.'},ensure_ascii=False,indent=2),encoding='utf-8')
print('Complete body retained; formatting equality verified; no publication.')
