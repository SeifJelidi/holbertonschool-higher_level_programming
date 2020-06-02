#!/usr/bin/python3
'''__inheritance__'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''child Class from the rectangle class'''
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        '''return area'''
        return self.__size * self.__size
    def __str__(self):
        '''___'''
        return "[Square] {}/{}".format(self.__size, self.__size)
