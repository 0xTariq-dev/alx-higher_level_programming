#!/usr/bin/python3
import unittest
from models.base import Base


class Test_Base(unittest.TestCase):
    """unittest Class for Base Class"""

    def test_Base_no_arg(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

    def test_Base_id(self):
        base20 = Base(20)
        self.assertEqual(base20.id, 20)

    def test_Base_after_id(self):
        base5 = Base(5)
        base = Base()
        self.assertEqual(base5.id, 5)
        self.assertEqual(base.id, 1)

if __name__ == "__main__":
    unittest.main()
