#!/usr/bin/env python3
"""
Script to convert JSON file to CSV format
Handles the specific structure of the Untitled-1.json file
"""

import csv
import json
import sys
from pathlib import Path


def convert_json_to_csv(json_file_path, csv_file_path):
    """
    Convert JSON array of objects to CSV format
    Handles special fields like Tags array by converting to comma-separated string
    """
    try:
        # Read JSON file
        with open(json_file_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        if not data:
            print("No data found in JSON file")
            return

        # Get all unique keys from all objects
        all_keys = set()
        for item in data:
            all_keys.update(item.keys())

        # Convert to list and sort for consistent column order
        fieldnames = sorted(list(all_keys))

        # Write to CSV
        with open(csv_file_path, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # Write header
            writer.writeheader()

            # Write data rows
            for item in data:
                # Convert Tags array to comma-separated string if it exists
                if "Tags" in item and isinstance(item["Tags"], list):
                    item["Tags"] = ", ".join(item["Tags"])

                # Handle any other list fields by converting to string
                for key, value in item.items():
                    if isinstance(value, list):
                        item[key] = ", ".join(str(v) for v in value)
                    elif value is None:
                        item[key] = ""

                writer.writerow(item)

        print(f"Successfully converted {json_file_path} to {csv_file_path}")
        print(f"Total records: {len(data)}")
        print(f"Columns: {', '.join(fieldnames)}")

    except FileNotFoundError:
        print(f"Error: File {json_file_path} not found")
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format - {e}")
    except Exception as e:
        print(f"Error: {e}")


def main():
    # Define file paths
    json_file = "/home/ayush/Desktop/accuknox/cspm-backend/tenant/offline_enrichment_data/control_benchmark/Untitled-1.json"
    csv_file = "/home/ayush/Desktop/accuknox/cspm-backend/tenant/offline_enrichment_data/control_benchmark/Untitled-1.csv"

    # Convert JSON to CSV
    convert_json_to_csv(json_file, csv_file)


if __name__ == "__main__":
    main()
