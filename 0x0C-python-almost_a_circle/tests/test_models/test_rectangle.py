#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
import sys

"""
Test module for Rectangle class
"""


class TestRectangle(unittest.TestCase):

    def test_width_height(self):
        """
        Testing width and height values
        with setters and getters
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        r1.width = 12
        r1.height = 4
        self.assertEqual(r1.width, 12)
        self.assertEqual(r1.height, 4)

    # _______________________________________

    def test_default_params(self):
        """
        Testing x and y default parameters
        """
        r1 = Rectangle(10, 3)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r1 = Rectangle(10, 3, 1)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 0)

    # _______________________________________

    def test_default_id(self):
        """
        Testing with default id
        """
        r1 = Rectangle(21, 7)
        r1 = Rectangle(15, 3, 2, 2)
        r2 = Rectangle(10, 3)
        self.assertEqual(r2.id, r1.id + 1)

    # _______________________________________

    def test_with_args(self):
        """Testing with full args"""
        r1 = Rectangle(10, 2, 4, 4, 20)

    # _______________________________________

    def test_id(self):
        """Testing the id"""
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 12)

    # _______________________________________

    def test_types(self):
        r1 = Rectangle(10, 2)
        self.assertIsInstance(r1, Rectangle)
        self.assertIsInstance(r1, Base)
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertFalse(issubclass(Base, Rectangle))

    # _______________________________________

    def test_private_att(self):
        r1 = Rectangle(12, 2)
        r1.x = 20
        r1.y = 10
        r1.id = 33

        self.assertEqual(r1.x, 20)
        self.assertEqual(r1.y, 10)
        self.assertEqual(r1.id, 33)

    # _______________________________________

    # Validations

    def test_types(self):
        with self.assertRaises(TypeError):
            # Strings
            r = Rectangle("10", 2)
            r = Rectangle(10, "2")
            r = Rectangle(10, 2, "5")
            r = Rectangle(10, 2, 5, "5")
            # lists
            r = Rectangle([10], 2)
            # dictionary
            r = Rectangle(10, {"2", 2})
            # floats
            r = Rectangle(10, 2, 5.5)
            # sets
            r = Rectangle(10, 2, 5, {5})

    # _______________________________________

    def test_values(self):
        with self.assertRaises(ValueError):
            # Test width and height values
            r = Rectangle(0, 2)
            r = Rectangle(-20, 4)
            r = Rectangle(10, 0)
            r = Rectangle(10, -3)
            # Test x and y values
            r = Rectangle(17, 5, -1)
            r = Rectangle(17, 5, 2, -2)

    # _______________________________________

    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    # _______________________________________

    def test_display(self):
        r1 = Rectangle(4, 6)
        my_output = StringIO()
        sys.stdout = my_output
        r1.display()
        printed_output = my_output.getvalue()
        sys.stdout = sys.__stdout__

        r1_display = '####\n####\n####\n####\n####\n####'
        self.assertEqual(printed_output.strip(), r1_display)
