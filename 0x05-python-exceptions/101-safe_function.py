#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        total = fct(*args)
        return (total)
    except Exception as error:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
