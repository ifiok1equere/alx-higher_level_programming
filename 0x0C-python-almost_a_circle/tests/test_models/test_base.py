#!/usr/bin/python3
"""This module define a test suite"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """This class defines series test suite"""

    def setUp(self):
        """This method creates Base class instances"""

        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.b4 = Base(12)
        self.b5 = Base()
        self.b6 = Base()

    def tearDown(self):
        """This method resets class attribute to 0 so that
        new instances can have non-incremental values for
        their id attributes"""

        Base._Base__nb_objects = 0

    def test_class_type(self):
        """The method checks whether object instance
        was created correctly"""

        self.assertEqual(self.b1.__class__.__name__, "Base")
        self.assertEqual(type(self.b1), Base)
        self.assertTrue(isinstance(self.b1, Base))

    def test_attribute(self):
        """Test to ensure attribute is correctly instantiated"""

        self.assertTrue(hasattr(self.b1, 'id'))

    def test_unique_id(self):
        """The method tests if unique id' are created for each instance"""

        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)

    def test_custom_id(self):
        """This method tests if instances have a custom id when id is not
        None"""

        self.assertEqual(self.b4.id, 12)

    def test_incremental_id(self):
        """This method tests if the id attribute is incremented correctly"""

        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertNotEqual(self.b4.id, 4)
        self.assertEqual(self.b5.id, 4)
        self.assertEqual(self.b6.id, 5)

    def test_to_json_string(self):
        """Test for json string representation"""

        self.r1 = Rectangle(10, 7, 2, 8)
        dictionary = self.r1.to_dictionary()

        with self.assertRaises(TypeError):
            self.json_dictionary = Base.to_json_string()
        with self.assertRaises(TypeError):
            self.json_dictionary = Base.to_json_string(2)

        self.json_dictionary = Base.to_json_string(None)
        self.assertEqual(self.json_dictionary, "[]")

        self.json_dictionary = Base.to_json_string([])
        self.assertEqual(self.json_dictionary, "[]")

        self.json_dictionary = Base.to_json_string([{}])
        self.assertEqual(self.json_dictionary, "[{}]")

        self.json_dictionary = Base.to_json_string([dictionary])
        self.assertTrue(type(self.json_dictionary) == str)
