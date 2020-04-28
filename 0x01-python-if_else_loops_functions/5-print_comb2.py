#!/usr/bin/python3
numbers = []
space = ", "
for number in range(0, 100):
    if number < 10:
        numbers.insert(number, "{}{}".format(0, number))
    else:
        numbers.insert(number, "{}".format(number))
print(space.join(numbers))
