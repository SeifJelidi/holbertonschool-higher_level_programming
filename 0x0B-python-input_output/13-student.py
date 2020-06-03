#!/usr/bin/python3
"""___"""


class Student():
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """initialize Student attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            if hasattr(self, '__dict__'):
                return self.__dict__
            if hasattr(self, '__slots__'):
                return self.__slots__

        if attrs is not None and isinstance(attrs, list) is False:
            if hasattr(self, '__dict__'):
                return self.__dict__
            if hasattr(self, '__slots__'):
                return self.__slots__

        if attrs is not None:
            if all(isinstance(item, str) for item in attrs):
                a = {}
                for i, value in self.__dict__.items():
                    if i in attrs:
                        a[i] = value
                return a

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for j in json.keys():
            self.__dict__[j] = json[j]
