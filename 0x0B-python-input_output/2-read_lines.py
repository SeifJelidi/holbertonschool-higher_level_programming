#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """read liness"""
    ligne = 0
    with open(filename, mode="r", encoding='utf-8') as f:
        reading = f.readlines()
        if nb_lines <= 0:
            nb_lines = len(reading)
        for l1 in reading:
            ligne += 1
            if ligne > nb_lines:
                break
            print(l1, end="")
    return ligne
