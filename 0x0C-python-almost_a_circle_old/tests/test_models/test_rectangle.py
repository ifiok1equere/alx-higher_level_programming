#!/usr/bin/python3
""" This module conducts unittests tests"""
import unittest
import os
import json
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    This class conducts test
    on the the Retangle class.
    """

    def setUp(self):
        """ The method sets up objects """
        Base._Base__nb_objects = 0
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10)
        self.r3 = Rectangle(10, 2, 0, 0, 12)
        self.r4 = Rectangle(5, 7)
        self.r5 = Rectangle(1, 2, 2, 3)
        self.r6 = Rectangle(3, 2, 1, 9, None)
        self.r7 = Rectangle(3, 2, 1, 9, "string")
        self.r8 = Rectangle(3, 2, 1, 9, 4.5)
        self.r9 = Rectangle(3, 2, 1, 9, True)
        self.r9 = Rectangle(3, 2, 1, 9, True)

    def tearDown(self):
        pass

    def test_init(self):
        """ The method tests the Base & Rectangle class atrributes """
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r1.y, 0)

        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r2.height, 10)
        self.assertEqual(self.r2.x, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r2.id, 2)

        self.assertEqual(self.r3.id, 12)
        self.assertEqual(self.r3.x, 0)
        self.assertEqual(self.r3.id, 12)
        self.assertEqual(self.r3.id, 12)
        self.assertEqual(self.r3.id, 12)
        self.assertEqual(self.r3.id, 12)

        self.assertEqual(self.r4.id, 3)
        self.assertEqual(self.r5.id, 4)
        self.assertEqual(self.r6.id, 5)
        self.assertEqual(self.r7.id, "string")
        self.assertEqual(self.r8.id, 4.5)
        self.assertEqual(self.r9.id, True)

    def test_init_raise_error(self):
        ''' Checks that TypeErrors were raised '''
        self.assertRaises(TypeError, Rectangle, 1)
        self.assertRaises(TypeError, Rectangle, 1, None)
        self.assertRaises(TypeError, Rectangle, None, None)
        self.assertRaises(TypeError, Rectangle, 'string', 2)
        self.assertRaises(TypeError, Rectangle, 1, 'string')
        self.assertRaises(ValueError, Rectangle, 1, 2, -1)
        self.assertRaises(TypeError, Rectangle)
        self.assertRaises(TypeError, Rectangle, 1.0, 2.1)

    def test_area(self):
        ''' Tests for correctness of the rectangle area '''
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r2.area(), 20)
        self.assertEqual(self.r3.area(), 20)
        self.assertNotEqual(self.r4.area(), 36)
        self.assertEqual(self.r5.area(), 2)
        self.assertEqual(self.r6.area(), 6)
        self.assertEqual(self.r7.area(), 6)
        self.assertEqual(self.r8.area(), 6)
        self.assertEqual(self.r9.area(), 6)

    def test_update(self):
        """ Tests for the update method """
        self.r1.update(8, 10, 3, 2, 20)

        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 3)
        self.assertEqual(self.r1.x, 2)
        self.assertEqual(self.r1.y, 20)
        self.assertEqual(self.r1.id, 8)

        self.r1.update(width=15, y=5)

        self.assertEqual(self.r1.width, 15)
        self.assertEqual(self.r1.y, 5)
        """ Ensure other attributes remain unchanged """
        self.assertEqual(self.r1.height, 3)
        self.assertEqual(self.r1.x, 2)
        self.assertEqual(self.r1.id, 8)

    def test_update_raise_error(self):
        """
        Tests for errors raised when invalid inputs are
        parsed into the update method
        """
        self.assertRaises(TypeError, self.r1.update, "valid", None)
        self.assertRaises(TypeError, self.r1.update, "valid", 20, "True")
        self.assertRaises(TypeError, self.r1.update, "valid", 23, 20, 0.1)
        self.assertRaises(TypeError, self.r1.update, "valid", 23, 20, 5, 0.3)
        self.assertRaises(ValueError, self.r1.update, '#', -2)
        self.assertRaises(ValueError, self.r1.update, '#', 2, -1)
        self.assertRaises(ValueError, self.r1.update, '#', 2, 1, -1)
        self.assertRaises(ValueError, self.r1.update, '#', 2, 1, 5, -5)

    def test_str(self):
        """ Tests for the overidding __str__ method """
        self.r1.update(4, 6, 2, 1, 12)
        self.assertEqual(str(self.r1), "[Rectangle] (4) 1/12 - 6/2")

    def test_to_dictionary(self):
        """ Tests for the dictionary representation of a square instance """
        self.assertEqual(
                self.r1.to_dictionary(),
                {'x': 0, 'y': 0, 'id': 1, 'height': 2, 'width': 10}
                )
        self.assertEqual(
                self.r2.to_dictionary(),
                {'x': 0, 'y': 0, 'id': 2, 'height': 10, 'width': 2}
                )
        self.assertEqual(
                self.r3.to_dictionary(),
                {'x': 0, 'y': 0, 'id': 12, 'height': 2, 'width': 10}
                )
        self.assertEqual(
                self.r4.to_dictionary(),
                {'x': 0, 'y': 0, 'id': 3, 'height': 7, 'width': 5}
                )
        self.assertEqual(
                self.r5.to_dictionary(),
                {'x': 2, 'y': 3, 'id': 4, 'height': 2, 'width': 1}
                )
        self.assertEqual(
                self.r6.to_dictionary(),
                {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 3}
                )
        self.assertEqual(
                self.r7.to_dictionary(),
                {'x': 1, 'y': 9, 'id': 'string', 'height': 2, 'width': 3}
                )
        self.assertEqual(
                self.r8.to_dictionary(),
                {'x': 1, 'y': 9, 'id': 4.5, 'height': 2, 'width': 3}
                )
        self.assertEqual(
                self.r9.to_dictionary(),
                {'x': 1, 'y': 9, 'id': True, 'height': 2, 'width': 3}
                )

    def test_to_json_string(self):
        self.assertEqual(
            Base.to_json_string(
                [self.r1.to_dictionary(), self.r2.to_dictionary()]
            ),
            '[{"x": 0, "y": 0, "id": 1, "height": 2, "width": 10}, '
            '{"x": 0, "y": 0, "id": 2, "height": 10, "width": 2}]'
            )

        self.assertEqual(
            Base.to_json_string(
                [
                    self.r1.to_dictionary()
                ]
            ),
            '[{"x": 0, "y": 0, "id": 1, "height": 2, "width": 10}]'
            )

        self.assertEqual(
            Base.to_json_string(
                [
                    self.r1.to_dictionary(),
                    self.r2.to_dictionary(),
                    self.r3.to_dictionary(),
                    self.r4.to_dictionary()
                ]
            ),
            '[{"x": 0, "y": 0, "id": 1, "height": 2, "width": 10}, '
            '{"x": 0, "y": 0, "id": 2, "height": 10, "width": 2}, '
            '{"x": 0, "y": 0, "id": 12, "height": 2, "width": 10}, '
            '{"x": 0, "y": 0, "id": 3, "height": 7, "width": 5}]'
            )

    def test_type(self):
        self.assertEqual(type(self.r8.to_dictionary()), dict)
        self.assertEqual(
                    type(Base.to_json_string(
                        [self.r1.to_dictionary(), self.r2.to_dictionary()]
                    )), str)

    def test_save_square_to_file(self):
        """
        Test saving a list of Square objects to a file.
        """
        Rectangle.save_to_file([self.r1, self.r2])

        with open("Rectangle.json", "r") as file:
            content = file.read()

        expected_json = json.dumps(
                [self.r1.to_dictionary(), self.r2.to_dictionary()]
                )
        self.assertEqual(content, expected_json)

        """ Clean up by removing the file after the test """
        os.remove("Rectangle.json")

    def test_save_empty_list(self):
        """
        Test saving an empty list of objects to a file.
        """
        Rectangle.save_to_file([])

        self.assertTrue(os.path.exists("Square.json"))

    def test_save_to_file_with_None(self):
        """
        Test saving a list with None object to a file.
        """
        self.assertRaises(TypeError, Rectangle.save_to_file, None)
