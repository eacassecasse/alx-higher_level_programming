#!/usr/bin/python3
"""A function that adds attributes to an object."""


def add_attribute(obj, att, value):
    """Add a new attribute to obj.

    Args:
        obj (any): The object to add an attribute to.
        att (str): The name of the attribute to add.
        value (any): The value of the attribute.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
