#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """Return a list represent a Pascal's triangle of n number"""
    if n <= 0:
        return []

    pascal_triangle = [[1]]
    for k in range(1, n):
        list = [1]
        for j in range(1, k):
            list.append(pascal_triangle[-1][j - 1] + pascal_triangle[-1][j])
        list.append(1)
        pascal_triangle.append(list)
    return pascal_triangle

