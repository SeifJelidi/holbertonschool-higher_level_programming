#!usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nx = 0
    try:
        while nx < x:
            print(my_list[nx], end='')
            nx += 1
        print()
    except IndexError:
        pass
        
    return nx

