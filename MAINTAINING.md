# Maintaining the companion repository

## Local site build

Run from the repository root with Python 3.10 or later:

```sh
python scripts/build.py
python scripts/validate.py
node scripts/test_library.cjs
python -m http.server 8000 --directory _site
```

The deployable directory is `_site`, not `docs`. It contains its own assets and uses relative URLs compatible with a GitHub Pages project subpath. Build and validation do not deploy the website. Current checks test links, counts, and selected mappings, not scientific validity or full snapshot membership.

## Records and corrections

The library offers a filtered CSV export and a static `reports.csv` fallback containing all 136 reports. Both contain bibliographic metadata only, not configuration-level supplementary data. The static file is rebuilt from the same README records; do not edit it manually. Browser download completion must be checked separately from content tests.

Report IDs and configuration IDs are different units. Shared publication lineage alone does not establish a shared executing configuration. R019 belongs to Earthwork and Material Processing; R063 belongs to Structural Assembly and Installation. R001 and R041 are the explicitly consolidated companion-report pair.

The complete report list remains in README. Configuration counts and scientific labels have not been changed by this presentation correction. Eleven contextual reports retain their separate listing until source-supported mapping is established.

## Publication checks still open

- Source-linked supplementary data and analysis materials are not yet included here. The manuscript data-availability statement must not claim otherwise until actual release.
- Mori evaluation-stage takeover availability remains a scientific adjudication item, not a UI decision.
- GitHub Pages deployment and live mobile/keyboard checks are not established by a local build.
- Do not add publication status, a manuscript DOI, or dataset-download buttons without verified destinations.
