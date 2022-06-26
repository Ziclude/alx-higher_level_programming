#!/usr/bin/python3
"""text indentation function."""


def text_indentation(text):
    """Prints two new lines after each specific punctuation
    Args:
       text (str): Perfom for operator.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    cat = ['.', '?', ':']
    nouv_text = ""
    for ltr in text:
        nouv_text += ltr
        if ltr in cat:
            nouv_text += "\n"
            print(nouv_text.strip(" "))
            nouv_text = ""
    if ltr not in cat:
        print(nouv_text.strip(" "), end="")
