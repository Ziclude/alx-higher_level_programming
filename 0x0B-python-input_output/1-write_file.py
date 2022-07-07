#!/usr/bin/python3
"""Define a file writing function"""


def write_file(filename="", text=""):
    """write a string to a UTF8 text file.
    Args:
        filename (str): name's file.
        text (str): text to write.
    Returns:
        number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
