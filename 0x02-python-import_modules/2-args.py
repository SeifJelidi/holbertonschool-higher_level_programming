#!/usr/bin/python3
import sys
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("{:d} arguments.".format(len(argv) - 1))
    else:
        if len(argv) == 2:
            ch = " argument:"
        else:
            ch = " arguments:"
        print("{}".format(len(argv) - 1) + ch)
        for i, j in enumerate(argv):
            if i != 0:
                print("{}: {}".format(i, j))
