#!/usr/bin/python3
"""Script that url and send request"""


import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as result:
        print(dict(result.headers).get("X-Request-Id"))
