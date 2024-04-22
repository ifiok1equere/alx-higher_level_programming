#!/usr/bin/python3
"""This module define a test suite"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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
        self.s1 = Square(5)
        dictionary = self.r1.to_dictionary()
        dictionary_ = self.s1.to_dictionary()

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

        self.json_dictionary = Square.to_json_string([dictionary, dictionary_])
        self.assertTrue(type(self.json_dictionary) == str)

    def test_save_to_file(self):
        """Test for JSON string to a file"""

        self.tearDown()

        self.r1 = Rectangle(10, 7, 2, 8)
        self.r2 = Rectangle(2, 4)
        self.s1 = Square(5)
        self.s2 = Square(1, 2, 5)

        filename_1 = "{:s}.json".format(self.r1.__class__.__name__)
        filename_2 = "{:s}.json".format(self.s1.__class__.__name__)

        Rectangle.save_to_file([self.r1, self.r2])
        Square.save_to_file([self.s1, self.s2])

        with open(filename_1, "r") as file:
            f = file.read()
            self.assertTrue(type(f) == str)

        with open(filename_2, "r") as file:
            self.assertTrue(type(file.read()) == str)

        Square.save_to_file([self.r1])
        with open(filename_2, "r") as file:
            self.assertTrue(type(file.read()) == str)

        Square.save_to_file([])
        with open(filename_2, "r") as file:
            self.assertEqual(file.read(), "[]")

        Rectangle.save_to_file(None)
        with open(filename_1, "r") as file:
            self.assertEqual(file.read(), "[]")

        Rectangle.save_to_file([self.r1, self.s2])
        with open(filename_1, "r") as file:
            self.assertTrue(type(file.read()) == str)

        Rectangle.save_to_file({self.s1, self.s2})
        with open(filename_1, "r") as file:
            self.assertTrue(type(file.read()) == str)

        Square.save_to_file("")
        with open(filename_2, "r") as file:
            self.assertEqual(file.read(), "[]")

        Square.save_to_file([self.r1, self.s2])
        with open(filename_2, "r") as file:
            self.assertTrue(type(file.read()) == str)
        with open(filename_2, "r") as file:
            self.assertTrue("size" in file.read())

        Rectangle.save_to_file({})
        with open(filename_1, "r") as file:
            self.assertEqual(file.read(), "[]")

        with self.assertRaises(TypeError):
            Rectangle.save_to_file()
        with self.assertRaises(TypeError):
            Square.save_to_file()
        with self.assertRaises(AttributeError):
            Square.save_to_file([34])
        with self.assertRaises(TypeError):
            Square.save_to_file(34)
        with self.assertRaises(AttributeError):
            Square.save_to_file([""])
        with self.assertRaises(AttributeError):
            Square.save_to_file([None])

    def test_from_json_string(self):
        """Tests for converting json string to dictionary"""

        r1 = Rectangle(10, 7, 2, 8)
        s1 = Square(1, 2, 5)

        r1_dict = r1.to_dictionary()
        s1_dict = s1.to_dictionary()

        json_string = Base.to_json_string([r1_dict, s1_dict])
        json_to_obj = Base.from_json_string(json_string)

        self.assertTrue(type(json_to_obj), list)
        self.assertTrue(type(json_to_obj[0]), dict)
