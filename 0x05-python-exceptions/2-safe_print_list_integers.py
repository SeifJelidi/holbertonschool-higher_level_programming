#!usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nx = 0
    while nx <= x:
        try:
            print("{:d}".format(my_list[nx]), end="")
            nx = nx + 1
        except (ValueError, TypeError):
            pass 
    print()
    return nx
