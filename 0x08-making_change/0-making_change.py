#!/usr/bin/python3
""" 0. piles coins chanllenge """


def makeChange(coins, total):
    """Return the fewest number of coins |
    return -1 if Impossible"""
    if total <= 0:
        return 0

    # using sort function to sort coins
    coins.sort(reverse=True)
    num_coins = 0

    for coin in coins:
        if total <= 0:
            break


        num_coins += total // coin
        total %= coin

    return num_coins if total == 0 else -1
