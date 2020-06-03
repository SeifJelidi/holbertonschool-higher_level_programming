#!/usr/bin/python3
"""___"""


class Student():
    """Student Class"""

    def __init__(self, first_name, last_name, age):
        """initialize Student attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        if hasattr(self, '__dict__'):
            return self.__dict__
        if hasattr(self, '__slots__'):
            return self.__slots__
