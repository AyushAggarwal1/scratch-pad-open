#!/usr/bin/env python3
"""
Script to extract all unique control names from ISO 27001 - 2022 in the AWS offline data JSON file.
"""

import json
import sys
from collections import OrderedDict


def extract_iso27001_controls(json_file_path):
    """
    Extract all unique control names from ISO 27001 - 2022 entries in the JSON file.

    Args:
        json_file_path (str): Path to the JSON file containing the data

    Returns:
        list: List of unique control names from ISO 27001 - 2022
    """
    try:
        # Read the JSON file
        with open(json_file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Extract control names for ISO 27001 - 2022
        iso27001_2022_controls = set()

        for entry in data:
            if entry.get("Program Name") == "ISO 27001 - 2022":
                control_name = entry.get("Control Name", "").strip()
                if control_name:  # Only add non-empty control names
                    iso27001_2022_controls.add(control_name)

        # Convert to sorted list for consistent output
        unique_controls = sorted(list(iso27001_2022_controls))

        return unique_controls

    except FileNotFoundError:
        print(f"Error: File '{json_file_path}' not found.")
        return []
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in file '{json_file_path}': {e}")
        return []
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
        return []


def main():
    """Main function to run the script."""
    # Path to the JSON file
    json_file_path = "/home/ayush/Desktop/accuknox/cspm-backend/tenant/offline_enrichment_data/control_benchmark/aws_offline_data.json"

    print("Extracting unique control names from ISO 27001 - 2022...")
    print("=" * 60)

    # Extract the control names
    unique_controls = extract_iso27001_controls(json_file_path)

    if unique_controls:
        print(
            f"Found {len(unique_controls)} unique control names from ISO 27001 - 2022:",
        )
        print()

        # Display the control names
        for i, control_name in enumerate(unique_controls, 1):
            print(f"{i:3d}. {control_name}")

        # Save to a text file
        output_file = (
            "/home/ayush/Desktop/accuknox/cspm-backend/iso27001_2022_controls.txt"
        )
        try:
            with open(output_file, "w", encoding="utf-8") as f:
                f.write("ISO 27001 - 2022 Control Names\n")
                f.write("=" * 40 + "\n\n")
                for i, control_name in enumerate(unique_controls, 1):
                    f.write(f"{i:3d}. {control_name}\n")

            print(f"\nControl names saved to: {output_file}")

        except Exception as e:
            print(f"Error saving to file: {e}")

    else:
        print("No control names found for ISO 27001 - 2022.")
        print(
            "Please check if the data contains entries with 'Program Name': 'ISO 27001 - 2022'",
        )


if __name__ == "__main__":
    main()
