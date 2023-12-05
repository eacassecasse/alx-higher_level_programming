#!/usr/bin/python3
"""A lookup function for object attributes."""


def lookup(obj):
    """A list of available attributes on an object."""
    return (dir(obj))
