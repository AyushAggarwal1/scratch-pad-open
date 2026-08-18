#!/usr/bin/env python3
"""
Script to convert CSV file to XLSX format
"""

import sys
from pathlib import Path

import pandas as pd


def convert_csv_to_xlsx(csv_file_path, xlsx_file_path):
    """
    Convert CSV file to XLSX format using pandas
    """
    try:
        # Read CSV file
        print(f"Reading CSV file: {csv_file_path}")
        df = pd.read_csv(csv_file_path)

        print(f"Data shape: {df.shape}")
        print(f"Columns: {list(df.columns)}")

        # Write to XLSX file
        print(f"Writing to XLSX file: {xlsx_file_path}")
        df.to_excel(xlsx_file_path, index=False, engine="openpyxl")

        print(f"Successfully converted {csv_file_path} to {xlsx_file_path}")
        print(f"Total records: {len(df)}")
        print(f"Total columns: {len(df.columns)}")

    except FileNotFoundError:
        print(f"Error: File {csv_file_path} not found")
    except Exception as e:
        print(f"Error: {e}")


def main():
    # Define file paths
    csv_file = "/home/ayush/Desktop/accuknox/cspm-backend/local-scripts/general-scripts/compliance-enrichment-scripts/qwe.csv"
    xlsx_file = "/home/ayush/Desktop/accuknox/cspm-backend/local-scripts/general-scripts/compliance-enrichment-scriptsoci_dpdp.xlsx"

    # Convert CSV to XLSX
    convert_csv_to_xlsx(csv_file, xlsx_file)


if __name__ == "__main__":
    main()
