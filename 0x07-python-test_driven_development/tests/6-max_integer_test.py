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

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_max_integer(self):
        """ This is a function test """

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 5.6, 4, 2.2]), 5.6)
        self.assertNotEqual(max_integer(['a', 'b', 'c']), 'b')
        self.assertEqual(max_integer([True, False]), True)
        self.assertEqual(max_integer(), None)
        self.assertIsNone(max_integer())
        self.assertIsNotNone(max_integer([3]))
        self.assertEqual(max_integer([3]), 3)
        self.assertIsInstance(max_integer([3, 5, 5.0]), int)
        self.assertNotIsInstance(max_integer(['b', 'g', 'z']), int)
        self.assertEqual(max_integer([5, 5.0]), 5.0)
        
        with self.assertRaises(TypeError):
            max_integer('a', 1, 3, 5)
            max_integer(["string", "dove", 1000])
            max_integer([True, False, 6, 's'])
            max_integer(None)
            max_integer("Ifiok")
            max_integer((1, 2, 'ifiok'))
            max_integer({"key": "value", "value": "key"})


