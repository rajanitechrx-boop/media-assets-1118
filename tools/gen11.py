import math, base64, os
NAVY="#0F2747"; NAVY2="#17365F"; CREAM="#FFF6E5"; AMBER="#F4A93B"; LINE="#E8920C"
INK="#0F2747"; MUTED="#3B4C66"; GREEN="#0B7A4B"; RED="#C62828"
def b64(p,mime): return f"data:{mime};base64,"+base64.b64encode(open(p,'rb').read()).decode()
CUT=b64('/tmp/v4/bust_cut.png','image/png'); AVA=b64('/tmp/v4/avatar6.jpg','image/jpeg')
TOTAL=5
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
TOTAL=5
slides=[]
SRC="Sources: Axis Bank GIFT City USD deposit rates (Nov 2026); HDFC Bank FCNR USD rates (1 Oct 2026). Rates change."
def row3(items,dark,top_):
    bg=NAVY2 if dark else '#FFFFFF'; bd='#2C4D7A' if dark else '#E2D6BE'; nc=AMBER if dark else NAVY; lc='#D9E2EE' if dark else MUTED
    out=f'<div style="position:absolute;left:72px;width:936px;top:{top_}px;display:flex;flex-direction:column;gap:14px">'
    for a,b,c in items:
        out+=f'<div style="display:flex;align-items:center;justify-content:space-between;background:{bg};border:2px solid {bd};border-radius:20px;padding:20px 28px"><div style="font-weight:800;font-size:38px;color:{nc};width:235px">{a}</div><div style="font-size:26px;color:{lc};width:360px;white-space:nowrap">{b}</div><div style="font-weight:800;font-size:38px;color:{GREEN if not dark else "#5CE0A0"};text-align:right;width:230px">{c}</div></div>'
    return out+'</div>'
# 1 cover with the headline number
inner=f'''<div style="position:absolute;left:72px;top:64px;font-weight:800;font-size:34px">NRI Sathi</div>
<div style="position:absolute;right:72px;top:58px;background:{AMBER};color:{NAVY};font-weight:800;font-size:24px;padding:10px 22px;border-radius:999px">FCNR vs GIFT CITY</div>
<div style="position:absolute;left:0;top:0;width:1080px;height:925px;overflow:hidden"><img src="{CUT}" style="position:absolute;left:430px;top:215px;width:900px;height:720px"></div>
<div style="position:absolute;left:0;right:0;top:780px;height:145px;background:linear-gradient(to bottom,rgba(15,39,71,0),{NAVY})"></div>
<h1 style="position:absolute;left:72px;right:72px;top:130px;margin:0;font-weight:800;font-size:66px;line-height:1.1;letter-spacing:-2px">USD 10,000 for 1 year. {mark('Extra USD 152')}</h1>
<div style="position:absolute;left:72px;top:400px;width:520px;display:flex;flex-direction:column;gap:14px">
<div style="background:{NAVY2};border:2px solid #2C4D7A;border-radius:16px;padding:12px 22px"><span style="font-size:26px;font-weight:600;color:#D9E2EE">GIFT City USD deposit</span><br><span style="color:{AMBER};font-size:40px;font-weight:800">USD 490</span></div>
<div style="background:{NAVY2};border:2px solid #2C4D7A;border-radius:16px;padding:12px 22px"><span style="font-size:26px;font-weight:600;color:#D9E2EE">FCNR deposit</span><br><span style="color:{AMBER};font-size:40px;font-weight:800">USD 338</span></div></div>
<div style="position:absolute;left:72px;top:850px;font-weight:700;font-size:30px;color:{AMBER}">Swipe for the maths →</div>'''
slides.append(base(1,True,inner,"Interest earned in 1 year on USD 10,000. See slide 2 for rates.",line_svg(0,dot=72,start=True)))
# 2 the calculation
inner=top(2,False,"THE CALCULATION")+headline(f"Same USD 10,000. {mark('Same 1 year')}",False,60,110)
inner+=row3([("GIFT City","4.90% simple","USD 490"),("FCNR","3.35% half-yearly","USD 338")],False,300)
inner+=f'<div style="position:absolute;left:72px;width:936px;top:520px;background:{AMBER};color:{NAVY};border-radius:22px;padding:26px 32px"><div style="font-weight:800;font-size:28px;letter-spacing:2px">YOUR EXTRA</div><div style="font-weight:800;font-size:76px;line-height:1.05;letter-spacing:-2px">USD 152</div><div style="font-weight:600;font-size:28px;margin-top:6px">490 minus 338. About 1.5% more on your money.</div></div>'
inner+=rows([("How","GIFT City: 10,000 x 4.90% = 490. FCNR: 10,000 x (1+3.35%/2)^2 − 10,000 = 338.")],False,790)
slides.append(base(2,False,inner,SRC,line_svg(1,dot=900,label="",dark=False)))
# 3 scale up
inner=top(3,True,"SCALE IT UP")+headline(f"The gap grows with your {mark('deposit')}",True,58,110)
inner+=row3([("USD 10,000","GIFT 490 · FCNR 338","+USD 152"),("USD 25,000","GIFT 1,225 · FCNR 845","+USD 380"),("USD 50,000","GIFT 2,450 · FCNR 1,689","+USD 761")],True,330)
inner+=rows([("Note","Extra interest, before any tax in your country of residence.")],True,800)
slides.append(base(3,True,inner,SRC,line_svg(2,dot=900,label="",dark=True)))
# 4 the catch
inner=top(4,False,"THE TRADE-OFF")+headline(f"Why the extra is {mark('not free')}",False,60,110)
inner+=rows([("Safety net","FCNR is covered by deposit insurance up to Rs 5 lakh. GIFT City deposits are not."),("Break early","FCNR pays nothing if you exit before 1 year. GIFT City callable deposits carry a 15 bps penalty."),("Rates move","Both change often. Lock the rate on the day you book."),("Fit","Check what your home country taxes before you compare.")],False,300)
slides.append(base(4,False,inner,SRC,line_svg(3,dot=900,label="",dark=False)))
# 5 CTA
inner=top(5,True,"YOUR TURN")+f'''<img src="{AVA}" style="position:absolute;right:72px;top:96px;width:320px;height:320px;border-radius:50%;border:5px solid {AMBER};object-fit:cover">
<h1 style="position:absolute;left:72px;top:140px;width:600px;margin:0;font-weight:800;font-size:60px;line-height:1.12;letter-spacing:-1.5px">{mark('FCNR')} or {mark('GIFT City')}?</h1>
<div style="position:absolute;left:72px;top:460px;display:flex;flex-direction:column;gap:14px;font-size:32px;font-weight:600"><div>Is USD 152 extra worth less cover?</div><div>Which do you use today?</div></div>
<div style="position:absolute;left:72px;right:72px;top:640px;background:{AMBER};color:{NAVY};border-radius:22px;padding:22px 28px;font-weight:800;font-size:32px;line-height:1.28">Tell us in the comments.</div>
<div style="position:absolute;left:72px;top:785px;font-size:30px;line-height:1.4;font-weight:800;color:{AMBER}">Save this. Follow NRI Sathi.<br><span style="color:{CREAM}">New NRI update every day. See you tomorrow!</span></div>'''
slides.append(base(5,True,inner,"Illustrative example, not a recommendation. Not financial, tax or legal advice.",line_svg(4,dot=300,end=True)))
import os; os.makedirs('/tmp/v4/o11',exist_ok=True)
for i,h in enumerate(slides,1): open(f'/tmp/v4/o11/f{i}.html','w').write(h)
