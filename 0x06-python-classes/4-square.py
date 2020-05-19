#!/usr/bin/python3
'''4-square: create a class Square'''


class Square:
    '''define class Square'''
    def __init__(self, size=0):
        '''initialize square class'''
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        '''get of size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''set of size'''
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''area of square'''
        return self.__size * self.__size
