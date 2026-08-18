"""
Reads aws, azure, google, oracle control_benchmark files and extracts
unique Plugin Names with: Description, Severity, Domain, more_info.

Deduplication: first occurrence of a Plugin Name wins (order: aws → azure → google → oracle).
Output: unique_plugins.json in the same directory.
"""

import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))

CLOUD_FILES = [
    ("aws", "aws_offline_data.json"),
    ("azure", "azure_offline_data.json"),
    ("google", "google_offline_data.json"),
    ("oracle", "oracle_offline_data.json"),
]

EXTRACT_FIELDS = ["Plugin Name", "Description", "Severity", "Domain", "more_info"]

seen = set()
unique_plugins = []

for cloud, filename in CLOUD_FILES:
    path = os.path.join(BASE, filename)
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    added = 0
    for entry in data:
        plugin_name = entry.get("Plugin Name", "").strip()
        if not plugin_name or plugin_name in seen:
            continue
        seen.add(plugin_name)
        unique_plugins.append({
            "Plugin Name": plugin_name,
            "Description": entry.get("Description", ""),
            "Origin Severity": entry.get("Severity", ""),
            "Severity": entry.get("Severity", ""),
            "Domain": entry.get("Domain", ""),
            "Security Module": "CSPM",
            "Cloud Type": cloud,
            "More Info": entry.get("more_info", ""),
            "Enabled": "True",
        })
        added += 1

    print(f"{cloud:8s} — {added} new unique Plugin Names added  (file total: {len(data)} entries)")

out_path = os.path.join(BASE, "unique_plugins.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(unique_plugins, f, indent=2, ensure_ascii=False)

print(f"\nTotal unique plugins : {len(unique_plugins)}")
print(f"Output written to   : {out_path}")
