#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard.
"""

import sys


def print_queens_solution(board):
    """Prints the solution in a readable format"""
    solution_list = []
    for i, row in enumerate(board):
        value = []
        for j, col in enumerate(row):
            if col == 1:
                value.extend([i, j])
        solution_list.append(value)
    print(solution_list)


def is_valid_queen_placement(board, current_row, current_column, board_size):
    """Checks if placing a queen at a given position is valid"""
    # Check previous columns
    for previous_column in range(current_column):
        if board[current_row][previous_column] == 1:
            return False

    # Check upper diagonal
    for row, column in zip(
        range(current_row, -1, -1), range(current_column, -1, -1)
    ):
        if board[row][column] == 1:
            return False

    # Check lower diagonal
    for row, column in zip(
        range(current_row, board_size, 1), range(current_column, -1, -1)
    ):
        if board[row][column] == 1:
            return False

    return True


def solve_n_queens_util(board, current_column, board_size):
    """Auxiliary method to find the possibilities of the answer."""
    if current_column == board_size:
        print_queens_solution(board)
        return True

    solution_found = False
    for current_row in range(board_size):
        if is_valid_queen_placement(board, current_row,
                                    current_column, board_size):
            board[current_row][current_column] = 1
            solution_found = (solve_n_queens_util(board,
                                                  current_column + 1,
                                                  board_size)
                              or solution_found)

            board[current_row][current_column] = 0

    return solution_found


def solve_n_queens(board_size):
    """Recursive function to solve the N Queens problem"""
    board = [[0 for _ in range(board_size)] for _ in range(board_size)]
    return False if not solve_n_queens_util(board, 0, board_size) else True


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

    solve_n_queens(sys.argv)
