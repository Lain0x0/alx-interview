#!/usr/bin/python3
""" 0-operations """


def minOperations(n: int) -> int:
    """ function that do a minimum operations """
    if (n <= 1):
        return (0)
    min_operation = 0
    division = 2
    while (n > 1):
        while (n % division == 0):
            min_operation += division
            n /= division
        division += 1

    return (min_operation)
