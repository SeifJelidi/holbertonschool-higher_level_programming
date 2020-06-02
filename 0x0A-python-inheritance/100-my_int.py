#!/usr/bin/python3
'''child class (MyInt) from the
the parent class (int)'''


class MyInt(int):
    def __init__(self, number):
        self.number = number

    def __ne__(self, val):
        return (self.number == val)

    def __eq__(self, val):
        return (self.number != val)

    def __str__(self):
        return (str(self.number))
