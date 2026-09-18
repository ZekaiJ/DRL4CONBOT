"""Generate the public report library from the complete README catalog."""
import re, json, html

def records(text):
    section = text.split('## 📚 Papers by Category',1)[1].split('<a id="overview">',1)[0]
    result=[]; task=''
    for line in section.splitlines():
        if line.startswith('### '): task=line[4:]
        match=re.match(r'- (.+)\. \*\*(\d{4})\*\* · (Structured|Contextual) · `(R\d+)`\.(.*)',line)
        if not match: continue
        title,year,role,rid,note=match.groups()
        link=re.fullmatch(r'\[(.*)\]\((https://[^)]+)\)',title)
        url=''
        if link: title,url=link.groups()
        result.append(dict(id=rid,title=title,year=year,role=role,task=task,url=url,note=note.strip()))
    if len(result)!=136 or len({r['id'] for r in result})!=136:
        raise ValueError('Catalog must contain 136 distinct reports')
    return result

def page(rows):
    esc=html.escape
    cards=[]
    for r in rows:
        title=f'<a href="{esc(r["url"],quote=True)}">{esc(r["title"])}</a>' if r['url'] else esc(r['title'])
        cards.append(f'<article class="paper" id="{r["id"]}"><h2>{title}</h2><p>{r["year"]} · {r["role"]} · {esc(r["task"])}</p><p>{esc(r["note"])}</p><a href="#{r["id"]}" aria-label="Link to {r["id"]}">{r["id"]}</a></article>')
    options=lambda values: ''.join(f'<option>{esc(v)}</option>' for v in values)
    return '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Paper Library | DRL4CONBOT</title><link rel="stylesheet" href="styles.css"><link rel="stylesheet" href="library.css"></head><body><main><nav><a href="index.html">DRL4CONBOT overview</a><a href="https://github.com/ZekaiJ/DRL4CONBOT#papers-by-category">Markdown catalog</a></nav><h1>Paper Library</h1><p>136 eligible reports · 103 structured · 33 contextual. These are reports, not 136 independent configurations. Review roles are not quality scores.</p><form id="filters" hidden><label>Search title or report ID<input id="query" type="search" placeholder="Excavation, assembly, R063…"></label><label>Task<select id="task"><option value="">All tasks</option>'''+options(dict.fromkeys(r['task'] for r in rows))+'''</select></label><label>Year<select id="year"><option value="">All years</option>'''+options(sorted({r['year'] for r in rows},reverse=True))+'''</select></label><label>Review role<select id="role"><option value="">All roles</option><option>Structured</option><option>Contextual</option></select></label><button type="reset">Clear filters</button><button type="button" id="export">Export results as CSV</button></form><p id="count" role="status" aria-live="polite">136 reports</p><p id="empty" hidden>No matching reports. Clear filters or try a broader search.</p><noscript><p>All reports are shown below. Use your browser's Find command to search.</p></noscript><div id="papers">'''+''.join(cards)+'''</div><p>Exports contain bibliography metadata from this catalog, not the full configuration data or reproduction package.</p><script src="library.js" defer></script></main></body></html>'''
