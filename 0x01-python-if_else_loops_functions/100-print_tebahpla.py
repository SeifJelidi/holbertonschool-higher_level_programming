#!/usr/bin/python3
for i in range(90, 64, -2):
    print("{:c}{:c}".format((i + 32), (i - 1)), end="")
