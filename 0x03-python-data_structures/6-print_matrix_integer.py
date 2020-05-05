#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in range(len(matrix)):
            s = 0
            for j in range(len(matrix[i])):
                print("{:d}".format(matrix[i][j]), end='')
                s = s + 1
                if s != len(matrix[i]):
                    print(" ", end='')
            print()
