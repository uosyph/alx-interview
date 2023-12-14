#!/usr/bin/python3
"""
"""


def minOperations(n):
    """
    """

    if not isinstance(n, int) or n < 2:
        return 0

    current_factor = 2
    prime_factors_list = []
    remaining_value = n

    while remaining_value != 1:
        if remaining_value % current_factor == 0:
            while remaining_value % current_factor == 0:
                remaining_value //= current_factor
                prime_factors_list.append(current_factor)
        current_factor += 1

    return sum(prime_factors_list)
