#!/usr/bin/python3
def read_file(filename=""):
    """reading file"""
    with open(filename) as r:
        print(r.read(), end='')
