"""This module defines the TestRectangle class.

Usage: 
    To execute all tests in the terminal execute the following command:

    $ python -m unittest tests/test_rectangle.py
"""

__author__ = ""
__version__ = ""

import unittest
import math
from shape.rectangle import Rectangle

class rectangletests(unittest.TestCase):
    """
    This is a class for tests of the rectangle class.
    """
    def setup(self):
        """
        
        """
        self.rectangle = Rectangle("white", 4, 6)

    def test_blank_color(self):
        """
        
        """
        with self.assertRaises(ValueError):
            self.rectangle = Rectangle("", 4, 6)

    def test_length_not_integar(self):
        """
        
        """
        with self.assertRaises(ValueError):
            self.rectangle = Rectangle("white", "ns", 6)

    def test_width_not_integar(self):
        """
        
        """
        with self.assertRaises(ValueError):
            self.rectangle = Rectangle("white", 4, "ns")

    def test_str_(self):
        """
        
        """
        self.rectangle = Rectangle("white", 4, 6)
        expected_str = "The shape color is white.\n This rectangle has four sides with the lengths of 4, 6, 4 and 6 centimeters."      
        self.assertEqual(str(self.rectangle), expected_str)

    def test_calculate_area(self):
        """
        
        """
        self.rectangle = Rectangle("white", 4, 6)
        expected_area = 4 * 6 
        self.assertEqual(self.rectangle.calcualte_area(), expected_area)

    def test_calculate_perimeter(self):
        """
        
        """
        self.rectangle = Rectangle("white", 4, 6)
        expected_perimeter = 4 * 2 + 6 * 2
        self.assertEqual(self.rectangle.calculate_perimeter(), expected_perimeter)
        