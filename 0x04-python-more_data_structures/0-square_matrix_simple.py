#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix[:]
    for arr in matrix:
        new_matrix[len(new_matrix):] = [[i*i for i in arr]]
    return new_matrix
