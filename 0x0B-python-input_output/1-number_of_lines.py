#!/usr/bin/python3
'''___'''


def number_of_lines(filename=""):
    """number of lines"""
    ligne = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for l1 in f:
            ligne += 1
    return ligne
