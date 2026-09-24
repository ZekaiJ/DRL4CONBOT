"""Summarize candidate evidence and unresolved source assessments separately."""
import csv
import json
from pathlib import Path

root = Path(__file__).resolve().parent
with (root / 'additional_measures.csv').open(encoding='utf-8', newline='') as f:
    rows = list(csv.DictReader(f))
assert len(rows) == 150
assert len({(r['report_id'], r['indicator']) for r in rows}) == 150
results = {}
for indicator in sorted({r['indicator'] for r in rows}):
    group = [r for r in rows if r['indicator'] == indicator]
    assert len(group) == 30 and all(r['evidence_identified'] in ('Y', 'N', 'U') for r in group)
    count = sum(r['evidence_identified'] == 'Y' for r in group)
    unresolved = sum(r['evidence_identified'] == 'U' for r in group)
    results[indicator] = {
        'candidate_positive': count,
        'candidate_negative': sum(r['evidence_identified'] == 'N' for r in group),
        'unresolved': unresolved,
        'configurations': 30,
        'finalized': False,
    }
print(json.dumps(results, indent=2))
