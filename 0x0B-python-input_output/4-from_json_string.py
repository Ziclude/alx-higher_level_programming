#!/usr/bin/python3
"""Define a JSON-to-object function"""
import json


def from_json_string(my_str):
    """Return Python object representation of JSON string"""
    return json.loads(my_str)
