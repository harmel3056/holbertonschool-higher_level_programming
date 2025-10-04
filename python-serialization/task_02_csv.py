#!/usr/bin/python3
"""
Converts CSV format to JSON using DictReader
"""
import csv
import json


def convert_csv_to_json(filename):
    """
    Converting CSV format to JSON using DictReader

    Args:
    filename - name of the file to run conversion on

    Return:
    True if conversion is successful, False if exception raised
    """
    try:
        with open(filename, "r", encoding="UTF-8") as infile:
            dictionary = csv.DictReader(infile)
            with open("data.json", "w") as outfile:
                for row in dictionary:
                        outfile.write(json.dumps(row))
            return True
    except Exception:
        return False


if __name__ == '__main__':
    csv_file = "data.csv"
    convert_csv_to_json(csv_file)
    print(f"Data from {csv_file} has been converted to data.json")
