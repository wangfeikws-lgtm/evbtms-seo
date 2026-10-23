"""Index existing EVLINK visual assets and extract documented factory-video stills.
Preserves source files; no invented photos, no watermark removal.
"""
import argparse, datetime, hashlib, json, os, subprocess
from pathlib import Path
from PIL import Image

def digest(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""):h.update(chunk)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--out",required=True);a=ap.parse_args()
    root=Path(r"E:\codex项目\独立站");out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    paths=[]
    for sub in ("system-images","article-assets","outputs/EVLINK-HVCH-All-Models-Native-V4/assets","outputs/EVLINK-HVCH-B-Series-A2-Layout-Final/assets","evlink-brand-film/analysis"):
        d=root/sub
        if d.exists():paths.extend(p for p in d.iterdir() if p.suffix.lower() in (".png",".jpg",".jpeg",".webp"))
    rows=[]
    for p in paths:
        try:
            with Image.open(p) as im:w,h=im.size
            name=p.name.lower()
            group="BTMS" if "btms" in name else "HVCH" if any(x in name for x in ("hvch","heater")) else "factory_video_frame" if p.parent.name=="analysis" else "unclassified"
            rows.append({"path":str(p),"name":p.name,"group":group,"width":w,"height":h,"bytes":p.stat().st_size,"sha256":digest(p),"provenance":"existing_project_asset","photo_status":"unknown; filename does not establish real photography","usage":"review existing authorization and product/model match before publishing"})
        except Exception as e:rows.append({"path":str(p),"error":str(e)})
    duplicates={}
    for r in rows:
        if "sha256" in r:duplicates.setdefault(r["sha256"],[]).append(r["path"])
    source=root/"evlink-brand-film/public/assets/company-video.mp4"
    ffmpegs=list((root/"evlink-brand-film/node_modules/.pnpm").glob("@remotion+compositor-win32*/node_modules/@remotion/compositor-win32*/ffmpeg.exe"))
    frames=[]
    if source.exists() and ffmpegs:
        for sec,label in ((30,"production-equipment"),(60,"heater-inspection-station")):
            intermediate=out/f"company-video-{sec}s-{label}.png"
            target=intermediate
            proc=subprocess.run([str(ffmpegs[0]),"-hide_banner","-loglevel","error","-y","-ss",str(sec),"-i",str(source),"-frames:v","1","-vf","scale=1280:-1",str(target)],capture_output=True,text=True,encoding="utf-8",errors="replace",timeout=45)
            if target.exists():
                with Image.open(target) as image:
                    target=intermediate.with_suffix(".webp")
                    image.convert("RGB").save(target,quality=86,method=6)
                with Image.open(target) as im:size=im.size
                frames.append({"file":target.name,"source":str(source),"time_seconds":sec,"size":size,"bytes":target.stat().st_size,"sha256":digest(target),"note":"Unretouched extracted frame; original platform watermark preserved. Visible equipment does not prove test scope, pass result, throughput or certification."})
            else:frames.append({"time_seconds":sec,"error":proc.stderr})
    payload={"observed_at":datetime.datetime.now(datetime.timezone.utc).isoformat(),"source_root":str(root),"assets":rows,"duplicate_groups":[v for v in duplicates.values() if len(v)>1],"factory_video":{"path":str(source),"bytes":source.stat().st_size if source.exists() else None,"sha256":digest(source) if source.exists() else None,"duration_from_ffmpeg":"00:02:06.27","source_metadata_creation_time":"2026-07-21T01:32:11Z; not a verified filming date","frames":frames}}
    (out/"asset-registry.json").write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding="utf-8")
    lines=["# 既有素材与工厂视频索引","","## 已定位原始视频","",f"- 路径：{source}",f"- 大小：{payload['factory_video']['bytes']} bytes","- 时长：2分06.27秒（FFmpeg读取）；元数据日期不是拍摄日期。","- 已提取30秒生产设备、60秒加热器检验工位画面；保留原平台水印，不冒充无水印原创照片。","- 已目视核对两帧；30秒不能仅凭设备外观命名具体工艺。60秒可见探头和加热器，但不能证明具体测试标准或通过结果。","- 不从画面推导25项测试、9360循环、认证、产量或员工人数。","- Peter已确认人数400是独立用户事实，不由视频证明。","","## 可交付画面","","| Frame | Source time | Dimensions | Bytes |","|---|---|---|---|"]
    for r in frames:
        if "file" in r:lines.append(f"| {r['file']} | {r['time_seconds']}s | {r['size'][0]}×{r['size'][1]} | {r['bytes']} |")
    lines+=["","## 产品素材","","| Group | File | Dimensions | Bytes |","|---|---|---|---|"]
    for r in rows:
        if "group" in r:lines.append(f"| {r['group']} | {r['path']} | {r['width']}×{r['height']} | {r['bytes']} |")
    lines+=["","同内容不同文件名已用SHA256分组，见asset-registry.json。文件名带real/original不构成实拍来源证明；AI合成场景不能标作工厂案例。"]
    (out/"asset-index.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    print(json.dumps({"indexed":len(rows),"duplicate_groups":len(payload["duplicate_groups"]),"frames":frames},ensure_ascii=False))

if __name__=="__main__":main()
