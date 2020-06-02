#!/usr/bin/python3
'''returns true or famse'''


def is_same_class(obj, a_class):
    '''if the object is exactly an instance of the specified class return True
     ,otherwise return False'''
    if type(obj) == a_class:
        return True
    else:
        return False
