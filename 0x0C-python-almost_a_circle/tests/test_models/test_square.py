#!/usr/bin/python3
""" This module conducts unittests tests """

import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """
    This class conducts test
    on the the Retangle class.
    """

    def setUp(self):
        """ The method sets up objects """
        Base._Base__nb_objects = 0
        self.s1 = Square(10)
        self.s2 = Square(2, 10)
        self.s3 = Square(10, 2, 0, 12)
        self.s4 = Square(3, 2, 1, None)
        self.s5 = Square(3, 2, 1, 6.5)
        self.s6 = Square(3, 2, 1, '6.5')
        self.s7 = Square(3, 2, True)
        self.s8 = Square(True, False, True)

    def tearDown(self):
        pass

    def test_init(self):
        """ The method tests the Base & Square class atrributes """
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s1.width, 10)
        self.assertEqual(self.s1.height, 10)
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s1.y, 0)

        self.assertEqual(self.s2.width, 2)
        self.assertEqual(self.s2.height, 2)
        self.assertEqual(self.s2.x, 10)
        self.assertEqual(self.s2.y, 0)
        self.assertEqual(self.s2.id, 2)

        self.assertEqual(self.s3.id, 12)
        self.assertEqual(self.s3.x, 2)
        self.assertEqual(self.s3.y, 0)
        self.assertEqual(self.s3.size, self.s3.width)
        self.assertEqual(self.s3.size, self.s3.height)
        self.assertEqual(self.s3.width, self.s3.width)

        self.assertEqual(self.s4.size, 3)
        self.assertEqual(self.s4.width, 3)
        self.assertEqual(self.s4.height, 3)
        self.assertEqual(self.s4.width, self.s4.height)
        self.assertEqual(self.s4.id, 3)

        self.assertEqual(self.s5.id, 6.5)

        self.assertEqual(self.s6.id, '6.5')

        self.assertEqual(self.s7.y, 1)

        self.assertEqual(self.s8.size, 1)
        self.assertEqual(self.s8.width, 1)
        self.assertEqual(self.s8.height, 1)
        self.assertEqual(self.s8.width, self.s8.height)
        self.assertEqual(self.s8.id, 5)

    def test_init_raise_error(self):
        ''' Checks that TypeErrors were raised '''
        self.assertRaises(TypeError, Square)
        self.assertRaises(TypeError, Square, '3')
        self.assertRaises(TypeError, Square, 3, '1')
        self.assertRaises(TypeError, Square, 3.1, 2)
        self.assertRaises(TypeError, Square, 1, 1.1)
        self.assertRaises(ValueError, Square, -1, 2)
        self.assertRaises(ValueError, Square, 1, -2)
        self.assertRaises(ValueError, Square, 1, 2, -5)
        self.assertRaises(ValueError, Square, 0, 2)

    def test_area(self):
        ''' Tests for correctness of the square area '''
        self.assertEqual(self.s1.area(), 100)
        self.assertEqual(self.s2.area(), 4)
        self.assertEqual(self.s3.area(), 100)
        self.assertNotEqual(self.s4.area(), 99)
        self.assertEqual(self.s5.area(), 9)
        self.assertEqual(self.s6.area(), 3 * 3)

    def test_update(self):
        """ Tests for the update method """
        self.s1.update(8, 10, 3, 20)

        self.assertEqual(self.s1.width, 10)
        self.assertEqual(self.s1.height, 10)
        self.assertEqual(self.s1.x, 3)
        self.assertEqual(self.s1.y, 20)
        self.assertEqual(self.s1.id, 8)

        self.s1.update(size=15)

        self.assertEqual(self.s1.width, 15)
        self.assertEqual(self.s1.height, 15)
        self.assertEqual(self.s1.size, 15)
        """ Ensure other attributes remain unchanged """
        self.assertEqual(self.s1.x, 3)
        self.assertEqual(self.s1.y, 20)
        self.assertEqual(self.s1.id, 8)

    def test_update_raise_error(self):
        """
        Tests for errors raised when invalid inputs are
        parsed into the update method
        """
        self.assertRaises(TypeError, self.s1.update, "valid", None)
        self.assertRaises(TypeError, self.s1.update, "valid", 20, "True")
        self.assertRaises(TypeError, self.s1.update, "valid", 23, 20, 0.1)
        self.assertRaises(TypeError, self.s1.update, "valid", 23, 20.1, 5)
        self.assertRaises(ValueError, self.s1.update, None, -2)
        self.assertRaises(ValueError, self.s1.update, '#*#', 2, -1)
        self.assertRaises(ValueError, self.s1.update, '##$', 2, 1, -1)
        self.assertRaises(TypeError, self.s1.update, '*', 2.1, 1, 5)

    def test_str(self):
        """ Tests for the overidding __str__ method """
        self.s1.update(4, 6, 2, 12)
        self.assertEqual(str(self.s1), "[Square] (4) 2/12 - 6")

    def test_to_dictionary(self):
        """ Tests for the dictionary representation of a square instance """
        self.assertEqual(
                self.s1.to_dictionary(), {'id': 1, 'x': 0, 'size': 10, 'y': 0}
                )
        self.assertEqual(
                self.s2.to_dictionary(), {'id': 2, 'x': 10, 'size': 2, 'y': 0}
                )
        self.assertEqual(
                self.s3.to_dictionary(), {'id': 12, 'x': 2, 'size': 10, 'y': 0}
                )
        self.assertEqual(
                self.s4.to_dictionary(), {'id': 3, 'x': 2, 'size': 3, 'y': 1}
                )
        self.assertEqual(
                self.s5.to_dictionary(), {'id': 6.5, 'x': 2, 'size': 3, 'y': 1}
                )
        self.assertEqual(
                self.s6.to_dictionary(),
                {'id': '6.5', 'x': 2, 'size': 3, 'y': 1}
                )
        self.assertEqual(
                self.s7.to_dictionary(), {'id': 4, 'x': 2, 'size': 3, 'y': 1}
                )
        self.assertEqual(
                self.s8.to_dictionary(), {'id': 5, 'x': 0, 'size': 1, 'y': 1}
                )

    def test_to_json_string(self):
        self.assertEqual(
            Base.to_json_string(
                [self.s1.to_dictionary(), self.s2.to_dictionary()]
            ),
            '[{"id": 1, "x": 0, "size": 10, "y": 0}, '
            '{"id": 2, "x": 10, "size": 2, "y": 0}]'
            )

        self.assertEqual(
            Base.to_json_string([self.s1.to_dictionary()]),
            '[{"id": 1, "x": 0, "size": 10, "y": 0}]'
            )
        self.assertEqual(
            Base.to_json_string(
                [
                    self.s1.to_dictionary(),
                    self.s2.to_dictionary(),
                    self.s3.to_dictionary(),
                    self.s4.to_dictionary()
                ]
            ),
            '[{"id": 1, "x": 0, "size": 10, "y": 0}, '
            '{"id": 2, "x": 10, "size": 2, "y": 0}, '
            '{"id": 12, "x": 2, "size": 10, "y": 0}, '
            '{"id": 3, "x": 2, "size": 3, "y": 1}]'
            )

        def test_type(self):
            self.assertEqual(type(self.s8.to_dictionary()), dict)
            self.assertEqual(
                    type(Base.to_json_string(
                        [self.s1.to_dictionary(), self.s2.to_dictionary()]
                    )), str)

    def test_save_square_to_file(self):
        """
        Test saving a list of Square objects to a file.
        """
        Square.save_to_file([self.s1, self.s2])

        with open("Square.json", "r") as file:
            content = file.read()

        expected_json = json.dumps(
                [self.s1.to_dictionary(), self.s2.to_dictionary()]
                )
        self.assertEqual(content, expected_json)

        """ Clean up by removing the file after the test """
        os.remove("Square.json")

    def test_save_empty_list(self):
        """
        Test saving an empty list of objects to a file.
        """
        Square.save_to_file([])

        self.assertTrue(os.path.exists("Square.json"))

    def test_save_to_file_with_None(self):
        """
        Test saving a list with None object to a file.
        """
        self.assertRaises(TypeError, Square.save_to_file, None)
