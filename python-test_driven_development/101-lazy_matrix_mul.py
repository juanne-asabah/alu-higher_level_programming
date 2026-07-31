#!/usr/bin/python3
"""
This module provides a function `lazy_matrix_mul` that multiplies two valid
matrices using the NumPy module.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a: First matrix (list of lists of integers or floats).
        m_b: Second matrix (list of lists of integers or floats).

    Returns:
        A new matrix containing the product of m_a and m_b.

    Raises:
        TypeError: If either m_a or m_b is not a list, not a list of lists,
                   contains non-numbers, or has non-uniform row lengths.
        ValueError: If either m_a or m_b is empty, or if they cannot be multiplied.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or any(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or any(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    # Check uniformity against the first row's width
    row_width_a = len(m_a[0])
    if not all(len(row) == row_width_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    row_width_b = len(m_b[0])
    if not all(len(row) == row_width_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Multiplication requires: columns of A (row_width_a) == rows of B (len(m_b))
    if row_width_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return np.matmul(m_a, m_b).tolist()
