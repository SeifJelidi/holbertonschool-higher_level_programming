#!/usr/bin/python3
"""___"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)
    and returns the number of characters added"""
    ch = 0
    with open(filename, 'a+', encoding='utf-8') as f:
        ch = f.write(text)
    return ch
