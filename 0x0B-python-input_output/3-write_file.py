#!/usr/bin/python3
"""___"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)
    and returns the number of characters written"""
    with open(filename, 'w') as w:
        return w.write(text)
