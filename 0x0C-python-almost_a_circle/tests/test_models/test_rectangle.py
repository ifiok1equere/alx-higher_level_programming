#!/usr/bin/python3
""" This module conducts unittests tests"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    This class conducts test
    on the the Retangle class.
    """

    def setUp(self):
        """ The method sets up objects """
        super().setUp()
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10)
        self.r3 = Rectangle(10, 2, 0, 0, 12)
        self.r4 = Rectangle(5, 7)
        self.r5 = Rectangle(1, 2, 2, 3)
        self.r6 = Rectangle(3, 2, 1, 9, None)
        self.r7 = Rectangle(3, 2, 1, 9, "string")
        self.r8 = Rectangle(3, 2, 1, 9, 4.5)
        self.r9 = Rectangle(3, 2, 1, 9, True)

    def tearDown(self):
        super().tearDown()
        self.r1 = None
        self.r2 = None
        
    def test_init(self):
        """ The method tests the Base & Rectangle class atrributes """
        self.assertEqual(self.r1.id, 6)
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r1.y, 0)

        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r2.height, 10)
        self.assertEqual(self.r2.x, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r2.id, 7)

        self.assertEqual(self.r3.id, 12)
        self.assertEqual(self.r3.x, 0)
        self.assertEqual(self.r3.id, 12)
        self.assertEqual(self.r3.id, 12)
        self.assertEqual(self.r3.id, 12)
        self.assertEqual(self.r3.id, 12)
        
        self.assertEqual(self.r4.id, 8)
        self.assertEqual(self.r5.id, 9)
        self.assertEqual(self.r6.id, 10)
        self.assertEqual(self.r7.id, "string")
        self.assertEqual(self.r8.id, 4.5)
        self.assertEqual(self.r9.id, True)
"""
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
    
    def test_area_raise_error(self):
        self.assertRaises(ValueError, self.r1.area(), -20)

    def test_display(self):
        pass

    def test_str(self):
        self.assertEqual(self.r1.__str__, "[Rectangle] (10) 0/0 - 10/2")
"""
