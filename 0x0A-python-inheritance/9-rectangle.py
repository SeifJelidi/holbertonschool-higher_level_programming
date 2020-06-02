#!/usr/bin/python3
'''new empty class'''


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    ''' rectangle class'''
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        '''the area of the rectangle'''
        return self.__width * self.__height

    def __str__(self):
        '''___'''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
