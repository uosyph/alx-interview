#!/usr/bin/python3
"""Define function to rotate a 2D matrix."""


def rotate_2d_matrix(matrix):
    """Rotate a 2D matrix in-place.

    Parameters:
        - matrix (list of lists): The 2D matrix to be rotated.
    """
    size = len(matrix)
    rotated_order = []

    # Traverse the matrix in a clockwise direction and store the elements
    for i in range(size):
        for j in range(size - 1, -1, -1):
            rotated_order.append(matrix[j][i])

    # Populate the matrix with the rotated elements
    for i in range(size):
        for j in range(size):
            matrix[i][j] = rotated_order.pop(0)
