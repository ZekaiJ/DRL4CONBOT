"""Recalculate descriptive E/W/D counts without third-party dependencies."""
from pathlib import Path
import csv
import json

rows = list(csv.DictReader((Path(__file__).parent/'physical_outcomes.csv').open(encoding='utf-8-sig',newline='')))
assert len(rows) == 30, 'Expected 30 high-exposure configurations'
assert len({r['configuration_id'] for r in rows}) == len(rows), 'Duplicate configuration'
indicators = ('endpoint','work_output','subsequent_state')
assert all(r[k] in {'Y','N'} for r in rows for k in indicators), 'Unresolved or invalid label'
assert all(r['exposure'] in {'L3','L4','L5'} for r in rows), 'Invalid exposure'
assert all(r['source_url'].startswith('https://') and r['source_locator'] and r['evidence_basis_and_scope'] for r in rows), 'Missing source evidence'

def summarize(group):
    return {k: {'yes': sum(r[k]=='Y' for r in group), 'no': sum(r[k]=='N' for r in group), 'denominator':len(group), 'percent':round(100*sum(r[k]=='Y' for r in group)/len(group),1) if group else None} for k in indicators}

print(json.dumps({'all':summarize(rows),'by_exposure':{level:summarize([r for r in rows if r['exposure']==level]) for level in ('L3','L4','L5')}},indent=2))
