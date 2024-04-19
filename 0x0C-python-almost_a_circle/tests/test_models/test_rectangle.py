#!/usr/bin/python3
"""This module define a test suite"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """This class defines series test suite"""

    def setUp(self):
        """This method creates Base class instances"""

        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10)
        self.r3 = Rectangle(10, 2, 0, 0, 12)
        self.r4 = Rectangle(10, 2, 2, 3)

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
