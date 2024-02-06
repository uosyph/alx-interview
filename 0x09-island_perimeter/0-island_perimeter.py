#!/usr/bin/python3
"""
Function to find the perimeter of the island
"""


def island_perimeter(grid):
    """
    A function that takes a list an returns a perimeter
    """
    perimeter_count = 0
    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    for row in range(rows):
        for col in range(cols):

            neighbors = [
                (row - 1, col),
                (row, col - 1),
                (row, col + 1),
                (row + 1, col)
            ]
            valid_neighbors = [
                1 if k[0] in range(rows) and k[1] in range(cols) else 0
                for k in neighbors
            ]

            if grid[row][col]:
                perimeter_count += sum(
                    [
                        1 if not is_valid or not grid[k[0]][k[1]] else 0
                        for is_valid, k in zip(valid_neighbors, neighbors)
                    ]
                )

    return perimeter_count
