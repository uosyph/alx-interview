#!/usr/bin/python3
"""
Determines if a list of integers represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Check whether the given list of integers represents a valid UTF-8 encoding.

    Args:
        data (list of int): List of integers to check.

    Returns:
        bool: True if the list is a valid UTF-8 encoding, False otherwise.
    """

    start_of_utf8 = 1 << 7  # 10000000
    continuation_byte = 1 << 6  # 01000000

    num_bytes_to_follow = 0

    if not data or len(data) == 0:
        return True

    for num in data:
        current_bit = 1 << 7

        # Determine the number of bytes in the UTF-8 character
        if num_bytes_to_follow == 0:
            while current_bit & num:
                num_bytes_to_follow += 1
                current_bit = current_bit >> 1

            if num_bytes_to_follow == 0:
                continue
            if num_bytes_to_follow == 1 or num_bytes_to_follow > 4:
                return False
        else:
            # Check if the current byte follows the UTF-8 encoding rules
            if not (num & start_of_utf8 and not (num & continuation_byte)):
                return False
        num_bytes_to_follow -= 1

    return False if num_bytes_to_follow else True
