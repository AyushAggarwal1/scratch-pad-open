import json

import pandas as pd


def convert_xlsx_to_json(xlsx_path, output_json_path, program_name="ISO 27001 - 2022"):
    df = pd.read_excel(xlsx_path)
    json_data = []

    for _, row in df.iterrows():
        # control_name = str(row[0]) + " " + str(row[1])
        control_name = str(row[1])
        control_description = row[2]
        plugins = str(row[3]).splitlines() if pd.notna(row[3]) else []

        for plugin in plugins:
            plugin = plugin.strip()
            if not plugin:
                continue
            entry = {
                "Program Name": program_name,
                "Control Name": control_name,
                "Control Description": control_description,
                "Plugin Name": plugin,
                "Description": "",
                "Severity": "",
                "Recommended Action": "",
                "Link": "",
                "Domain": "",
                "Tags": [""],
                "Remediation Steps": "",
                "more_info": "",
            }
            json_data.append(entry)

    with open(output_json_path, "w") as f:
        json.dump(json_data, f, indent=4)

    print(f"✅ JSON saved to: {output_json_path}")


# Example usage
convert_xlsx_to_json("aws_iso_xlsx.xlsx", "aws_iso.json")
