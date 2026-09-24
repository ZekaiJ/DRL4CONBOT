"""Reproduce publication-version exclusions without changing classifications."""
import csv
from pathlib import Path

path = Path(__file__).resolve().parent / 'data/S4_configuration_characteristics.csv'
with path.open(encoding='utf-8-sig', newline='') as stream:
    rows = list(csv.DictReader(stream))
assert len(rows) == 103
assert len({r['configuration_id'] for r in rows}) == 103
active = {'Command intervention', 'Formal runtime enforcement'}
cases = [set(), {'R012', 'R024', 'R159'}, {'R012', 'R024', 'R026', 'R159'}]
expected = [(103, 13, 30, 9, 73), (100, 12, 29, 9, 71), (99, 11, 28, 9, 71)]
for excluded, target in zip(cases, expected):
    kept = [r for r in rows if r['representative_report_id'] not in excluded]
    high = [r for r in kept if r['validation_exposure_code'] in {'L3', 'L4', 'L5'}]
    low = [r for r in kept if r['validation_exposure_code'] in {'L0', 'L1', 'L2'}]
    assert len(high) + len(low) == len(kept)
    h = sum(r['execution_time_protection'] in active for r in high)
    l = sum(r['execution_time_protection'] in active for r in low)
    assert (len(kept), h, len(high), l, len(low)) == target
    print(f"Excluded: {', '.join(sorted(excluded)) or 'none'}; N={len(kept)}; "
          f"higher={h}/{len(high)} ({100*h/len(high):.1f}%); "
          f"lower={l}/{len(low)} ({100*l/len(low):.1f}%); "
          f"difference={100*(h/len(high)-l/len(low)):.1f} percentage points")
