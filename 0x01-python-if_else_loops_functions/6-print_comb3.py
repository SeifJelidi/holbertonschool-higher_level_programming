#!/usr/bin/python3
space = ", "
for number in range(0, 10):
    for i in range(number + 1, 10):
        print("{}{}".format(number, i), end="")
        if (number != 8 or i != 9):
            print(space, end="")
print("")
