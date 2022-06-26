#!/usr/bin/python3
"""Define a matrix div function."""


def matrix_divided(matrix, div):
    """Divide all items of matrix.
    Args:
        matrix (list): list of items
        div (int or float): divisor
    Raises:
         TypeError: Matrix contains non-numbers.
         TypeError: Matrix contains differents sizes of row.
         TypeError: Div isn't int or float
         TypeError: Div = 0.
    Return:
          New matrix.
    """
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(rw, list) for rw in matrix) or
        not all((isinstance(elt, int) or isinstance(elt, float))
                for elt in [nb for rw in matrix for nb in rw])):
        raise TypeError("matrix must be a matrix(list of lists) of "
                        "integers/floats")

    if not all(len(rw) == len(matrix[0]) for rw in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), rw)) for rw in matrix])
