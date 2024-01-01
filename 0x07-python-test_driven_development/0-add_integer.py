#!/usr/bin/python3
"""This module defines add_integer function"""


def add_integer(a, b=98):
    """
    A function that adds computes the addition of 2 integers

    Args:
        a (int): first number to add
        b (int): second number to add
    Raises:
        TypeError: If either a or b are not integers
    """
    if not type(a) in [int, float]:
        raise TypeError("a must be an integer")
    if not type(b) in [int, float]:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
