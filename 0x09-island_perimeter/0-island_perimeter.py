#!/usr/bin/python3
"""Island Perimeter Alx Interview"""


def island_perimeter(grid):
    """Function that sumilate working with 2D-Arrays"""
    perimeter = 0
    for p in range(len(grid)):
        for q in range(len(grid[p])):
            if grid[p][q] == 1:
                perimeter += 4
                if p > 0 and grid[p - 1][q] == 1:
                    perimeter -= 2
                if q > 0 and grid[p][q - 1] == 1:
                    perimeter -= 2
    return perimeter
