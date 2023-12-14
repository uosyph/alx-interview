#!/usr/bin/python3
"""
Calculate the minimum number of operations required to transform a given
positive integer 'n' into 1. An operation can be either dividing the number
by its smallest prime factor or incrementing the number.

Parameters:
- n (int): The positive integer to be transformed.

Returns:
int: The minimum number of operations required to transform 'n' into 1.

Note:
- If 'n' is not a positive integer or less than 2, the function returns 0.
- Uses prime factorization to find the smallest prime factors of 'n'.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations required to
    transform a given positive integer 'n' into 1.

    Parameters:
    - n (int): The positive integer to be transformed.

    Returns:
    int: The minimum number of operations required to transform 'n' into 1.
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
