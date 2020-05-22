#!/usr/bin/python3
"""
print_square: print a square with the character (#)
"""


def print_square(size):
    """
        print a square with the character (#)
    """
    if isinstance(size, int) is False and isinstance(size, float) is False:
        raise TypeError("size must be an integer")
    if isinstance(size, float) is True and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, (size)):
        for j in range(0, (size)):
            print("#", end="")
        print("")
