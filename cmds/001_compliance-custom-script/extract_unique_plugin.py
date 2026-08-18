#!/usr/bin/env python3
"""
Script to read aws_offline_data.json and create a new JSON file with unique
Plugin Name and Description combinations.
"""

import json
import sys
from collections import defaultdict


def read_json_file(file_path):
    """Read and parse the JSON file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in '{file_path}': {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        sys.exit(1)


def create_unique_plugins(data):
    """
    Create a list of unique entries based on Plugin Name and Description.
    Uses a dictionary to track unique combinations and keeps only Plugin Name, Description and more_info.
    """
    unique_entries = {}
    seen_combinations = set()

    for entry in data:
        plugin_name = entry.get("Plugin Name", "")
        description = entry.get("Description", "")
        more_info = entry.get("more_info", "")

        # Create a unique key based on Plugin Name and Description
        combination_key = (plugin_name, description, more_info)

        # Only add if we haven't seen this combination before
        if combination_key not in seen_combinations:
            seen_combinations.add(combination_key)
            # Create simplified entry with only Plugin Name and Description
            simplified_entry = {
                "Plugin Name": plugin_name,
                "Description": description,
                "more_info": more_info,
            }
            unique_entries[combination_key] = simplified_entry

    # Convert back to list format
    return list(unique_entries.values())


def write_json_file(data, output_path):
    """Write data to a JSON file with proper formatting."""
    try:
        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        print(f"Successfully created '{output_path}' with {len(data)} unique entries.")
    except Exception as e:
        print(f"Error writing to '{output_path}': {e}")
        sys.exit(1)


def main():
    """Main function to orchestrate the process."""
    input_file = "/home/ayush/Desktop/accuknox/cspm-backend/tenant/offline_enrichment_data/control_benchmark/oracle_offline_data.json"
    output_file = "unique_oracle_plugins.json"

    print(f"Reading data from '{input_file}'...")
    data = read_json_file(input_file)
    print(f"Loaded {len(data)} total entries.")

    print("Creating unique entries based on Plugin Name and Description...")
    unique_data = create_unique_plugins(data)
    print(f"Found {len(unique_data)} unique Plugin Name + Description combinations.")

    print(f"Writing unique entries to '{output_file}'...")
    write_json_file(unique_data, output_file)

    # Print some statistics
    print(f"\nSummary:")
    print(f"- Original entries: {len(data)}")
    print(f"- Unique entries: {len(unique_data)}")
    print(f"- Duplicates removed: {len(data) - len(unique_data)}")

    # Show a few examples of unique entries
    print(f"\nFirst 3 unique entries:")
    for i, entry in enumerate(unique_data[:3]):
        print(f"{i+1}. Plugin: '{entry.get('Plugin Name', 'N/A')}'")
        print(
            f"   Description: '{entry.get('Description', 'N/A')[:100]}{'...' if len(entry.get('Description', '')) > 100 else ''}'",
        )
        print()


if __name__ == "__main__":
    main()
