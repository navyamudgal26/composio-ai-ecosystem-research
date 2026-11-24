# Composio AI Ecosystem Research

## Overview
Research tracker for 100 applications across 10 categories, assessing API availability,
authentication, access models, API capabilities, MCP ecosystem evidence and buildability.

## Current progress
- Total applications: 100
- Researched: 3
- Partially researched: 26
- Other / pending: 71

## Project structure
- `data/apps_100.csv` — master application research dataset
- `output/` — source audits and evidence-gap reports
- `case_study/index.html` — self-contained HTML research snapshot
- `Composio_Research_Agent.ipynb` — notebook workflow

## Run
1. Install dependencies: `pip install pandas requests beautifulsoup4 matplotlib python-dotenv openpyxl`
2. Open `Composio_Research_Agent.ipynb` in Jupyter.
3. Run notebook cells in order.
4. Open `case_study/index.html` in a browser.

## Research integrity
This is a progress snapshot. Unverified fields are not treated as confirmed findings.
HTTP success does not prove API or MCP availability. Vendor-maintained and community
MCP implementations must be distinguished. Accuracy must only be reported against a
valid manually labelled evaluation set.

## Evidence
Use the official evidence URLs recorded in `data/apps_100.csv`. Review source ownership,
documentation content, plan restrictions and regional limitations before final claims.
