#!/usr/bin/python3
"""This module defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Creates a Pascal Triangle

    Args:
        n: size of the Pascal Triangle

    Returns:
        A list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    while len(triangle) != n:
        tri = triangle[-1]
        aux = [1]
        for i in range(len(tri) - 1):
            aux.append(tri[i] + tri[i + 1])
        aux.append(1)
        triangle.append(aux)
    return triangle
