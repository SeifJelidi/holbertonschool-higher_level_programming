#!/usr/bin/python3
"""
add_integer :the sum of two integers
a: int
b: int (89 in default)
"""


def add_integer(a, b=98):
    """
        Adding of a and b
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")

    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
