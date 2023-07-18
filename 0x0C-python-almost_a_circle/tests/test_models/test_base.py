#!/usr/bin/python3
""" This module tests"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    This class conducts test
    on the the Base class.
    """

    def setUp(self):
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.b4 = Base(12)
        self.b5 = Base()
        self.b6 = Base(-1)
        self.b7 = Base(-2)
        self.b8 = Base(2)
        self.b9 = Base(0)
        self.b10 = Base(23)
        self.b11 = Base()
        self.b12 = Base(None)
        self.b13 = Base('Ehiz')

    def tearDown(self):
        self.b1 = None
        self.b2 = None
        self.b3 = None
        self.b4 = None
        self.b5 = None
        self.b6 = None
        self.b7 = None
        self.b8 = None
        self.b9 = None
        self.b10 = None
        self.b11 = None
        self.b12 = None
        self.b13.id = 0

    def test_base(self):
        """ The method tests the Base class atrributes """
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, 4)
        self.assertEqual(self.b6.id, -1)
        self.assertEqual(self.b7.id, -2)
        self.assertEqual(self.b8.id, 2)
        self.assertEqual(self.b9.id, 0)
        self.assertEqual(self.b10.id, 23)
        self.assertEqual(self.b11.id, 5)
        self.assertEqual(self.b12.id, 6)
        self.assertEqual(self.b13.id, "Ehiz")
