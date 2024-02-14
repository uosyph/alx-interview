#!/usr/bin/python3
"""
Module to determine the winner of a prime game.
"""


def is_prime(number):
    for divisor in range(2, int(number**0.5) + 1):
        if not number % divisor:
            return False
    return True


def calculate_primes(up_to_number, primes):
    highest_prime = primes[-1]
    if up_to_number > highest_prime:
        for num in range(highest_prime + 1, up_to_number + 1):
            primes.append(num) if is_prime(num) else primes.append(0)


def isWinner(x, nums):
    ...
