#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    mdl = number % 10
elif number < 0:
    mdl = number % -10

if mdl > 5:
    str = 'and is greater than 5'
elif mdl == 0:
    str = 'and is 0'
elif mdl < 6:
    str = 'and is less than 6 and not 0'
print("Last digit of {} {} {} {}".format(number, 'is', mdl, str))
