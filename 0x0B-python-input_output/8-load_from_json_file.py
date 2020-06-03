#!/usr/bin/python3
"""___"""


def load_from_json_file(filename):
    """creates an Object from a JSON file"""
    import json
    with open(filename, 'r') as fo:
        return json.load(fo)
