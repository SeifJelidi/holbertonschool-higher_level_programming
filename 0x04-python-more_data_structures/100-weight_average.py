#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) is 0:
        return 0
    else:
        result1 = reduce((lambda x, y: x * y), my_list)
        return result1
