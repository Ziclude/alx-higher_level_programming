#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return ([list(map(lambda a: a * a, r)) for r in matrix])
