#!/usr/bin/python3
'''Rectangle (child class from base)'''


from models.base import Base


class Rectangle(Base):
    '''Rectangle (child class from base)'''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''Get of width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Set of width'''
        if type(value) is int and value > 0:
            self.__width = value
        elif type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        '''Get of height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Set of height'''
        if type(value) is int and value > 0:
            self.__height = value
        elif type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        '''Get of x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Set of x'''
        if type(value) is int and value >= 0:
            self.__x = value
        elif type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        '''Get of y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Set of y'''
        if type(value) is int and value >= 0:
            self.__y = value
        elif type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        '''Area of rectangle'''
        return self.__width * self.__height

    def display(self):
        '''Display #0'''
        if (self.area() == 0):
            print('')
            return
        for this_y in range(0, self.__y):
            print('')
        for j in range(0, self.__height):
            for i in range(0, self.__x):
                print(' ', end='')
            for k in range(0, self.__width):
                print('#', end='')
            print('')

    def __str__(self):
        '''Custom str'''
        i = self.id
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.__height
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(i, x, y, w, h))

    def update(self, *args, **kwargs):
        '''assigns an argument to each attribute'''
        if args is not None and args != ():
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.id = args[0]
                self.__width = args[1]
            if len(args) == 3:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
            if len(args) == 4:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
            if len(args) == 5:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''returns a dictionary representaton of a Rectangle'''
        return {'x': self.__x, 'y': self.__y, 'id': self.id,
                'height': self.__height, 'width': self.__width}
