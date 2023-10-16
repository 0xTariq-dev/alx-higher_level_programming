#!/usr/bin/python3

"""
Testing base module
"""


import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Defines tests for Base class"""

    def test_no_args(self):
        b1 = Base()
        b2 = Base()
        # b2.id will be greater than b1.id by 1
        self.assertEqual(b1.id, b2.id - 1)
        self.assertEqual(b2.id, b1.id + 1)

    # _______________________________________

    def test_none_arg(self):
        b1 = Base(None)
        b2 = Base(None)
        # b2.id will be greater than b1.id by 1
        self.assertEqual(b1.id, b2.id - 1)

    # _______________________________________

    def test_with_args(self):
        b1 = Base(12)
        self.assertEqual(b1.id, 12)
        b2 = Base(25)
        self.assertEqual(b2.id, 25)
        self.assertNotEqual(b1.id, b2.id)

    # _______________________________________

    def test_instantiation(self):
        b1 = Base()
        self.assertIsInstance(b1, Base)
        b2 = Base(12)
        self.assertIsInstance(b2, Base)

    # _______________________________________

    def test_public_att(self):
        b1 = Base(18)
        b1.id = 20
        self.assertNotEqual(b1.id, 18)

    # _______________________________________

    def test_hidden_att(self):
        b1 = Base()
        with self.assertRaises(AttributeError):
            print(b1.__nb_objects)
            b1.__nb_objects
            print(b1.nb_objects)
            b1.__nb_objects

    # ---------------------------------------

    def test_access_nb_instances(self):
        with self.assertRaises(AttributeError):
            print(Base(20).__nb_instances)

    # ---------------------------------------

    def test_Different_id_types(self):
        # Test string type.
        self.assertEqual(Base("str").id, "str")
        # Test float type.
        self.assertEqual(Base(9.99).id, 9.99)
        # Test dictionary type.
        self.assertEqual(Base({"i": 20, "b": 60}).id, {"i": 20, "b": 60})
        # Test bool type.
        self.assertEqual(Base(False).id, False)
        # Test list type.
        self.assertEqual(Base([8, 7]).id, [8, 7])
        # Test tuple type.
        self.assertEqual(Base((2, 5)).id, (2, 5))
        # Test range type.
        self.assertEqual(Base(range(10)).id, range(10))
        # Test infinty float type.
        self.assertEqual(Base(float('inf')).id, float('inf'))
        # Test bytes string type.
        self.assertEqual(Base(b'bytes').id, b'bytes')
        # Test NaN type.
        self.assertNotEqual(Base(float('nan')).id, float('nan'))

    # ---------------------------------------

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(5, 5)

    # ---------------------------------------


class TestBase_to_JSON:
    """ Test Cases for to_json_string method"""

    def test_to_json_string_type(self):
        # Test Rectangle string Type.
        rec = Rectangle(1, 5, 20, 4, 3)
        self.assertEqual(type(Base.to_json_string([rec.to_dictionary])), str)
        # Test Square string Type.
        sq = Square(2, 7, 8, 4)
        self.assertEqual(type(Base.to_json_string([sq.to_dictionary])), str)

    # ---------------------------------------

    def test_to_json_string_empty_and_none(self):
        # Test empty list.
        self.assertEqual(Base.to_json_string([]), "[]")
        # Test None.
        self.assertEqual(Base.to_json_string(None), "[]")

    # ---------------------------------------

    def test_to_json_string_args_types(self):
        # Test with no arguments.
        with self.assertRaises(TypeError):
            Base.to_json_string()
        # Test with many arguments.
        with self.assertRaises(TypeError):
            Base.to_json_string(1, 20, [56])
        # Test with unsupported type.
        with self.assertRaises(TypeError):
            Base.to_json_string([5.5])
        with self.assertRaises(TypeError):
            Base.to_json_string([True])
        with self.assertRaises(TypeError):
            Base.to_json_string([5.5, 'str', False, {'s': 5}])


    # ---------------------------------------


class TestBase_save_to_file(unittest.TestCase):
    """ Test Cases for save_to_file method"""

    def test_save_to_file_Rectangle(self):
        # Test with one instance.
        rec = Rectangle(5, 6, 5, 6, 7)
        Rectangle.save_to_file([rec])
        with open("Rectangle.json", "r") as j:
            self.assertTrue(len(j.read()) == 52)
        # Test With Two Instances.
        rec = Rectangle(5, 6, 5, 6, 7)
        rec2 = Rectangle(10, 6, 5, 6, 7)
        Rectangle.save_to_file([rec, rec2])
        with open("Rectangle.json", "r") as j:
            self.assertTrue(len(j.read()) == 105)
        # Test With None.
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as j:
            self.assertEqual(j.read(), "[]")

    # ---------------------------------------

    def test_save_to_file_Square(self):
        # Test with one instance.
        sq = Square(5, 6, 5, 6)
        Square.save_to_file([sq])
        with open("Square.json", "r") as j:
            self.assertTrue(len(j.read()) == 38)
        # Test With Two Instances.
        sq = Square(5, 6, 5, 6)
        sq2 = Square(10, 6, 6, 7)
        Square.save_to_file([sq, sq2])
        with open("Square.json", "r") as j:
            self.assertTrue(len(j.read()) == 77)
        # Test With None.
        Square.save_to_file(None)
        with open("Square.json", "r") as j:
            self.assertEqual(j.read(), "[]")

    # ---------------------------------------

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as j:
            self.assertEqual(j.read(), "[]")
        

    # ---------------------------------------

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Square.save_to_file()

    # ---------------------------------------

    def test_save_to_file_many_args(self):
        with self.assertRaises(TypeError):
            Square.save_to_file(1, 2, 10)

    # ---------------------------------------

    def test_save_to_file_Overwrite(self):
        sq = Square(5, 6, 5, 6)
        Square.save_to_file([sq])
        sq = Square(15, 6, 5, 6)
        Square.save_to_file([sq])
        with open("Square.json", "r") as j:
            self.assertTrue(len(j.read()) == 39)

    # ---------------------------------------

    def test_save_to_file_class_name_for_filename(self):
        sq = Square(15, 6, 5, 6)
        Base.save_to_file([sq])

    # ---------------------------------------

    @classmethod
    def teardown(self):
        """Delete Created Files"""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass

        try:
            os.remove("Square.json")
        except IOError:
            pass

        try:
            os.remove("Base.json")
        except IOError:
            pass

    # ---------------------------------------


class TestBase_from_json_string(unittest.TestCase):
    """Test from_json_string method"""

    def test_from_json_string_type(self):
        list_input = [{"id": 50, "width": 10, "height": 4}]
        JSON_list = Rectangle.to_json_string(list_input)
        output = Rectangle.from_json_string(JSON_list)
        self.assertEqual(type(output), list)

    # ---------------------------------------

    def test_from_json_string_Rectangle(self):
        # Test with one instance.
        list_input = [{"id": 50, "width": 10, "height": 4, "y": 7}]
        JSON_list = Rectangle.to_json_string(list_input)
        output = Rectangle.from_json_string(JSON_list)
        self.assertEqual(output, list_input)
        # Test with two instances.
        list_input = [
                {"id": 50, "width": 10, "height": 4, "y": 7},
                {"id": 70, "width": 18, "height": 5, "y": 9}
        ]
        JSON_list = Rectangle.to_json_string(list_input)
        output = Rectangle.from_json_string(JSON_list)
        self.assertEqual(output, list_input)

    # ---------------------------------------

    def test_from_json_string_Square(self):
        # Test with one instance.
        list_input = [{"id": 50, "size": 5, "height": 7}]
        JSON_list = Square.to_json_string(list_input)
        output = Square.from_json_string(JSON_list)
        self.assertEqual(output, list_input)
        # Test with two instances.
        list_input = [
                {"id": 50, "size": 5, "height": 4},
                {"id": 60, "size": 5, "height": 7}
        ]
        JSON_list = Square.to_json_string(list_input)
        output = Square.from_json_string(JSON_list)
        self.assertEqual(output, list_input)

    # ---------------------------------------

    def test_save_from_file_empty_list_and_None(self):
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string(None), [])

    # ---------------------------------------

    def test_save_from_file_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    # ---------------------------------------

    def test_save_from_file_many_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string(1, 2, 10)

    # ---------------------------------------
   
