#!/usr/bin/python3
def read_file(filename=""):
    """reading file"""
    with open(filename, encoding="UTF-8") as r:
        print(r.read(), end='')
