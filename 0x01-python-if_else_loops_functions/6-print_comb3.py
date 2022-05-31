#!/usr/bin/python3
cat = 0
while cat <= 89:
    if cat % 10 == 0:
        cat += 1 + cat // 10
    print("{:02d}".format(cat), end='\n' if cat == 89 else ", ")
    cat += 1
