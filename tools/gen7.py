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
TOTAL=6
slides=[]
def qcard(quote,who,sub,dark,top_,size=46):
    bg=NAVY2 if dark else '#FFFFFF'; bd='#2C4D7A' if dark else '#E2D6BE'; fg=CREAM if dark else NAVY; sc='#D9E2EE' if dark else MUTED
    return f'''<div style="position:absolute;left:72px;width:936px;top:{top_}px;background:{bg};border:2px solid {bd};border-radius:26px;padding:34px 40px 30px 52px">
<div style="position:absolute;left:0;top:26px;bottom:26px;width:12px;border-radius:6px;background:{AMBER}"></div>
<div style="font-weight:800;font-size:{size}px;line-height:1.18;letter-spacing:-1px;color:{fg}">&ldquo;{quote}&rdquo;</div>
<div style="margin-top:18px;font-weight:800;font-size:26px;color:{AMBER if dark else '#8A4B00'}">{who}</div>
<div style="font-size:23px;color:{sc};margin-top:2px">{sub}</div></div>'''
SRC="Source: Quora thread on retiring/returning to Bangalore after years in the US. Individual opinions, not advice."
# 1 cover
chips=[("Went back","glad they did"),("Went back","warns others not to"),("Your view?","RETURN or STAY")]
chip_html=''.join(f'<div style="display:flex;flex-direction:column;background:{NAVY2};border:2px solid #2C4D7A;border-radius:16px;padding:12px 22px"><span style="font-size:26px;font-weight:600;color:#D9E2EE">{a}</span><span style="color:{AMBER};font-size:32px;font-weight:800;line-height:1.15">{b}</span></div>' for a,b in chips)
inner=f'''<div style="position:absolute;left:72px;top:64px;font-weight:800;font-size:34px">NRI Sathi</div>
<div style="position:absolute;right:72px;top:58px;background:{AMBER};color:{NAVY};font-weight:800;font-size:24px;padding:10px 22px;border-radius:999px">NRI VOICES · QUORA</div>
<div style="position:absolute;left:0;top:0;width:1080px;height:925px;overflow:hidden"><img src="{CUT}" style="position:absolute;left:390px;top:195px;width:960px;height:768px"></div>
<div style="position:absolute;left:0;right:0;top:780px;height:145px;background:linear-gradient(to bottom,rgba(15,39,71,0),{NAVY})"></div>
<h1 style="position:absolute;left:72px;right:72px;top:130px;margin:0;font-weight:800;font-size:68px;line-height:1.1;letter-spacing:-2px">They moved back to India. {mark('Worth it?')}</h1>
<div style="position:absolute;left:72px;top:400px;width:480px;display:flex;flex-direction:column;gap:14px">{chip_html}</div>
<div style="position:absolute;left:72px;top:850px;font-weight:700;font-size:30px;color:{AMBER}">Swipe →</div>'''
slides.append(base(1,True,inner,"Real answers from a public Quora thread. Individual opinions, not advice.",line_svg(0,dot=72,start=True)))
# 2 Rajiv
inner=top(2,False,"WENT BACK · HAPPY")+f'<div style="position:absolute;left:72px;top:108px">{pill("20 YEARS IN THE US","amber")}</div>'+headline(f"After 10+ years back, a {mark('success')}",False,62,170)
inner+=qcard("I would call it a success.","Rajiv S.","Returned after 20+ years in the US",False,350,56)
inner+=rows([("His surprise","Extended family is not what it was in the 70s and 80s, especially in the metros."),("His upside","He now works for the love of it, not to pay a mortgage.")],False,640)
slides.append(base(2,False,inner,SRC,line_svg(1,dot=540,label="HAPPY",dark=False)))
# 3 Sucharita
inner=top(3,True,"WENT BACK · HAPPY")+f'<div style="position:absolute;left:72px;top:108px">{pill("A DECADE IN CALIFORNIA","amber")}</div>'+headline(f"Back in Bangalore: {mark('the right call')}",True,62,170)
inner+=qcard("we took the right decision coming back","Sucharita","Moved from Santa Clara to Bangalore",True,350,50)
inner+=rows([("Why","Closer to parents, extended family and old school and college friends."),("Honest note","Bangalore has changed, and some changes are not for the better.")],True,640)
slides.append(base(3,True,inner,SRC,line_svg(2,dot=540,label="HAPPY")))
# 4 warning
inner=top(4,False,"WENT BACK · WARNING")+f'<div style="position:absolute;left:72px;top:108px">{pill("THE OTHER SIDE","red")}</div>'+headline(f"Others say: {mark('do not come back')}",False,62,170)
inner+=qcard("DON'T COME BACK. This is a practical answer, not emotional.","Bhuvana R.","Lives in India; reply to a 45-years-in-the-US asker",False,350,44)
inner+=rows([("Her point","After decades in an orderly country, the chaos is hard to adjust to."),("Her tip","Consider a tier-2 or tier-3 town for health reasons.")],False,640)
slides.append(base(4,False,inner,SRC,line_svg(3,dot=540,label="WARNING",dark=False)))
# 5 pattern
STATTOP=380
inner=top(5,True,"THE PATTERN")+f'<div style="position:absolute;left:72px;top:108px">{pill("IN THE ANSWERS WE READ","amber")}</div>'+headline(f"It is rarely about {mark('salary')}",True,64,170)
inner+=stats([("Happy","family, cheap help, good hospitals"),("Unhappy","crowds, noise, pollution"),("Both","expectations matter most")],True)
inner+=rows([("Plus","Several returnees say household help and healthcare are easy and affordable."),("Minus","Others say traffic, noise and dust wore them down.")],True,580)
slides.append(base(5,True,inner,"Based on a handful of Quora answers, not a survey. Individual opinions, not advice.",line_svg(4,dot=540,label="WHAT STANDS OUT")))
# 6 CTA
inner=top(6,True,"YOUR TURN")+f'''<img src="{AVA}" style="position:absolute;right:72px;top:96px;width:320px;height:320px;border-radius:50%;border:5px solid {AMBER};object-fit:cover">
<h1 style="position:absolute;left:72px;top:140px;width:600px;margin:0;font-weight:800;font-size:60px;line-height:1.12;letter-spacing:-1.5px">{mark('RETURN')} or {mark('STAY')}?</h1>
<div style="position:absolute;left:72px;top:460px;display:flex;flex-direction:column;gap:14px;font-size:32px;font-weight:600"><div>Have you moved back? Was it worth it?</div><div>What surprised you the most?</div><div>What is stopping you?</div></div>
<div style="position:absolute;left:72px;right:72px;top:640px;background:{AMBER};color:{NAVY};border-radius:22px;padding:22px 28px;font-weight:800;font-size:32px;line-height:1.28">Share your experience in the comments.</div>
<div style="position:absolute;left:72px;top:785px;font-size:30px;line-height:1.4;font-weight:800;color:{AMBER}">Save this. Follow NRI Sathi.<br><span style="color:{CREAM}">New NRI update every day. See you tomorrow!</span></div>'''
slides.append(base(6,True,inner,"Quotes from public Quora answers, credited by display name. Not financial, tax or legal advice.",line_svg(5,dot=300,end=True)))
import os; os.makedirs('/tmp/v4/o7',exist_ok=True)
for i,h in enumerate(slides,1): open(f'/tmp/v4/o7/q{i}.html','w').write(h)
