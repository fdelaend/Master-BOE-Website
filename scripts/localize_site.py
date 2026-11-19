"""Quarto post-render hook: static, page-matched FR/EN navigation."""
from pathlib import Path
import re,os
root=Path(__file__).resolve().parents[1]
out=Path(os.environ.get('QUARTO_PROJECT_OUTPUT_DIR',root/'_site'))
if not out.is_absolute():out=root/out
names=['index','a-propos','equipe','memoires','stages','liens','debouches','terrain']
labels={'À propos':'About','L’équipe':'Team','Mémoires':'Theses','Stage de terrain':'Field course','Stage professionnel':'Internship','Débouchés':'Careers','Liens utiles':'Useful links','Rejoindre le master ↗':'Admission ↗','Basculer la navigation':'Toggle navigation'}
for english in (False,True):
 for name in names:
  f=out/('en' if english else '')/(name+'.html')
  if not f.exists():continue
  text=f.read_text()
  match=re.search(r'<header id="quarto-header".*?</header>',text,re.S)
  if not match:raise RuntimeError(f'Missing navbar: {f}')
  nav=match.group()
  nav=re.sub(r'<div class="language-switch".*?</div>','',nav,flags=re.S)
  if english:
   for fr,en in labels.items():nav=nav.replace(fr,en)
   for target in names:
    nav=re.sub(r'href="(?:\.\./|\./|/)?'+re.escape(target)+r'\.html([#][^"]*)?"',lambda m:'href="'+target+'.html'+(m.group(1) or '')+'"',nav)
   # Root links may be absolute relative to a project deployed in a subdirectory.
   nav=re.sub(r'(<a class="navbar-brand" href=")[^"]*(")',r'\1index.html\2',nav)
  if english:
   nav=re.sub(r'(<a class="nav-link)(?: active)?("[^>]*href=")([^"]+)("[^>]*>)',lambda m:m.group(1)+(' active' if m.group(3).split('#')[0]==name+'.html' else '')+m.group(2)+m.group(3)+m.group(4),nav)
  fr=('../' if english else '')+name+'.html' 
  en=('' if english else 'en/')+name+'.html'
  switch='<div class="language-switch" role="group" aria-label="'+('Language' if english else 'Langue')+'">'
  for code,url,active in [('FR',fr,not english),('EN',en,english)]:
   switch+=f'<a href="{url}" lang="{code.lower()}" hreflang="{code.lower()}"'+(' aria-current="true"' if active else '')+f'>{code}</a>'
  switch+='</div>'
  nav=nav.replace('<div class="quarto-navbar-tools">',switch+'<div class="quarto-navbar-tools">')
  text=text[:match.start()]+nav+text[match.end():]
  if english:
   text=text.replace('Biologie des organismes et écologie</p>','Organismal Biology and Ecology</p>')
   text=re.sub(r'<html([^>]*?)lang="[^"]+"',r'<html\1lang="en"',text, count=1)
  # Alternate language metadata for search engines and assistive tooling.
  text=re.sub(r'<link rel="alternate" hreflang="(?:fr|en)"[^>]*>\n?','',text)
  text=text.replace('</head>',f'<link rel="alternate" hreflang="fr" href="{fr}">\n<link rel="alternate" hreflang="en" href="{en}">\n</head>')
  f.write_text(text)
