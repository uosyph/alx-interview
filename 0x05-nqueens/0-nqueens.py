#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard.
"""

import sys


def print_queens_solution(board):
    """Prints the solution in a readable format"""
    queens_positions = [(row, board[row].index(1)) for row in range(len(board))]
    print(queens_positions)


def solve_n_queens(board, current_column, board_size):
    """Recursive function to solve the N Queens problem"""
    if current_column == board_size:
        print_queens_solution(board)
        return True


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
