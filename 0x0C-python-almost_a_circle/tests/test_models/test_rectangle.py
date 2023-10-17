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

    def test_explicit_id(self):
        """Testing with full args"""

        self.assertEqual(Rectangle(10, 2, 4, 4, 20).id, 20)

        r1 = Rectangle(10, 2, 4, 4, 25)
        r2 = Rectangle(10, 2, 4, 4, 25)
        self.assertEqual(r1.id, r2.id)

        r1 = Rectangle(10, 2, 4, 4, 25)
        r2 = Rectangle(10, 2, 4, 4, 30)
        self.assertEqual(r1.id, r2.id - 5)

    # _______________________________________

    def test_with_args(self):
        """Testing with full args"""
        Rectangle(10, 2, 4, 4, 20)

    # _______________________________________

    def test_with_no_args(self):
        """Testing with no args"""
        with self.assertRaises(TypeError):
            Rectangle()

    # _______________________________________

    def test_with_one_args(self):
        """Testing with one arg"""
        with self.assertRaises(TypeError):
            Rectangle(5)

    # _______________________________________

    def test_with_many_args(self):
        """Testing with one arg"""
        with self.assertRaises(TypeError):
            Rectangle(5, 2, 1, 2, 15, 20)

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

    def test_indirect_att_access(self):
        r1 = Rectangle(12, 2)
        r1.x = 20
        r1.y = 10
        r1.id = 33

        self.assertEqual(r1.x, 20)
        self.assertEqual(r1.y, 10)
        self.assertEqual(r1.id, 33)

    # _______________________________________

    def test_direct_att_access(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(12, 2).__width)
            print(Rectangle(12, 2).__height)
            print(Rectangle(12, 2, 1, 4).__x)
            print(Rectangle(12, 2, 1, 1).__y)

            r1 = Rectangle(12, 2)
            r1.__x = 5
            r1.__y = 5

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

        r3 = Rectangle(8, 7, 0, 0, 12)
        r3.width = 20
        r3.height = 10
        self.assertEqual(r3.area(), 200)

        r3 = Rectangle(13612647432734723472, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 95288532029143064304)

        r3 = Rectangle(7, 21512642754863876325418658321, 0, 0, 12)
        self.assertEqual(r3.area(), 150588499284047134277930608247)

    # _______________________________________

    @staticmethod
    def str_takeout():
        my_output = StringIO()
        sys.stdout = my_output
        return my_output

    # _______________________________________

    def test_display(self):
        r1 = Rectangle(4, 6)

        my_output = self.str_takeout()
        r1.display()
        printed_output = my_output.getvalue()
        sys.stdout = sys.__stdout__

        r1_display = '####\n####\n####\n####\n####\n####'
        self.assertEqual(printed_output.strip(), r1_display)

        r1 = Rectangle(3, 3, 1, 1)

        my_output = self.str_takeout()
        r1.display()
        printed_output = my_output.getvalue()
        sys.stdout = sys.__stdout__

        r1_display = '###\n ###\n ###'
        self.assertEqual(printed_output.strip(), r1_display)

    # _______________________________________

    def test_str(self):
        r1 = Rectangle(10, 3)
        r1_str = f"[Rectangle] (18) 0/0 - 10/3"
        self.assertEqual(r1.__str__(), r1_str)


class TestRectangleAttr(unittest.TestCase):

    def test_rectangle_width_type(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)
            Rectangle([10], 7)
            Rectangle(None, 3)
            Rectangle(5.5, 5)
            Rectangle({"5": 5}, 10)

    def test_rectangle_height_type(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, "2")
            Rectangle(12, [2])
            Rectangle(12, None)
            Rectangle(12, 5.5)
            Rectangle(12, {5})

    def test_rectangle_x_type(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 2, "2")
            Rectangle(12, 2, 1.2)
            Rectangle(12, 6, [2])
            Rectangle(12, 4, {3})
            Rectangle(12, 4, None)

    def test_rectangle_y_type(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(17, 5, 2, "2")
            Rectangle(17, 5, 2, [1])
            Rectangle(17, 5, 2, 3.1)
            Rectangle(17, 5, 2, None)
            Rectangle(17, 5, 2, {2})

    # ________________________________________________________________

    def test_rectangle_width_value(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-5, 5)
            Rectangle(-20, 5)
            Rectangle(0, 5)

    def test_rectangle_height_value(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -5)
            Rectangle(12, -8)
            Rectangle(17, 0)

    def test_rectangle_x_value(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 5, -5)
            Rectangle(12, 8, -1)

    def test_rectangle_y_value(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(17, 2, 2, -2)
            Rectangle(17, 2, 5, -5)


class TestRectangleUpdateMethod(unittest.TestCase):

    def test_update_with_kwargs(self):
        rect = Rectangle(10, 20)
        rect.update(width=30, height=40, x=50, y=60,
                    id=70)  # Update with **kwargs
        self.assertEqual((rect.width, rect.height, rect.x,
                         rect.y, rect.id), (30, 40, 50, 60, 70))

    def test_update_empty_args_with_kwargs(self):
        rect = Rectangle(10, 20)
        rect.update(width=30, height=40, x=50, y=60,
                    id=70)  # No *args, only **kwargs
        self.assertEqual((rect.width, rect.height, rect.x,
                         rect.y, rect.id), (30, 40, 50, 60, 70))

    def test_update_empty_args_empty_kwargs(self):
        rect = Rectangle(10, 20)
        rect.update()  # No *args and no **kwargs, should not change the instance
        self.assertEqual((rect.width, rect.height, rect.x,
                         rect.y, rect.id), (10, 20, 0, 0, rect.id))


class TestRectangleToDictionaryMethod(unittest.TestCase):

    def test_to_dictionary(self):
        # Create a Rectangle instance
        rect = Rectangle(10, 20, 30, 40, 50)
        
        # Get the dictionary representation
        rect_dict = rect.to_dictionary()
        
        # Verify that the dictionary contains the expected keys and values
        self.assertEqual(rect_dict, {'id': 50, 'width': 10, 'height': 20, 'x': 30, 'y': 40})

    def test_to_dictionary_default_values(self):
        # Create a Rectangle instance with default values
        rect = Rectangle(10, 20)
        
        # Get the dictionary representation
        rect_dict = rect.to_dictionary()
        
        # Verify that the dictionary contains the expected keys and values
        self.assertEqual(rect_dict, {'id': rect.id, 'width': 10, 'height': 20, 'x': 0, 'y': 0})
