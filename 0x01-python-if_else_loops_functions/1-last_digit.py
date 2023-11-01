#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if number < 0:
    last = -last
msg = "Last digit of {:d} is {:d} {}"
if last > 5:
    print(msg.format(number, last, "and is greater than 5"))
elif last == 0:
    print(msg.format(number, last, "and is 0"))
else:
    print(msg.format(number, last, "and is less than 6 and not 0"))
