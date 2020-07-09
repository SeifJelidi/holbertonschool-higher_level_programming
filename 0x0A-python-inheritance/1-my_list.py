#!/usr/bin/python3
'''MyList that inherits from list'''


class MyList(list):
    '''the child class from the parent class (list)'''
    def print_sorted(self):
        '''print the list'''
        print(sorted(self))
