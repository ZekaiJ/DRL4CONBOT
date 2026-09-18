"""Check presentation integrity, not scientific correctness."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import re
import json
import csv
from build import ROOT, OUTPUT

class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.ids=set()
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if 'id' in attrs: self.ids.add(attrs['id'])
        self.links.extend(attrs[k] for k in ('href','src') if k in attrs)

def validate():
    text=(ROOT/'README.md').read_text(encoding='utf-8')
    ids=re.findall(r'`(R\d+)`',text)
    assert len(ids)==len(set(ids))==136, 'Report membership count/duplicates'
    assert len(re.findall(r'· Structured ·',text))==103
    assert len(re.findall(r'· Contextual ·',text))==33
    sections=text.split('### ')
    assert any(s.startswith('Structural Assembly') and '`R063`' in s for s in sections)
    assert any(s.startswith('Earthwork') and '`R019`' in s for s in sections)
    for file in OUTPUT.glob('*.html'):
        parser=Links(); parser.feed(file.read_text(encoding='utf-8'))
        for link in parser.links:
            url=urlsplit(link)
            if url.scheme or url.netloc: continue
            assert not url.path.startswith('/'), f'Root-relative link: {link}'
            target=(file.parent/unquote(url.path)).resolve() if url.path else file
            assert target.is_relative_to(OUTPUT.resolve()), f'Escapes publication directory: {link}'
            assert target.exists(), f'Missing: {link}'
            if url.fragment and target==file: assert url.fragment in parser.ids, link
    assert (OUTPUT/'index.html').exists()
    rows=json.loads((OUTPUT/'reports.json').read_text(encoding='utf-8'))
    assert {r['id'] for r in rows}==set(ids)
    assert len(rows)==136
    with (OUTPUT/'reports.csv').open(encoding='utf-8-sig',newline='') as stream:
        exported=list(csv.DictReader(stream))
    assert len(exported)==136
    assert {r['id'] for r in exported}==set(ids)
    assert sum(r['role']=='Structured' for r in exported)==103
    assert sum(r['role']=='Contextual' for r in exported)==33
    library=Links(); library.feed((OUTPUT/'papers.html').read_text(encoding='utf-8'))
    assert set(ids).issubset(library.ids)
    print('PASS: 136 unique reports, 103/33 roles, corrected mappings, deployable internal links')

if __name__=='__main__': validate()
