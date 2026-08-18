---
title: Compliance Custom Scripts
parent: Cmds
nav_order: 1
has_children: false
has_toc: false
description: "Python and Apps Script helpers for extracting, enriching, and converting compliance control-benchmark data (AWS/Azure/GCP/OCI plugin catalogs)."
---

# Compliance Custom Scripts

One-off scripts for wrangling the control-benchmark JSON behind compliance plugins — no write-up per script, just the files themselves.

| Script | Purpose |
|---|---|
| [`cm_extract_unique_plugins.py`](cm_extract_unique_plugins.py) | Dedupes Plugin Names across the AWS/Azure/Google/Oracle control-benchmark files (first occurrence wins) into `unique_plugins.json`. |
| [`extract_unique_plugin.py`](extract_unique_plugin.py) | Extracts unique Plugin Name + Description pairs from `aws_offline_data.json`. |
| [`extract_control_names.py`](extract_control_names.py) | Extracts all unique ISO 27001:2022 control names from the AWS offline data JSON. |
| [`extract_plugin_more_info.py`](extract_plugin_more_info.py) | Pulls Plugin Name + `more_info` out of `azure_offline_data_enriched.json` into a new JSON file. |
| [`enrich_more_info.py`](enrich_more_info.py) | Enriches `azure_offline_data.json` with `more_info` from `gcp_plugin_info_only.json`, matched by Plugin Name. |
| [`enrich.py`](enrich.py) | Copies fields (Description, Recommended Action, …) from `oracle_offline_data.json` into `soc.json` by matching key. |
| [`extract.py`](extract.py) | Converts an XLSX control-benchmark sheet (default: ISO 27001:2022) to JSON. |
| [`convert_json_to_csv.py`](convert_json_to_csv.py) | Converts a JSON file to CSV. |
| [`convert_csv_to_xlsx.py`](convert_csv_to_xlsx.py) | Converts a CSV file to XLSX. |
| [`google_sheet.js`](google_sheet.js) | Apps Script bound to a Google Sheet — exports its rows to JSON and saves them to Drive. |
