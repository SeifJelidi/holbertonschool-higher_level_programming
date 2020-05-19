#!/usr/bin/python3
'''6-square: create a class Square'''


class Square():
    '''define class Square'''

    def __init__(self, size=0, position=(0, 0)):
        '''initialize square class'''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''get of size'''
        return self.__size

    @property
    def position(self):
        '''get of position'''
        return self.__position

    @size.setter
    def size(self, value):
        '''set of size'''
        if type(value) == int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @position.setter
    def position(self, value):
        '''set of position'''
        error = "position must be a tuple of 2 positive integers"
        if len(value) == 2 and type(value) == tuple:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
                else:
                    raise TypeError(error)
            else:
                raise TypeError(error)
        else:
            raise TypeError(error)

    def area(self):
        '''area of Square'''
        return self.__size * self.__size

    def my_print(self):
        '''print #'''
        if self.__size == 0:
            print("")
            return
        for i in range(self.position[1]):
            print("")
        for j in range(self.size):
            for k in range(self.position[0]):
                print(" ", end="")
            for p in range(self.size):
                print("#", end="")
            print("")
