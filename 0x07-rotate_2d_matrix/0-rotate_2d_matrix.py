#!/usr/bin/python3
"""Alx-Interview: Rotate_2D Matrix"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix"""
    n = len(matrix)

    for x in range(n):
        for y in range(x + 1, n):
            matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

    for i in range(n):
        matrix[i].reverse()
