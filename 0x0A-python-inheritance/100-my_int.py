#!/usr/bin/python3
'''child class (MyInt) from the
the parent class (int)'''


class MyInt(int):
    '''__'''
    def __init__(self, number):
        '''__'''
        self.number = number

    def __ne__(self, val):
        '''___'''
        return (self.number == val)

    def __eq__(self, val):
        '''___''''
        return (self.number != val)

    def __str__(self):
        '''___'''
        return (str(self.number))
