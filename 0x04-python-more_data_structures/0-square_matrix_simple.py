#!/usr/bin/python3
"""Computes the square value of all integers of a matrix"""
def square_matrix_simple(matrix=[]):
    return ([list(map(lambda a: a * a, r)) for r in matrix])
