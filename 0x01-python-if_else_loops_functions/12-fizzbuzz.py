#!/usr/bin/python3
FZ = "Fizz"
BZ = "Buzz"
def fizzbuzz():
    for cat in range(1, 101):
        if (cat % 3 and cat % 5):
            print("%s%s" % (FZ, BZ), end=' ')
        elif (cat % 3):
            print("%s" % (FZ), end=' ')
        elif (cat % 5):
            print("%s" % (BZ), end=' ')
        else:
            print("%d" % (cat), end=' ')
