#!/usr/bin/python3
"""This module defines print_square function"""


def print_square(size):
    """
    A function that prints a square matrix with character #.

    Args:
        size (int): The height/width of the matrix
    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(0, size):
        [print("#", end="") for _ in range(size)]
        print("")
