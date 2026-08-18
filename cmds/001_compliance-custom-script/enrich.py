import json

# File paths
json1_path = "/home/ayush/Desktop/accuknox/cspm-backend/tenant/offline_enrichment_data/control_benchmark/oracle_offline_data.json"
json2_path = "soc.json"
output_path = "ouptut_filled.json"

# Fields to copy from json1 to json2
fields_to_copy = [
    "Description",
    # "Severity",
    "Recommended Action",
    "Link",
    "Domain",
    "Tags",
    "Remediation Steps",
    "more_info",
]

# Load json1 and json2 (lists of dictionaries)
with open(json1_path, "r") as f1:
    json1_data = json.load(f1)

with open(json2_path, "r") as f2:
    json2_data = json.load(f2)

# Build lookup dictionary from json1 using Plugin Name
plugin_lookup = {item["Plugin Name"]: item for item in json1_data}

# Update json2 using plugin name match
for entry in json2_data:
    plugin_name = entry.get("Plugin Name")
    if plugin_name in plugin_lookup:
        source = plugin_lookup[plugin_name]
        for field in fields_to_copy:
            entry[field] = source.get(field, "")

# Save updated json2
with open(output_path, "w") as f_out:
    json.dump(json2_data, f_out, indent=4)

print(f"Updated json2 written to: {output_path}")
