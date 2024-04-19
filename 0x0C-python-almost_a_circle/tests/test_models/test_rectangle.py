#!/usr/bin/python3
"""This module define a test suite"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """This class defines series test suite"""

    def setUp(self):
        """This method creates Rectangle class instances"""

        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10)
        self.r3 = Rectangle(10, 2, 0, 0, 12)
        self.r4 = Rectangle(10, 2, 2, 3)
        self.r33 = Rectangle(10, 2, 6)

    def tearDown(self):
        """This method resets class attribute to 0 so that
        new instances can have non-incremental values for
        their id attributes
        """

        Base._Base__nb_objects = 0

    def test_class_type(self):
        """The method checks whether object instance
        was created correctly
        """

        self.assertEqual(self.r1.__class__.__name__, "Rectangle")
        self.assertEqual(type(self.r1), Rectangle)
        self.assertIsInstance(self.r1, Rectangle)
        self.assertIsInstance(self.r1, Base)

    def test_inheritance(self):
        """This method tests for inheritance"""

        self.assertTrue(issubclass(Rectangle, Base))

    def test_attribute(self):
        """Test to ensure attribute is correctly instantiated"""

        self.assertTrue(hasattr(self.r1, 'id'))
        self.assertTrue(hasattr(self.r1, 'width'))
        self.assertTrue(hasattr(self.r1, 'height'))
        self.assertTrue(hasattr(self.r1, 'x'))
        self.assertTrue(hasattr(self.r1, 'y'))
        # self.assertTrue(hasattr(self.r1, 'y'))

    def test_unique_attribute_values(self):
        """The method tests if unique id' are created for each instance"""

        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r2.height, 10)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r1.y, 0)

    def test_custom_attribute_values(self):
        """This method tests if instances have a custom id when id is not
        None"""

        self.assertEqual(self.r4.id, 3)
        self.assertEqual(self.r4.x, 2)
        self.assertEqual(self.r4.y, 3)
        self.assertEqual(self.r4.x, 2)
        self.assertEqual(self.r4.y, 3)

    def test_incremental_id(self):
        """This method tests if the id attribute is incremented correctly"""

        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 12)
        self.assertNotEqual(self.r4.id, 12)

    def test_input_validation(self):
        """This method tests for valid inputs during class instantiation"""

        with self.assertRaises(TypeError):
            self.r5 = Rectangle("ifiok", 2)
            self.r5 = Rectangle(3.5, 2)
            self.r6 = Rectangle(15, "equere")
            self.r7 = Rectangle(15, 16.9)
            self.r8 = Rectangle(15.0, 16.9)
            self.r9 = Rectangle("ifiok", "equere")
            self.r10 = Rectangle("1", 2)
            self.r11 = Rectangle(8, "2")
            self.r12 = Rectangle("0", "0")
            self.r13 = Rectangle()
            self.r14 = Rectangle(3, 2, "2", 3)
            self.r15 = Rectangle(3, 2, 2, "3")
            self.r16 = Rectangle(3, 2, "2", "3")
            self.r17 = Rectangle(3, 2, "2", "3")
            self.r30 = Rectangle(5, 6, None, -3, 7)
            self.r31 = Rectangle(5, 6, [2])
            self.r32 = Rectangle(5, 6, {}, 4)
            self.r34 = Rectangle("", 6, "", 4)
            self.r35 = Rectangle("", 6, 7, 54)
            self.r36 = Rectangle(5, 6, 7, "")
            self.r37 = Rectangle(None, 6, 7, 3)
            self.r38 = Rectangle(1, None, 7, 0)

        with self.assertRaises(ValueError):
            self.r18 = Rectangle(-1, 2)
            self.r19 = Rectangle(1, -2)
            self.r20 = Rectangle(-1, -2)
            self.r21 = Rectangle(0, 2)
            self.r22 = Rectangle(1, 0)
            self.r23 = Rectangle(0, 0)
            self.r24 = Rectangle(5, 6, 0, 3, 7)
            self.r25 = Rectangle(5, 6, 4, 0, 0)
            self.r26 = Rectangle(5, 6, 0, 0)
            self.r27 = Rectangle(5, 6, -1, 3, 7)
            self.r28 = Rectangle(5, 6, 8, -5)
            self.r29 = Rectangle(5, 6, -2, -3, 7)

        try:
            Rectangle(10, "2")
        except Exception as e:
            self.assertEqual(str(e), "height must be an integer")

        try:
            r = Rectangle(10, 2)
            r.width = -10
        except Exception as e:
            self.assertTrue(str(e) == "width must be > 0")

        try:
            r = Rectangle(10, 2)
            r.x = {}
        except Exception as e:
            self.assertTrue(str(e) == "x must be an integer")

        try:
            Rectangle(10, 2, 3, -1)
        except Exception as e:
            self.assertTrue(str(e) == "y must be >= 0")
