#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """This class defines a test for the
    aforementioned function in which case
    we are trying to find out what the 
    maximum number in a list is"""

    list_1 = [1, 2, 3, 4]
    list_2 = [1, 5.6, 4, 2.2]
    list_3 = ['a', 1, 3, 5]
    list_4 = ['a', 'b', 'c']
    list_5 = ["string", "dove", 1000]
    list_6 = [True, False, 6, 's']
    list_7 = [True, False]

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_max_integer(self):
        self.assertEqual(max_integer(self.list_1), 4)
        self.assertEqual(max_integer(self.list_2), 5.6)
        self.assertNotEqual(max_integer(self.list_4), 'b')
        self.assertEqual(max_integer(self.list_7), True)
        self.assertEqual(max_integer(), None)

    def test_values(self):
        self.assertRaises(TypeError, max_integer, self.list_3)
        self.assertRaises(TypeError, max_integer, self.list_5)
        self.assertRaises(TypeError, max_integer, self.list_6)
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, "Ifiok")
