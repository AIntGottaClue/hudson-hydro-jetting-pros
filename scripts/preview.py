from pathlib import Path
import re
for p in Path('dist').rglob('*.html'):
 s=p.read_text(); s=re.sub(r'((?:href|src)=["\'])/(?!/)',r'\1/hudson-hydro-jetting-pros/',s);p.write_text(s)
