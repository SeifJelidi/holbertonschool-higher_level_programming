#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        sum = 0
        for x in my_list:
            for i in x:
                sum = sum + i
    res = sum / len(my_list)
    return res
