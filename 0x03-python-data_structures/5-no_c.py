#!/usr/bin/python3
def no_c(my_string):
    s = list(my_string)
    for i, j in enumerate(s):
        if j == 'C' or j == 'c':
            del s[i]
    return "".join(s)
