#!/usr/bin/python3
"""A function that checks for inherited classes."""


def inherits_from(obj, a_class):
    """Checks if obj is an inherited instance of a_class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class to match the type of obj.
    Returns:
        True - If obj is inherited instance of a_class.
        False - Otherwise.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
