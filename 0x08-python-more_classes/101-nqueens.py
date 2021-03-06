#!/usr/bin/python3
"""Solving the N-queens puzzle
Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.
Example:
    $ ./101-nqueens.py N
Attributes:
    bd (list): list of lists representing the chessboard.
    slts (list): list of lists containing solutions.
"""
import sys


def init_bd(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    bd = []
    [bd.append([]) for i in range(n)]
    [rw.append(' ') for i in range(n) for rw in bd]
    return (bd)


def bd_deepcopy(bd):
    """Return a deepcopy of a chessboard."""
    if isinstance(bd, list):
        return list(map(bd_deepcopy, bd))
    return (bd)


def get_slt(bd):
    """Return the list of lists representation of a solved chessboard."""
    slt = []
    for r in range(len(bd)):
        for c in range(len(bd)):
            if bd[r][c] == "Q":
                slt.append([r, c])
                break
    return (slt)


def xout(bd, rw, col):
    """X out spots on a chessboard.
    All spots where non-attacking queens can no
    longer be played are X-ed out.
    Args:
        bd (list): The current chessboard.
        rw (int): row where a queen was last played.
        col (int): column where a queen was last played.
    """
    # X out all forward spots
    for c in range(col + 1, len(bd)):
        bd[rw][c] = "x"
    # X out all backwards spots
    for c in range(col - 1, -1, -1):
        bd[rw][c] = "x"
    # X out all spots below
    for r in range(rw + 1, len(bd)):
        bd[r][col] = "x"
    # X out all spots above
    for r in range(rw - 1, -1, -1):
        bd[r][col] = "x"
    # X out all spots diagonally down to the right
    c = col + 1
    for r in range(rw + 1, len(bd)):
        if c >= len(bd):
            break
        bd[r][c] = "x"
        c += 1
    # X out all spots diagonally up to the left
    c = col - 1
    for r in range(rw - 1, -1, -1):
        if c < 0:
            break
        bd[r][c]
        c -= 1
    # X out all spots diagonally up to the right
    c = col + 1
    for r in range(rw - 1, -1, -1):
        if c >= len(bd):
            break
        bd[r][c] = "x"
        c += 1
    # X out all spots diagonally down to the left
    c = col - 1
    for r in range(rw + 1, len(bd)):
        if c < 0:
            break
        bd[r][c] = "x"
        c -= 1


def recursive_solve(bd, rw, queens, slts):
    """solve an N-queens puzzle.
    Args:
        bd (list): The current working chessboard.
        rw (int): The current working row.
        queens (int): The current number of placed queens.
        slts (list): A list of lists of solutions.
    Return:
        slt
    """
    if queens == len(bd):
        slts.append(get_slt(bd))
        return (slts)

    for c in range(len(bd)):
        if bd[rw][c] == " ":
            tmp_bd = bd_deepcopy(bd)
            tmp_bd[rw][c] = "Q"
            xout(tmp_bd, rw, c)
            slts = recursive_solve(tmp_bd, rw + 1,
                                   queens + 1, slts)
    return (slts)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    bd = init_bd(int(sys.argv[1]))
    slts = recursive_solve(bd, 0, 0, [])
    for sol in slts:
        print(sol)
