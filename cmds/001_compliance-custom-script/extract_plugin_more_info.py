#!/usr/bin/env python3
"""
Script to extract Plugin Name and more_info fields from azure_offline_data_enriched.json
and create a new JSON file with only these fields.
"""

import json
import sys
from pathlib import Path


def extract_plugin_info(input_file, output_file):
    """
    Extract Plugin Name and more_info fields from the input JSON file
    and write them to a new JSON file.
    """
    try:
        # Read the input file
        print(f"Reading from: {input_file}")
        with open(input_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Extract required fields
        extracted_data = []
        count = 0

        for item in data:
            if isinstance(item, dict):
                extracted_item = {}

                # Extract Plugin Name
                if "Plugin Name" in item:
                    extracted_item["Plugin Name"] = item["Plugin Name"]

                # Extract more_info
                if "more_info" in item:
                    extracted_item["more_info"] = item["more_info"]

                # Only add items that have at least one of the required fields
                if extracted_item:
                    extracted_data.append(extracted_item)
                    count += 1

        # Write to output file
        print(f"Writing {count} items to: {output_file}")
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(extracted_data, f, indent=2, ensure_ascii=False)

        print(f"Successfully extracted data from {len(data)} items")
        print(
            f"Created {len(extracted_data)} items with Plugin Name and/or more_info fields",
        )

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in input file - {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def main():
    # File paths
    input_file = "gcp_offline_data_enriched.json"
    output_file = "gcp_plugin_info_only.json"

    # Check if input file exists
    if not Path(input_file).exists():
        print(f"Error: Input file '{input_file}' not found in current directory.")
        print("Please make sure you're running this script from the correct directory.")
        sys.exit(1)

    # Extract the data
    extract_plugin_info(input_file, output_file)


if __name__ == "__main__":
    main()
