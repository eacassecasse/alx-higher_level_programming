#!/usr/bin/python3
"""This module defines a function that converts object to JSON."""


def class_to_json(obj):
    """Return the representation of a simple data structure in JSON."""
    return obj.__dict__
