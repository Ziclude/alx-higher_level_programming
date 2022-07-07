#!/usr/bin/python3
"""Define a text file reading function"""


def read_file(filename=""):
    """Print the UTF8 content text file to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
