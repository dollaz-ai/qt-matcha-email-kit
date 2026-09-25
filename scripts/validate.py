"""Validate local handoff files without accessing external accounts."""
from pathlib import Path
from html.parser import HTMLParser
import json,re,hashlib
r=Path(__file__).resolve().parents[1]
errors=[]
class Links(HTMLParser):
 def handle_starttag(self,tag,attrs):
  for k,v in attrs:
   if k in ('src','href') and v and not v.startswith(('http:','https:','mailto:','#','data:','{%','{{')):
    p=(self.base/v.split('#')[0].split('?')[0]);
    if not p.exists():errors.append(f'{self.base}: missing {v}')
for file in [r/'index.html',r/'templates/welcome-1-preview.html']:
 parser=Links();parser.base=file.parent;parser.feed(file.read_text())
for file in [r/'README.md',r/'USAGE.md',*list((r/'docs').glob('*.md'))]:
 for target in re.findall(r'\]\(([^)]+)\)',file.read_text()):
  if not target.startswith(('https:','http:','#')) and not (file.parent/target.split('#')[0]).exists():errors.append(f'{file.name}: missing {target}')
assert len(list((r/'assets/illustrations/svg').glob('*.svg')))==21
assert len(list((r/'assets/illustrations/png').glob('*.png')))==21
assert len(list((r/'assets/lifestyle/webp').glob('*.webp')))==17
assert len(list((r/'assets/lifestyle/email-jpg').glob('*.jpg')))==17
assert len(list((r/'designs').glob('*-desktop.png')))==7
assert len(list((r/'designs').glob('*-mobile.png')))==7
assets=json.loads((r/'templates/asset-map.json').read_text());definition=json.loads((r/'templates/welcome-1.klaviyo-definition.json').read_text())
def walk(x):
 if isinstance(x,dict):
  if x.get('asset_id') and x['asset_id'] not in assets:errors.append('Unmapped template asset '+x['asset_id'])
  for v in x.values():walk(v)
 elif isinstance(x,list):
  for v in x:walk(v)
walk(definition)
for path in assets.values():assert (r/path).exists()
for p in r.rglob('*'):
 if p.is_file() and '.git' not in p.parts and p.suffix in ('.html','.json','.md','.svg'):
  text=p.read_text()
  for pattern in [r'gh[pousr]_[A-Za-z0-9]{30,}',r'pk_[A-Za-z0-9]{25,}',r'/Users/',r'BEGIN (?:RSA |OPENSSH )?PRIVATE KEY']:
   if re.search(pattern,text):errors.append('Sensitive/local data pattern: '+str(p.relative_to(r)))
if errors:raise SystemExit('\n'.join(errors))
print('PASS: counts, relative links, template assets and public-handoff content checks')
