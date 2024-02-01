#!/usr/bin/python3
"""
Implementation of the dynamic programming approach
to find the minimum number of coins needed for change.
"""


def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed to meet a given total amount.


    Parameters:
        - coins (list): A list of coin denominations available.
        - total (int): The total amount for which change needs to be made.

    Returns:
        int: The fewest number of coins needed to meet the total amount.
            If the total is 0 or less, return 0.
            If it's not possible to make exact change, returns -1.
    """
    if total <= 0:
        return 0

    coin_count = 0
    coins = sorted(coins)[::-1]

    for coin in coins:
        while coin <= total:
            total -= coin
            coin_count += 1
        if total == 0:
            return coin_count

    return -1
