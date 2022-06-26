#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer."""

    def test_ordered_list(self):
        """Test an ordered list."""
        order = [1, 2, 3, 4]
        self.assertEqual(max_integer(order), 4)

    def test_unorder_list(self):
        """Test an unordered list."""
        unord = [1, 2, 3, 4]
        self.assertEqual(max_integer(unord), 4)

    def test_max_at_begng(self):
        """Test a list with a beginning max value."""
        max_at_begng = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_begng), 4)

    def test_empty_lst(self):
        """Test an empty list."""
        emty = []
        self.assertEqual(max_integer(emty), None)

    def test_one_elt_list(self):
        """Test a list with a single element."""
        one_elt = [7]
        self.assertEqual(max_integer(one_elt), 7)

    def test_flts(self):
        """Test a list of floats."""
        flts = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(flts), 15.2)

    def test_ints_and_flts(self):
        """Test a list of ints and floats."""
        ints_and_flts = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_flts), 15.5)

    def test_strg(self):
        """Test a string."""
        strg = "Brennan"
        self.assertEqual(max_integer(strg), 'r')

    def test_list_of_strgs(self):
        """Test a list of strings."""
        strgs = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strgs), "name")

    def test_empty_strg(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
