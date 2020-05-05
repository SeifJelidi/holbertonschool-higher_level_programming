#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return(None)
    x = my_list[0]
    for y in my_list:
        if x < y:
            x = y
    return x
