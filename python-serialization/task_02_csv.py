#!/usr/bin/python3
"""
"""
import csv
import json


def convert_csv_to_json(filename):
    try:
        with open(filename, "r", encoding="UTF-8") as f:
#            csv_reader = csv.reader(f)
            dictionary = csv.DictReader(f)
            for row in dictionary:
                write(json.dumps(row))
            return True
    except (FileNotFoundError, EOFError):
        return False


if __name__ == '__main__':
    csv_file = "data.csv"
    convert_csv_to_json(csv_file)
    print(f"Data from {csv_file} has been converted to data.json")