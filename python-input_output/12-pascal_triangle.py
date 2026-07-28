#!/usr/bin/python3
"""Defines a Pascal's Triangle generation matrix structure utility."""


def pascal_triangle(n):
    """Generates an explicit list of integer lists outlining Pascal's Triangle.

    Args:
        n (int): The upper layer boundary row count to calculate.

    Returns:
        list: A nested matrix profile representation of the triangle layout.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) < n:
        last_row = triangle[-1]
        next_row = [1]
        for i in range(len(last_row) - 1):
            next_row.append(last_row[i] + last_row[i + 1])
        next_row.append(1)
        triangle.append(next_row)

    return triangle
