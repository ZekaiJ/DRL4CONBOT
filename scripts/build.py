"""Build a self-contained static site using Python's standard library."""
from pathlib import Path
import shutil
import json
import csv
from library import records, page

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / '_site'

def build():
    OUTPUT.mkdir(exist_ok=True)
    html = (ROOT / 'docs/index.html').read_text(encoding='utf-8')
    html = html.replace('../Assets/overview/', 'assets/overview/')
    html = html.replace('../Supplementary/', 'https://github.com/ZekaiJ/DRL4CONBOT/tree/main/Supplementary/')
    html = html.replace('../LICENSE', 'https://github.com/ZekaiJ/DRL4CONBOT/blob/main/LICENSE')
    html = html.replace('<a href="#framework">Framework</a>', '<a href="papers.html">Paper Library</a><a href="#framework">Framework</a>')
    (OUTPUT / 'index.html').write_text(html, encoding='utf-8')
    shutil.copy2(ROOT / 'docs/styles.css', OUTPUT / 'styles.css')
    shutil.copytree(ROOT / 'Assets/overview', OUTPUT / 'assets/overview', dirs_exist_ok=True)
    rows=records((ROOT/'README.md').read_text(encoding='utf-8'))
    library_html=page(rows).replace('<p id="count"', '<p><a href="reports.csv" download="drl4conbot-all-reports.csv">Download all 136 reports as CSV</a> · Bibliographic metadata only</p><p id="count"')
    (OUTPUT/'papers.html').write_text(library_html,encoding='utf-8')
    (OUTPUT/'reports.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
    with (OUTPUT/'reports.csv').open('w',encoding='utf-8-sig',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=['id','title','year','role','task','url','note'])
        writer.writeheader()
        writer.writerows({key: "'"+str(value) if str(value).startswith(('=','+','-','@','\t','\r')) else value for key,value in row.items()} for row in rows)
    for name in ('library.js','library.css'):
        shutil.copy2(ROOT/'docs'/name,OUTPUT/name)
    print('Built _site with self-contained overview assets')

if __name__ == '__main__':
    build()
