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

    def my_print(self):
        '''print #'''
        if self.__size > 0:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print("")
        else:
            print("")
