#!/usr/bin/python3
"""A function that read a files content."""
import json


def load_from_json_file(filename):
    """Builds an object from JSON file."""
    with open(file=filename, mode="r", encoding="UTF-8") as fr:
        return json.load(fr)
