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

    infinite = total + 1
    coin_count = {0: 0}

    for current_total in range(1, total + 1):
        coin_count[current_total] = infinite

        for coin_value in coins:
            remaining_total = current_total - coin_value
            if remaining_total < 0:
                continue

            coin_count[current_total] = min(coin_count[remaining_total] + 1,
                                            coin_count[current_total])

    if coin_count[total] == total + 1:
        return -1

    return coin_count[total]
