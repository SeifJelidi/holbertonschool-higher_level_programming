#!/usr/bin/python3
def read_file(filename=""):
    """reading file"""
    with open(filename, mode="r", encoding='utf-8') as f:
        reading = f.read()
    print(reading, end='')
