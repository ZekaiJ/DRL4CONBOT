# Physical outcome evidence in 30 construction-robotics configurations

This supplement documents three outcome indicators for the 30 configurations evaluated under construction-representative, field or workflow-integrated conditions in the DRL4CONBOT review. The unit of analysis is an executing configuration, not a trial, robot or independent deployment.

## Indicators

- **E (endpoint)**: explicit physical task success, completion or attainment of a stated terminal condition. Tracking alone is insufficient. A declared local endpoint need not represent completion of an entire construction operation.
- **W (work output)**: evaluation of actual material, component or work output beyond robot-motion metrics. Qualitative physical-output comparisons and reported estimates qualify. Quantities inferred solely from robot motion do not automatically qualify.
- **D (subsequent state)**: characterization of the physical condition left by an operation with an explicit connection to subsequent work, planning or execution. Repeated operation alone is insufficient. Recovery indicators are assessed separately.

Y denotes qualifying evidence in the inspected physical evaluation. N denotes that qualifying evidence was not identified, not that the system lacks the capability. These indicators are assessed separately and are not assumed to form nested sets. Their proportions are reporting frequencies, not task success rates.

## Files and reproduction

`physical_outcomes.csv` contains configuration identifiers, source links, locations and evidence-scope notes. PDF page numbers refer to the inspected PDF sequence and may differ from printed pagination. R109 uses publisher HTML section and figure references. Bibliographic details should be read with the linked source.

Run `python reproduce.py` from this directory to calculate E/W/D counts and percentages, both overall and by validation exposure. No additional software packages are needed. The calculation uses the classifications in the table; it does not replace reading the original studies.

`additional_measures.csv` documents the other five reporting features in Table 8: motion results (14 configurations), physical time or throughput (10), human effort or enacted intervention (6), repeated-evaluation denominators (17), and reported or uniquely determinable unsuccessful counts (10). Run `python reproduce_additional.py` to reproduce the counts and percentages. Source notes are retained in their original English or Chinese wording.

Measured trajectories with numerical coordinates qualify as motion results; commands and planned paths alone do not. Evaluation denominators retain their original units, including cycles within workflows and participants in comparisons. Unsuccessful counts may be derived only when reported outcomes and denominators uniquely determine them. Approximate counts remain approximate. Evidence from a lower-exposure test is not transferred to the highest-exposure evaluation.

Human-effort evidence includes qualitative assessments of actual operator involvement or workload; it does not necessarily quantify labor savings. Preparation and adaptation alone do not establish an intervention outcome in the final evaluation. N means that qualifying evidence was not identified, not zero failures, zero human involvement, or absence of a capability.

Update, 24 September 2026: previously unresolved assessments were checked against the source papers. All 150 assessments now have a Y or N decision. Uncertainties about actors or exact trial counts remain in the notes. This update does not change the separately assessed E/W/D records and is not an additional independent human reassessment.

## Review process and scope

The authors checked and approved the 30 E/W/D outcome records. This process was not independent duplicate assessment, and no agreement statistic was calculated before discussion. The additional five measures were subsequently reassessed against source notes and disputed passages on 24 September 2026; they are not covered by the independent exposure/protection reassessment. Supplementary videos and other media were not reviewed exhaustively.

The supplement provides bibliographic links and evidence summaries rather than reproducing publisher full texts, figures or restricted database records.
