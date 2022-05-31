#!/usr/bin/python3
for val in range(97, 123):
    if (val != 101 and val != 113):
        print("{:c}".format(val), end='')
