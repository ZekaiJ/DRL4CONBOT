# Publication versions and sensitivity analysis

Four reports in the structured comparison are cited as arXiv versions. Publication records were checked on 18 September 2026, after the search cutoff of 28 August 2026; no reports were added to the review.

| Report | Cited version | Status at the check date |
|---|---|---|
| R012, Jin et al. | [arXiv:2303.16427](https://arxiv.org/abs/2303.16427) | Formal version not identified |
| R024, Yoo et al. | [arXiv:2406.19848](https://arxiv.org/abs/2406.19848) | Formal version not identified |
| R026, Gruetter et al. | [arXiv:2509.17683](https://arxiv.org/abs/2509.17683) | Listed in the [ICRA 2026 program](https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_5.html); final proceedings version not verified |
| R159, Xiao et al. | [arXiv:2308.16280](https://arxiv.org/abs/2308.16280) | Formal version not identified |

The protection comparison was repeated after excluding the three reports without an identified formal version, then all four arXiv-cited reports. Retained classifications were unchanged. Higher exposure denotes L3–L5, lower exposure L0–L2, and protection denotes command intervention or formal enforcement.

| Reports excluded | Configurations retained | Higher exposure | Lower exposure | Difference (percentage points) |
|---|---:|---:|---:|---:|
| None | 102 | 13/30 (43.3%) | 9/72 (12.5%) | 30.8 |
| R012, R024, R159 | 99 | 12/29 (41.4%) | 9/70 (12.9%) | 28.5 |
| R012, R024, R026, R159 | 98 | 11/28 (39.3%) | 9/70 (12.9%) | 26.4 |

The contrast remains positive in both analyses. These exclusions test sensitivity to the cited versions, not publication bias or restriction to a fully verified peer-reviewed corpus. Failure to identify a formal version does not establish that none exists.

Run `python publication_version_sensitivity.py` from this folder to reproduce the table from the configuration data. Differences use unrounded proportions.
