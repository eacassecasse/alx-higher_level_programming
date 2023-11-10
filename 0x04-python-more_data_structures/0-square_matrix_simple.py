#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    nmat = []
    for col in matrix:
        result = [x**2 for x in col]
        nmat.append(result)
    return nmat
