#!/usr/bin/python3
"""Define a locked class"""


class LockedClass:
    """Prevent user for anything but attributes called
    'first_name' from instantiating new LockedClass attributes
    """

    __slots__ = ["first_name"]
