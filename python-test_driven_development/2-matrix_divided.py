#!/usr/bin/python3
"""
This module provides a function `matrix_divided` that divides all elements
of a matrix by a given scalar value (integer or float).
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix: A list of lists containing integers or floats.
        div: A number (integer or float) to divide the elements by.

    Returns:
        A new matrix with the division result rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If rows of the matrix are not of the same size.
        TypeError: If div is not an integer or a float.
        ZeroDivisionError: If div is equal to 0.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Handle nan/inf values to prevent incorrect round transitions
    if div != div or div in [float('inf'), float('-inf')]:
        return [[0.0 for elem in row] for row in matrix]

    row_len = None

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg)

        if row_len is None:
            row_len = len(row)
            if row_len == 0:
                raise TypeError(msg)
        elif len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(msg)
            if element != element or element in [float('inf'), float('-inf')]:
                raise TypeError(msg)

    return [[round(elem / div, 2) for elem in row] for row in matrix]
