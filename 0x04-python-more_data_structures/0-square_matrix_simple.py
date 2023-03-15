#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    return list(map(lambda x : [element**2 for element in x], matrix))
