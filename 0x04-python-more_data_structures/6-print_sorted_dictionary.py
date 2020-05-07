#!usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for x in sorted(a_dictionary):
        print(x, end="")
        print(":", a_dictionary[x])
