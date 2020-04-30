#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    s = 0
    for i, j in enumerate(argv):
        if i != 0:
            s += int(j)
    print("{}".format(s))
