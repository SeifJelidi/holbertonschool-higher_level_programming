#!/usr/bin/python3
'''creation of the new class(rectangle)'''


class Rectangle:
    '''width and height of the class'''
    number_of_instances = 0

    def __init__(self, width, height):
        '''/'''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''the widht of the the rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is int:
            if value >= 0:
                self.__width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is int:
            if value >= 0:
                self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        '''Area of rectangle (h * w)'''
        return self.__height * self.__width

    def perimeter(self):
        '''the perimeter of the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__height * 2 + self.__width * 2

    def __str__(self):
        '''prints the rectangle with #'''
        strrect = ""
        hashh = "#"
        if self.__width is 0 or self.__height is 0:
            return strrect
        else:
            seiif = strrect.join(hashh * self.width + '\n') * self.height
            return seiif[:-1]

    def __repr__(self):
        myw = str(self.width)
        myh = str(self.height)
        return "Rectangle" + "(" + myw + ", " + myh + ")"

    def __del__(self):
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''returns the biggest rectangle based on the area'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif int(rect_1.area()) >= int(rect_2.area()):
            return rect_1
        elif int(rect_1.area()) < int(rect_2.area()):
            return rect_2
