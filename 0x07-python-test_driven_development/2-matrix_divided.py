#!/usr/bin/python3
"""
Module 2-matrix_divided: divides all elements of a matrix.
matrix must be a matrix (list of lists) of integers/floats else raise TypeError
Each row of the matrix must have the same size
div must be a number (int or float) and can't be equal to 0.
"""


def matrix_divided(matrix, div):
    """ Method matrix_divided: divides all elements of a matrix
    Args:
        matrix (list): The matrix to divide.
        div (int/float): The divisor value.
    Returns: A new matrix contains the results of division.
    """
    if (type(matrix) is not list) or matrix == [] or \
            not all(isinstance(row, list) for row in matrix) or \
            not all((type(x) in [int, float])
                    for x in [num for row in matrix for num in row]):
        raise TypeError("matrix must be a matrix (list of lists) of")\
                        + (" integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
