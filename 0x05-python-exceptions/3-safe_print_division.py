#!/usr/bin/python3
def safe_print_division(a, b):
    cat = 0
    try:
        cat = a / b
    except (ZeroDivisionError):
        cat = None
    finally:
        print("Inside result: {}".format(cat))
        return (cat)
