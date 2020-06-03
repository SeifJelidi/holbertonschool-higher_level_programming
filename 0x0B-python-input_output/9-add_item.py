#!/usr/bin/python3
"""___"""


import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


filename = 'add_item.json'
L = []

try:
    L = load_from_json_file("add_item.json")
    for argument in sys.argv[1:]:
        L.append(argument)
    save_to_json_file(L, filename)
except:
    save_to_json_file(L, filename)
