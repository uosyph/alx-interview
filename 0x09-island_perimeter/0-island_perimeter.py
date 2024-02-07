#!/usr/bin/python3
"""
This module provides a function to calculate
the perimeter of an island represented by a grid.

The island is represented as a 2D grid where 1s represent land and 0s
represent water. The perimeter of the island is defined as the total length
of the boundary between land and water.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island based on the provided grid.

    Args:
        grid (List[List[int]]): A 2D grid representing the island
        where 1s represent land and 0s represent water.

    Returns:
        int: The perimeter of the island.
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
