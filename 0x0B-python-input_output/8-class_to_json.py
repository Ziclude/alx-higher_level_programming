#!/usr/bin/python3
"""Define Python class to JSON function"""


def class_to_json(obj):
    """Return dictionnary representation of
    simple data structure"""
    return obj.__dict__
