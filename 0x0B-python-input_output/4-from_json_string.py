#!/usr/bin/python3
"""A function that deserializes an object."""
import json


def from_json_string(my_str):
    """Deserializes an object from JSON."""
    return (json.loads(my_str))