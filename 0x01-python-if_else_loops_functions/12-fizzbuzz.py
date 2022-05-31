#!/usr/bin/python3
def fizzbuzz():
    for cat in range(1, 101):
        if cat % 3 == 0:
            print("Fizz", end='')
        if cat % 5 == 0:
            print("Buzz", end='')
        if cat % 3 and cat % 5:
            print("{:d}".format(cat), end='')
        print(end='')
