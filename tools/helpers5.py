import math, base64, os
NAVY="#0F2747"; NAVY2="#17365F"; CREAM="#FFF6E5"; AMBER="#F4A93B"; LINE="#E8920C"
INK="#0F2747"; MUTED="#3B4C66"; GREEN="#0B7A4B"; RED="#C62828"
def b64(p,mime): return f"data:{mime};base64,"+base64.b64encode(open(p,'rb').read()).decode()
CUT=b64('/tmp/v4/bust_cut.png','image/png'); AVA=b64('/tmp/v4/avatar5.jpg','image/jpeg')
TOTAL=7
def ypath(x): return 915+18*math.sin(2*math.pi*x/1500+0.6)
def line_svg(i, dot=None, label=None, end=False, start=False, dark=True):
    off=i*1080
    pts=[]
    x0=0 if not start else 72
    for x in range(x0,1081,20):
        pts.append(f"{x},{ypath(x+off):.1f}")
    d="M"+" L".join(pts)
    s=f'<svg style="position:absolute;left:0;top:0" width="1080" height="1080" viewBox="0 0 1080 1080"><path d="{d}" fill="none" stroke="{LINE}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
    if dot is not None:
        y=ypath(dot+off); tc= AMBER if dark else INK
        s+=f'<circle cx="{dot}" cy="{y:.1f}" r="13" fill="{LINE}" stroke="{NAVY if dark else CREAM}" stroke-width="5"/>'
        if label: s+=f'<text x="{dot}" y="{y-30:.1f}" font-family="Inter" font-weight="800" font-size="26" letter-spacing="1.5" fill="{tc}" text-anchor="{"start" if start else "middle"}">{label}</text>'
    if end:
        y=ypath(1000+off)
        s+=f'<path d="M1002,{y-14:.1f} L1030,{y:.1f} L1002,{y+14:.1f}" fill="none" stroke="{LINE}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
    return s+'</svg>'
def pill(txt,kind):
    bg,fg={'green':(GREEN,'#fff'),'red':(RED,'#fff'),'amber':(AMBER,NAVY)}[kind]
    return f'<div style="display:inline-block;background:{bg};color:{fg};font-weight:800;font-size:24px;letter-spacing:1.5px;padding:10px 22px;border-radius:999px">{txt}</div>'
def base(i,dark,inner,source,svg):
    bg=NAVY if dark else CREAM; fg=CREAM if dark else INK
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
body{{margin:0}} *{{box-sizing:border-box}}
.s{{position:relative;width:1080px;height:1080px;background:{bg};color:{fg};font-family:'Inter',sans-serif;overflow:hidden}}
</style></head><body><div class="s">{inner}{svg}
<div style="position:absolute;left:72px;right:72px;top:962px;font-size:21px;line-height:1.3;color:{'#D9E2EE' if dark else MUTED}">{source}<div style="margin-top:6px;opacity:.9">@nrisathi · General information, not financial, legal or immigration advice.</div></div>
</div></body></html>'''
def top(i,dark,tagtxt):
    c=AMBER if dark else MUTED
    return f'<div style="position:absolute;left:72px;top:64px;font-weight:800;font-size:24px;letter-spacing:3px;color:{c}">{i:02d} / {TOTAL:02d} &nbsp;·&nbsp; {tagtxt}</div>'
def stat(num,lab,dark,w):
    bg=NAVY2 if dark else '#FFFFFF'; bd='#2C4D7A' if dark else '#E2D6BE'; nc=AMBER if dark else NAVY; lc='#D9E2EE' if dark else MUTED
    return f'<div style="width:{w}px;background:{bg};border:2px solid {bd};border-radius:22px;min-height:150px;padding:18px 20px"><div style="font-weight:800;font-size:40px;line-height:1.05;color:{nc};white-space:nowrap">{num}</div><div style="font-size:22px;line-height:1.28;margin-top:8px;color:{lc}">{lab}</div></div>'
def stats(items,dark):
    n=len(items); w=int((936-20*(n-1))/n)
    return f'<div style="position:absolute;left:72px;top:{STATTOP}px;display:flex;gap:20px">'+''.join(stat(a,b,dark,w) for a,b in items)+'</div>'
STATTOP=470
def rows(items,dark,top_):
    out=f'<div style="position:absolute;left:72px;width:936px;top:{top_}px;display:flex;flex-direction:column;gap:12px">'
    lc=AMBER if dark else '#8A4B00'; bd='#2C4D7A' if dark else '#E2D6BE'
    for lab,txt in items:
        out+=f'<div style="border-top:2px solid {bd};padding-top:12px"><div style="font-weight:800;font-size:22px;letter-spacing:2.5px;color:{lc}">{lab.upper()}</div><div style="font-weight:600;font-size:28px;line-height:1.26;margin-top:4px">{txt}</div></div>'
    return out+'</div>'
def headline(txt,dark,size=76,top_=190):
    return f'<h1 style="position:absolute;left:72px;right:72px;top:{top_}px;margin:0;font-weight:800;font-size:{size}px;line-height:1.12;letter-spacing:-1.5px">{txt}</h1>'
def mark(w): return f'<span style="background:{AMBER};color:{NAVY};padding:0 12px;border-radius:10px">{w}</span>'
slides=[]
