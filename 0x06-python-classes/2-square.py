#!/usr/bin/python3
'''2-square: create a class Square'''


class Square:
    '''define class Square'''
    def __init__(self, size=0):
        '''initialize square class'''
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
