#!/usr/bin/python3
"""This module defines say_my_name function"""


def say_my_name(first_name, last_name=""):
    """
    A function that prints a name

    Args:
        first_name (str): The first name to print
        last_name (str): The optional last name to print
    Raises:
        TypeError: If either first name or last name are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print('My name is {} {}'.format(first_name, last_name))
