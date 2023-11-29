#!/usr/bin/python3
"""Generate Pascal's Triangle with specified number of rows."""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle with the specified number of rows.

    Args:
        n (int): Number of rows to generate.

    Returns:
        list of lists: Pascal's Triangle as a list of lists.
    """

    pascal_list = []

    if n <= 0:
        return pascal_list

    for _ in range(n):
        row = [1]
        if pascal_list:
            last_row = pascal_list[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        pascal_list.append(row)

    return pascal_list
