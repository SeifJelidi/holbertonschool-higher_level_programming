#!/usr/bin/python3
def uppercase(str):
    for x in range(0, len(str)):
        t = ord(str[x])
        if t < 123 and t > 96:
            t = t - 32
        print("{}".format(chr(t)), end="")
    print((""))
