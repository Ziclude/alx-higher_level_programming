#!/usr/bin/python3
def magic_calculation(a, b):
    cat = 0
    for u in range(1, 3):
        try:
            if u > a:
                raise Exception('Too far')
            else:
                cat += a ** b / u
        except (ValueError):
            cat = b + a
            break
    return (cat)
