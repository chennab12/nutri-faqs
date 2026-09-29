"""Animated cooking cartoons and learning flows, with reduced-motion support."""
from html import escape
from streamlit.components.v1 import html
from content import LESSONS

SCENES={x["title"]:x["visual"] for x in LESSONS}
SCENES.update({
    "Overview":["Foods","Meals","Weekly pattern","Practical choice"],
    "Kitchen tools":["Choose meal","Enter amounts","See estimate","Adjust safely"],
    "Sources":["Claim","Original source","Evidence quality","Decision"],
    "Compare approaches":["Conventional","Ayurveda","Homeopathy","Safe choice"],
    "Ayurveda in the kitchen":["Tradition","Whole foods","Check evidence","Keep safe"],
    "Homeopathy and decision guide":["Remedy claim","Evidence check","Do not delay care","Food plan"],
})

def show(title):
    stages=SCENES[title]
    blocks=[]
    for i,label in enumerate(stages):
        x=24+i*213
        blocks.append(f'<g class="card c{i}"><rect x="{x}" y="72" width="178" height="83" rx="17" fill="#fff" stroke="#a5ceb5" stroke-width="2"/><circle cx="{x+25}" cy="101" r="14" fill="#287b52"/><text x="{x+25}" y="106" text-anchor="middle" class="num">{i+1}</text><text x="{x+13}" y="137" class="label">{escape(label)}</text></g>')
    arrows="".join(f'<path d="M {202+i*213} 114 H {237+i*213}" class="path" marker-end="url(#arrow)"/>' for i in range(3))
    page=f'''<!doctype html><html><head><meta charset="utf-8"><style>
    body{{margin:0;font-family:system-ui,Segoe UI,sans-serif}}
    .frame{{overflow-x:auto;border:1px solid #c4ddc9;border-radius:18px;background:linear-gradient(125deg,#effaf1,#fff7e8)}}
    svg{{width:100%;height:auto;min-width:680px;display:block}}
    .title{{font-size:21px;font-weight:750;fill:#254736}}.label{{font-size:14px;font-weight:650;fill:#254736}}
    .num{{font-size:13px;font-weight:700;fill:#fff}}.small{{font-size:14px;fill:#476753}}
    .path{{stroke:#287b52;stroke-width:4;stroke-dasharray:10 7;fill:none;animation:flow 1.4s linear infinite}}
    .card{{animation:shine 4.8s ease-in-out infinite}}.c1{{animation-delay:1.2s}}.c2{{animation-delay:2.4s}}.c3{{animation-delay:3.6s}}
    .chef{{transform-origin:770px 235px;animation:bob 2.3s ease-in-out infinite}}.steam{{animation:steam 2s ease-in-out infinite}}
    @keyframes flow{{to{{stroke-dashoffset:-34}}}}@keyframes shine{{15%{{filter:drop-shadow(0 4px 5px #91c6a0)}}}}
    @keyframes bob{{50%{{transform:translateY(-5px)}}}}@keyframes steam{{50%{{opacity:.2;transform:translateY(-7px)}}}}
    @media(prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
    </style></head><body><div class="frame"><svg viewBox="0 0 900 284" role="img" aria-label="{escape(title)}: {escape(' to '.join(stages))}">
    <defs><marker id="arrow" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0 L7 3.5 L0 7" fill="#287b52"/></marker></defs>
    <text x="24" y="38" class="title">{escape(title)} · visual memory cue</text>
    {arrows}{''.join(blocks)}
    <rect x="24" y="185" width="658" height="72" rx="15" fill="#fff" stroke="#c4ddc9"/>
    <text x="41" y="211" class="small">Chef's reminder: think in meals and patterns, then check</text>
    <text x="41" y="234" class="small">personal needs and evidence before making health claims.</text>
    <g class="chef"><circle cx="775" cy="210" r="29" fill="#edbd8e" stroke="#ae7953"/>
    <path d="M743 191 Q739 177 753 173 Q757 157 771 167 Q789 152 797 169 Q814 167 812 189 Z" fill="#fff" stroke="#a1baa6" stroke-width="2"/>
    <circle cx="765" cy="208" r="3" fill="#213a30"/><circle cx="785" cy="208" r="3" fill="#213a30"/>
    <path d="M764 220 Q775 230 787 219" fill="none" stroke="#995a43" stroke-width="2"/>
    <rect x="741" y="238" width="67" height="40" rx="15" fill="#287b52"/>
    <path d="M812 253 h44" stroke="#edbd8e" stroke-width="10" stroke-linecap="round"/>
    <ellipse cx="855" cy="257" rx="20" ry="7" fill="#9c6548"/><ellipse cx="855" cy="251" rx="18" ry="5" fill="#f1c86c"/>
    <path class="steam" d="M848 243 q-5 -8 0 -16 M860 243 q-5 -8 0 -16" fill="none" stroke="#93ae9a" stroke-width="2"/></g>
    </svg></div></body></html>'''
    html(page,height=310,scrolling=False)
