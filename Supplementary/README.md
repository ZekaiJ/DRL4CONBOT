# Supplementary data

This package supports the review of deep reinforcement learning for construction robotics. The search cutoff is 28 August 2026. The review includes 136 reports: 101 structured reports describing 100 executing configurations, and 35 contextual reports.

## Files

| File | Content |
|---|---|
| search_strategies.md | Database search strategies and search scope |
| data/title_abstract_screening.csv | Decisions for 3,138 screened records; abstracts omitted |
| data/S1_fulltext_eligibility_decisions.csv | Eligibility decisions for 175 assessed reports |
| data/S2_included_reports.csv | The 136 included reports and synthesis roles |
| data/S3_report_lineages.csv | Report-to-lineage mappings |
| data/S4_configuration_characteristics.csv | The 100 executing configurations |
| data/S5_recovery_transitions.csv | Recovery assessments for 30 configurations |
| data/S12_recovery_source_locations.csv | Source pointers and explicit limitations of indicator-specific anchors |
| reproduce.py | Regenerates descriptive counts and cross-tabulations |
| [physical_outcomes/](physical_outcomes/README.md) | Source-linked E/W/D outcome records and a separate reproduction script for the 30 higher-exposure configurations |

## Reproduction

Run `python reproduce.py` with Python 3.10 or later. No third-party packages are required. The script writes results.json beside the script; that file is generated, not an additional input. Recovery indicator counts are 13, 4, 2, and 2. Reports, lineages, and configurations are distinct units.

The database route assessed 159 reports and included 121; supplementary searching assessed 16 and included 15. Four database reports could not be retrieved. Search results comprised 6,255 records before deduplication, 3,138 screened records, and 2,975 screening exclusions.

Assessments designated A/B were conducted independently by human reviewers. This statement does not imply duplicate assessment at every stage for every record. Source limitations and incomplete indicator anchors are retained. Undemonstrated recovery does not establish absence of the capability.

Original database exports, abstracts, and third-party full texts are not redistributed. The package supports tracing the recorded decisions and reproducing aggregate statistics, not repeating the full database-export and deduplication workflow. Third-party rights remain with their owners; no additional rights in those sources are granted here. Detailed review records remain in the research archive.

## Physical outcome evidence

The additional physical-outcome supplement can be reproduced with `python physical_outcomes/reproduce.py` from this directory. It reports 28 configurations with physical task-endpoint evidence, 12 with physical work-output evaluation, and 3 with a characterized post-operation state explicitly connected to subsequent work (denominator 30 for each). These are separately assessed reporting indicators, not nested categories or success rates. Work-output evidence includes qualitative comparisons of physical outputs. The supplement does not reassess the other five reporting features or the recovery indicators.

## Screening fields

The screening ledger retains the original process codes for traceability. They describe how entries were generated or inherited, rather than the identities of A/B reviewers. The available screening script assigns decisions using metadata rules or carries forward earlier screening records. Independent human A/B assessments are a separate review activity; these codes alone do not establish subsequent human checking of every rule-generated decision.

| ta_basis | Meaning in the screening script |
|---|---|
| ordered_rule | A metadata rule generated the screening decision |
| ordered_rule_conservative_include | No exclusion rule was triggered and the record was forwarded to full-text assessment |
| transferred_prior_frozen_screen | A matching prior screening decision was carried forward |
| gold_recall_protection | A previously included report was retrieved and forwarded to full-text assessment without applying the additional non-reference-record exclusion gates |
| uniform_scope_gate | An additional application-scope rule was applied to a record initially forwarded to full-text assessment |
| uniform_deep_embodied_gate | An additional deep-learning or embodied-execution rule was applied to a record initially forwarded to full-text assessment |

`ta_confidence` contains script-assigned scores for these paths, not calibrated probabilities or measures of reviewer agreement. `gold_report_id` and `gold_synthesis_group` refer to the previously included report set, not an independent validation standard. The one entry with a narrative `ta_basis` records a subsequent source-based decision. A carried-forward decision is not represented as a new source assessment.

S1–S5 and S12 retain the numbering used in the supporting records. The omitted intermediate tables are not required inputs to this minimal package. S12 preserves available page locations and verification limitations; source passages must be consulted before interpreting a page location as support for a particular recovery indicator.
