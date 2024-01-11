#!/usr/bin/python3
"""
N-Queens Solver

The N-Queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard.

Usage: ./0-nqueens.py <N>
    Where N must be an integer greater or equal to 4.

Returns:
    Every possible solution to the problem.
    One solution per line.
    Solutions are not printed in a specific order.
"""

from sys import argv


def is_valid_queen_placement(board, current_row, current_column):
    """
    Checks if placing a queen at a given position is valid.

    Parameters:
        - board (list): The chessboard representation with queen placements.
        - current_column (int): The current column being considered
                                for queen placement.
        - current_row (int): The current row being considered
                             for queen placement.

    Returns:
        bool: True if queen placement is valid, False otherwise.
    """

    # Check the column
    if board[current_row][current_column]:
        return False

    for row in range(current_row):
        if board[row][current_column]:
            return False

    # Check upper-left diagonal
    row, column = current_row, current_column
    while row > 0 and column > 0:
        row -= 1
        column -= 1
        if board[row][column]:
            return False

    # Check upper-right diagonal
    row, column = current_row, current_column
    while row > 0 and column < len(board) - 1:
        row -= 1
        column += 1
        if board[row][column]:
            return False

    return True


def initialize_board(n):
    """
    Initializes an empty chessboard of size N.

    Parameters:
        n (int): The size of the chessboard.

    Returns:
        list: The initialized chessboard.
    """

    return [[0] * n for _ in range(n)]


def solve_nqueens(board, row):
    """
    Recursively solves the N-Queens puzzle.

    Parameters:
        board (list): The chessboard.
        row (int): The current row to consider.

    Returns:
        None
    """

    for column in range(len(board)):
        if is_valid_queen_placement(board, row, column):
            board[row][column] = 1

            if row == len(board) - 1:
                print(format_solution(board))
                board[row][column] = 0
                continue
            elif solve_nqueens(board, row + 1):
                return board
            else:
                board[row][column] = 0


def format_solution(board):
    """
    Formats the solution as a list of queen positions.

    Parameters:
        board (list): The chessboard with queens placed.

    Returns:
        list: The list of queen positions.
    """

    solution = []

    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column]:
                solution.append([row, column])
    return solution


def nqueens_solver(n):
    """
    Solves the N-Queens puzzle for a given board size.

    Parameters:
        n (int): The size of the chessboard.

    Returns:
        None
    """

    for column in range(n):
        board = initialize_board(n)
        board[0][column] = 1
        solve_nqueens(board, 1)


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(argv[1])
        if n < 4:
            print("N must be at least 4")
            exit(1)
    except ValueError:
        print("N must be a number")
        exit(1)

    nqueens_solver(n)
