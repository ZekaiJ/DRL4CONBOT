from pathlib import Path
import csv, json
from collections import Counter
ROOT = Path(__file__).resolve().parent
def read(name):
    with (ROOT / "data" / name).open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))
reports = read("S2_included_reports.csv")
configs = read("S4_configuration_characteristics.csv")
recovery = read("S5_recovery_transitions.csv")
eligibility = read("S1_fulltext_eligibility_decisions.csv")
lineages = read("S3_report_lineages.csv")
locations = read("S12_recovery_source_locations.csv")
screening = read("title_abstract_screening.csv")
assert len(reports) == 136 and len(configs) == 100 and len(recovery) == 30
assert len({r["configuration_id"] for r in configs}) == 100
report_ids = {r["report_id"] for r in reports}
assert len(report_ids) == 136
assert len(eligibility) == 175 and len(screening) == 3138
assert Counter(r["eligibility_decision"] for r in eligibility) == {"include": 136, "exclude": 39}
assert {r["report_id"] for r in eligibility if r["eligibility_decision"] == "include"} == report_ids
assert len(lineages) == 136 and {r["report_id"] for r in lineages} == report_ids
assert {r["representative_report_id"] for r in configs} <= report_ids
assert Counter(r["synthesis_role"] for r in reports) == {"Structured comparative": 101, "Eligible contextual": 35}
high_ids = {r["representative_report_id"] for r in configs if r["validation_exposure_code"] in ("L3", "L4", "L5")}
assert len(high_ids) == 30 and {r["report_id"] for r in recovery} == high_ids
assert len(locations) == 30 and {r["report_id"] for r in locations} == high_ids
stages = ["detection", "response", "restoration", "continuation"]
counts = {s: sum(r[s + "_status"] == "Enacted in the final evaluation" for r in recovery) for s in stages}
assert list(counts.values()) == [13, 4, 2, 2]
def cross(a, b):
    return {v: dict(Counter(r[b] for r in configs if r[a] == v)) for v in sorted({r[a] for r in configs})}
result = {
    "eligible_reports": len(reports),
    "report_roles": dict(Counter(r["synthesis_role"] for r in reports)),
    "configurations": len(configs),
    "regimes": dict(Counter(r["task_and_failure_regime"] for r in configs)),
    "exposure": dict(Counter(r["validation_exposure_code"] for r in configs)),
    "protection": dict(Counter(r["execution_time_protection"] for r in configs)),
    "authority_by_protection": cross("learned_role_in_execution", "execution_time_protection"),
    "protection_by_exposure": cross("execution_time_protection", "validation_exposure_code"),
    "regime_by_exposure": cross("task_and_failure_regime", "validation_exposure_code"),
    "recovery_denominator": len(recovery),
    "recovery_demonstrated": counts,
}
(ROOT / "results.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps(result, indent=2))
