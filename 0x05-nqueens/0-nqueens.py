#!/usr/bin/python3
"""
N-Queens Solver

The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard.

Usage: nqueens N

N must be an integer greater than or equal to 4.
"""

import sys


def print_queens_solution(board):
    """
    Prints the solution in a readable format.

    Parameters:
        board (list): The chessboard representation with queen placements.
    """
    queens_positions = [(row, board[row].index(1))
                        for row in range(len(board))]
    print(queens_positions)


def is_valid_queen_placement(board, current_column, current_row, board_size):
    """
    Checks if placing a queen at a given position is valid.

    Parameters:
        - board (list): The chessboard representation with queen placements.
        - current_column (int): The current column being considered
                                for queen placement.
        - current_row (int): The current row being considered
                             for queen placement.
        - board_size (int): The size of the chessboard.

    Returns:
        bool: True if queen placement is valid, False otherwise.
    """
    # Check previous columns
    for previous_column in range(current_column):
        if board[current_row][previous_column] == 1:
            return False

    # Check upper diagonal
    row, column = current_row, current_column
    while row >= 0 and column >= 0:
        if board[row][column] == 1:
            return False
        row -= 1
        column -= 1

    # Check lower diagonal
    row, column = current_row, current_column
    while row < board_size and column >= 0:
        if board[row][column] == 1:
            return False
        row += 1
        column -= 1

    return True


def solve_n_queens(board, current_column, board_size):
    """
    Recursive function to solve the N Queens problem.

    Parameters:
        - board (list): The chessboard representation with queen placements.
        - current_column (int): The current column being considered
                                for queen placement.
        - board_size (int): The size of the chessboard.

    Returns:
        bool: True if a solution is found, False otherwise.
    """
    if current_column == board_size:
        print_queens_solution(board)
        return True

    solution_found = False
    for current_row in range(board_size):
        if is_valid_queen_placement(board, current_column,
                                    current_row, board_size):
            board[current_row][current_column] = 1
            solution_found = (
                solve_n_queens(board, current_column + 1, board_size)
                or solution_found
            )
            board[current_row][current_column] = 0

    return solution_found


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        board_size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)

    chess_board = [[0] * board_size for _ in range(board_size)]
    solve_n_queens(chess_board, 0, board_size)
