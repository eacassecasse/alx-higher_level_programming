#!/usr/bin/python3
"""This module defines matrix_divided function"""


def matrix_divided(matrix, div):
    """
    A function that divides all elements of a matrix.

    Args:
        matrix (list): A list of integers or floats
        div (int/float): The divisor value
    Raises:
        TypeError: If the matrix is empty or doesn't contain integers/floats
        TypeError: If the matrix rows are not list
        TypeError: If div is not a number
        ZeroDivisionError: If div is 0
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(type(el) in [int, float] for row in matrix for el in row)):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    if type(div) not in [int, float]:
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    return ([list(map(lambda el: round(el / div, 2), row)) for row in matrix])
