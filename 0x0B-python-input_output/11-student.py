#!/usr/bin/python3
"""Define class Student"""


class Student:
    """Represent Student"""

    def __init__(self, first_name, last_name, age):
        """Initialize new Student.
        Args:
           first_name (str): first name's student
           last_name (str): last name's student
           age (int): age's student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get dictionnary representation of student
        Args:
           attrs (list): (optional) attributes to represent
        """
        if (type(attrs) == list and all(type(elem) == str for elem in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of student
        Args:
           json (dict):key pairs to replace attributes
        """
        for i, v in json.items():
            setattr(self, i, v)
