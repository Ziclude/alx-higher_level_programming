#!/usr/bin/python3
"""Script that fetches to intranet status"""


if __name__ == '__main__':
    import urlib.request
    with urlib.request.urlopen('https://alx-intranet.hbtn.io/status') as result:
        content = result.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
