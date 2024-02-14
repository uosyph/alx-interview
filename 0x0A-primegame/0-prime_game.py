#!/usr/bin/python3
"""
Module to determine the winner of a prime game.
"""


def is_prime(number):
    """
    Checks if a number is prime.
    """
    for divisor in range(2, int(number**0.5) + 1):
        if not number % divisor:
            return False
    return True


def calculate_primes(up_to_number, primes):
    """
    Calculate all prime numbers up to a given number.
    """
    highest_prime = primes[-1]
    if up_to_number > highest_prime:
        for num in range(highest_prime + 1, up_to_number + 1):
            primes.append(num) if is_prime(num) else primes.append(0)


def isWinner(x, nums):
    """
    Determine the winner of a prime game.
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
