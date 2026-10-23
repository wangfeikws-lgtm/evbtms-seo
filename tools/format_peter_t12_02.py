"""Format user text without rewriting, retaining exact non-whitespace text."""
from pathlib import Path
import html,re,hashlib,json
src=Path('C:/Users/Administrator/.codex/attachments/344f5ef4-c701-4fe4-be29-babcbe8846d4/已粘贴的文本.txt')
out=Path(__file__).resolve().parents[1]/'REPORTS/2026-10-23'
raw=src.read_text(encoding='utf-8-sig').strip()
lines=[x.strip() for x in raw.splitlines() if x.strip()]
label=lines.pop(0)
headings={
'What exactly does the IP67 test cover?',
'Limitations of Protection Ratings: High-Pressure Washing, Accidental Conditions, and Unconnected Interfaces',
'The impact of electromagnetic compatibility (EMC) is bidirectional, and laboratory test environments differ significantly from actual vehicle environments.',
'A Key Metric to Compare','Five Questions and Their Implications','Frequently Asked Questions on This Topic'}
faq={'Is an IP67 rating sufficient for underbody installation?',
'Can a heater interfere with the vehicle’s network even while passing EMC (electromagnetic compatibility) testing?'}
questions={
'Is this test report specific to the current configuration (including connectors), or is it a generic report applicable to other models in the same series?',
'Under what connection conditions were the IP rating tests conducted? What prerequisites apply to the wiring harness side for this rating?',
'Were the tests conducted using mass-produced wiring harnesses in a full-vehicle environment under full-power operating conditions? Were CAN bus error frames recorded during testing?',
'Regarding the insulation resistance specification: What are the specific values? Were they verified for each individual unit, or were they derived solely from sampling tests?',
'If water ingress is suspected during use, what information or materials does the warranty process require us to provide?'}
parts=[];in_list=False
for line in lines:
    if line in questions:
        if not in_list:parts.append('<ol>');in_list=True
        parts.append('<li>'+html.escape(line)+'</li>');continue
    if in_list:parts.append('</ol>');in_list=False
    tag='h2' if line in headings else 'h3' if line in faq else 'p'
    q='Does the IP67 rating cover requirements related to coolant leaks?'
    if line.startswith(q):
        parts.append('<h3>'+q+'</h3>');parts.append('<p>'+html.escape(line[len(q):].strip())+'</p>')
    else:parts.append(f'<{tag}>'+html.escape(line)+f'</{tag}>')
if in_list:parts.append('</ol>')
body='\n'.join(parts)+'\n'
norm=lambda s:re.sub(r'\s+','',s)
assert norm(html.unescape(re.sub('<[^>]*>','',body)))==norm(''.join(lines))
(out/'T12-W2-02-peter-approved-body.html').write_text(body,encoding='utf-8')
title='IP67 and EMC in High-Voltage Heaters: What to Check Before Installation'
page='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+title+'</title><style>body{max-width:920px;margin:30px auto;padding:20px;font:18px/1.8 system-ui;color:#253746}h1,h2,h3{line-height:1.35}h2{margin-top:38px}li{margin:12px 0}</style><h1>'+title+'</h1>'+body+'</html>'
(out/'T12-W2-02-peter-reading.html').write_text(page,encoding='utf-8')
(out/'T12-W2-02-format-check.json').write_text(json.dumps({'source':str(src),'format_only':True,'non_whitespace_content_matches':True,'source_heading_removed_from_body':label,'body_h1_count':0,'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'ai_detection_this_version':'NOT_TESTED','publication':'NOT_PUBLISHED_BY_CODEX'},ensure_ascii=False,indent=2),encoding='utf-8')
print('Formatted; non-whitespace text equality verified; no publication.')
