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

    def to_json(self):
        """Get dictionnary representation of student"""
        return self.__dict__
