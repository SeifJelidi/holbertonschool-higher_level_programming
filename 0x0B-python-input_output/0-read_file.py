#!/usr/bin/python3
'''____'''


def read_file(filename=""):
    """reading file"""
    with open(filename, encoding="UTF-8") as r:
        print(r.read(), end='')
