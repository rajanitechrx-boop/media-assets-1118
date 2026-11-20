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
slides=[]
SRC_BT="Sources: Business Today (27-28 Apr 2026)."
# 1 cover
chips=[("Zoho's Vembu","open letter: return home"),("BharatPe's Grover","called it unrealistic"),("NRI Sathi","what about your money?")]
chip_html=''.join(f'<div style="display:flex;flex-direction:column;background:{NAVY2};border:2px solid #2C4D7A;border-radius:16px;padding:12px 22px"><span style="font-size:26px;font-weight:600;color:#D9E2EE">{a}</span><span style="color:{AMBER};font-size:32px;font-weight:800;line-height:1.15">{b}</span></div>' for a,b in chips)
inner=f'''<div style="position:absolute;left:72px;top:64px;font-weight:800;font-size:34px">NRI Sathi</div>
<div style="position:absolute;right:72px;top:58px;background:{AMBER};color:{NAVY};font-weight:800;font-size:24px;padding:10px 22px;border-radius:999px">RETURN OR STAY · NOV 2026</div>
<div style="position:absolute;left:0;top:0;width:1080px;height:925px;overflow:hidden"><img src="{CUT}" style="position:absolute;left:390px;top:195px;width:960px;height:768px"></div>
<div style="position:absolute;left:0;right:0;top:780px;height:145px;background:linear-gradient(to bottom,rgba(15,39,71,0),{NAVY})"></div>
<h1 style="position:absolute;left:72px;right:72px;top:130px;margin:0;font-weight:800;font-size:68px;line-height:1.1;letter-spacing:-2px">Should NRIs return to India? {mark('Vembu vs Grover')}</h1>
<div style="position:absolute;left:72px;top:400px;width:480px;display:flex;flex-direction:column;gap:14px">{chip_html}</div>
<div style="position:absolute;left:72px;top:850px;font-weight:700;font-size:30px;color:{AMBER}">Swipe →</div>'''
slides.append(base(1,True,inner,"Based on public reports, Apr-Nov 2026. General information, not advice.",line_svg(0,dot=72,start=True)))
# 2 what happened
STATTOP=380
inner=top(2,False,"THE DEBATE")+f'<div style="position:absolute;left:72px;top:108px">{pill("APRIL 2026","amber")}</div>'+headline(f"Zoho's founder asked NRIs to {mark('come home')}",False,64,170)
inner+=stats([("Open letter","Vembu to Indians in the US"),("2023","Shenava (TuluAI) moved back, backs it"),("₹94/$","Grover: not realistic")],False)
inner+=rows([("Ask","Sridhar Vembu urged skilled Indians abroad to return and build India's tech strength."),("Reply","Ashneer Grover mocked the idea, pointing to the rupee rate and the heat.")],False,580)
slides.append(base(2,False,inner,SRC_BT+" Positions paraphrased.",line_svg(1,dot=540,label="TWO CAMPS",dark=False)))
# 3 why stay
STATTOP=380
inner=top(3,True,"WHY MANY STAY")+f'<div style="position:absolute;left:72px;top:108px">{pill("ONE INVESTOR\'S VIEW","amber")}</div>'+headline(f"Pay is {mark('not the main reason')}",True,66,170)
inner+=stats([("Daily life","civic quality of everyday life"),("Safety nets","dependable support systems"),("Predictable","systems work as expected")],True)
inner+=rows([("Who","Vineeth K, a Chicago-based investor, answered Vembu's call."),("Note","This is one person's view, not a survey. Many NRIs feel they never left India emotionally.")],True,580)
slides.append(base(3,True,inner,SRC_BT+" No statistics in the article.",line_svg(2,dot=540,label="THE OTHER SIDE")))
# 4 data
STATTOP=380
inner=top(4,False,"WHAT THE DATA SAYS")+f'<div style="position:absolute;left:72px;top:108px">{pill("FOUNDERS ONLY","amber")}</div>'+headline(f"Returnees start {mark('fast')}, then?",False,66,170)
inner+=stats([("Early","returnee founders do well (ORF study)"),("Later","India-trained founders lead"),("Rising","return migration, say experts")],False)
inner+=rows([("Study","ORF study: homegrown founders now outperform returnees in long-term outcomes."),("Why back","Startup scene, remote work, tight visa rules and family, per immigration experts.")],False,580)
slides.append(base(4,False,inner,"Sources: ORF study; Business Today, 6 Aug 2026. About startup founders, not all NRIs.",line_svg(3,dot=540,label="WHAT STUDIES SAY",dark=False)))
# 5 accounts
STATTOP=380
inner=top(5,True,"IF YOU RETURN")+f'<div style="position:absolute;left:72px;top:108px">{pill("YOUR BANK ACCOUNTS","red")}</div>'+headline(f"Your {mark('NRE and NRO')} accounts must change",True,64,170)
inner+=stats([("NRE / NRO","convert to resident or RFC"),("FCNR(B)","can run to maturity"),("RFC","keeps your foreign currency")],True)
inner+=rows([("Rule","Banks redesignate NRE and NRO once you become a resident. You cannot keep them as an NRI account."),("Tax","RNOR status may protect foreign income for a limited period. Confirm with a CA.")],True,580)
slides.append(base(5,True,inner,"Sources: ICICI Bank and IDFC FIRST NRI return guides. Rules change; check with your bank and a CA.",line_svg(4,dot=540,label="YOUR MONEY")))
# 6 checklist
items=["Tell your bank the date you return","Choose NRE to RFC or to resident, with numbers","Keep FCNR(B) deposits till maturity","Do not break FDs early; check RNOR with a CA"]
li=''.join(f'<div style="display:flex;gap:20px;align-items:flex-start;margin-bottom:22px"><div style="min-width:54px;height:54px;border-radius:50%;background:{AMBER};color:{NAVY};font-weight:800;font-size:30px;display:flex;align-items:center;justify-content:center">{k}</div><div style="font-weight:700;font-size:34px;line-height:1.25;padding-top:2px">{t}</div></div>' for k,t in enumerate(items,1))
inner=top(6,False,"CHECKLIST")+f'<div style="position:absolute;left:72px;top:108px">{pill("BEFORE YOU BOOK THE TICKET","amber")}</div>'+headline(f"Moving back? {mark('4 things')} first",False,66,170)
inner+=f'<div style="position:absolute;left:72px;top:380px;width:936px">{li}</div>'
slides.append(base(6,False,inner,"General information, not tax or legal advice. Rules differ by case; confirm with your bank and a CA.",line_svg(5,dot=540,label="PLAN FIRST",dark=False)))
# 7 CTA
inner=top(7,True,"YOUR TURN")+f'''<img src="{AVA}" style="position:absolute;right:72px;top:96px;width:320px;height:320px;border-radius:50%;border:5px solid {AMBER};object-fit:cover">
<h1 style="position:absolute;left:72px;top:140px;width:600px;margin:0;font-weight:800;font-size:60px;line-height:1.12;letter-spacing:-1.5px">{mark('RETURN')} or {mark('STAY')}?</h1>
<div style="position:absolute;left:72px;top:460px;display:flex;flex-direction:column;gap:14px;font-size:32px;font-weight:600"><div>Would you move back for a startup?</div><div>What would make you return?</div><div>What is stopping you?</div></div>
<div style="position:absolute;left:72px;right:72px;top:640px;background:{AMBER};color:{NAVY};border-radius:22px;padding:22px 28px;font-weight:800;font-size:32px;line-height:1.28">Comment RETURN or STAY and tell us why.</div>
<div style="position:absolute;left:72px;top:785px;font-size:30px;line-height:1.4;font-weight:800;color:{AMBER}">Save this. Follow NRI Sathi.<br><span style="color:{CREAM}">New NRI update every day. See you tomorrow!</span></div>'''
slides.append(base(7,True,inner,"Public reports and bank guides, Nov 2026. Always confirm with your bank before acting.",line_svg(6,dot=300,end=True)))
for i,h in enumerate(slides,1): open(f'/tmp/v4/r{i}.html','w').write(h)
