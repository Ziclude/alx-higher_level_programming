#!/usr/bin/python3
"""Script that takes url and send req"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as rest:
            print(rest.read().decode('UTF-8'))
    except error.HTTPError as err:
        print('Error code:', err.code)
