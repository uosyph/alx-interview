#!/usr/bin/python3
"""
Module to determine the winner of a prime game.

This module provides functions to check if a number is prime,
calculate prime numbers up to a given number,
and determine the winner of a prime game based on a series of rounds.
"""


def is_prime(number):
    """
    Checks if a number is prime.

    Args:
        number (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    for divisor in range(2, int(number**0.5) + 1):
        if not number % divisor:
            return False
    return True


def calculate_primes(up_to_number, primes):
    """
    Calculate all prime numbers up to a given number.

    Args:
        up_to_number (int): The number up to which to calculate primes.
        primes (list): A list containing prime numbers.

    Returns:
        None
    """
    highest_prime = primes[-1]
    if up_to_number > highest_prime:
        for num in range(highest_prime + 1, up_to_number + 1):
            primes.append(num) if is_prime(num) else primes.append(0)


def isWinner(x, nums):
    """
    Determine the winner of a prime game.

    Args:
        x (int): The number of rounds to play.
        nums (list): An array of integers representing
        the numbers for each round.

    Returns:
        str or None: The name of the player that won the most rounds.
                     If the winner cannot be determined, returns None.
    """
    players_wins = {"Maria": 0, "Ben": 0}
    primes = [0, 0, 2]

    calculate_primes(max(nums), primes)

    for round_num in range(x):
        sum_options = sum(
            (i != 0 and i <= nums[round_num])
            for i in primes[: nums[round_num] + 1]
        )
        players_wins["Maria" if sum_options % 2 else "Ben"] += 1

    if players_wins["Ben"] < players_wins["Maria"]:
        return "Maria"
    elif players_wins["Ben"] > players_wins["Maria"]:
        return "Ben"

    return None
