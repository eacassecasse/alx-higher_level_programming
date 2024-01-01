#!/usr/bin/python3
"""A function that write a files content."""
import json


def save_to_json_file(my_obj, filename):
    """Write JSON string inside a file."""
    with open(file=filename, mode="w", encoding="UTF-8") as fw:
        fw.write(json.dumps(my_obj))
