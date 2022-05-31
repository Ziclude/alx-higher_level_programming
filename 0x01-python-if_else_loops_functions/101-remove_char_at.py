#!/usr/bin/python3
def remove_char_at(str, n):
    nouv = ""
    a = 0
    for d in str:
        if a != n:
            nouv += d
        a += 1
    return nouv
