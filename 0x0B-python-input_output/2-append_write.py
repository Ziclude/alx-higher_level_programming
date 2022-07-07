#!/usr/bin/python3
"""Define a file appending function"""


def append_write(filename="", text=""):
    """Append string to the end of utf8 text file.
    Args:
       filename (str): name's file
       text (str): string to append
    Returns:
         Number of characters appended.
    """
    with open(filename="", "a", encoding="utf-8") as f:
        return f.write(text)
