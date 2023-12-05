#!/usr/bin/python3
"""A function that checks an object class."""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a_class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class to match the type of obj.
    Returns:
        True - If obj is instance of a_class.
        False - Otherwise.
    """
    if type(obj) == a_class:
        return True
    return False
