#!usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        nx = 0
        while nx < x:
            print(my_list[nx], end='')
            nx += 1
        print()
    except IndexError:
        print()
    return nx
