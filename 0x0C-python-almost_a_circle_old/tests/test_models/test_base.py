#!/usr/bin/python3
""" This module tests"""
import json
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    This class conducts test
    on the the Base class.
    """

    def setUp(self):
        """ Create multiple objects of the Base class for testing """
        Base._Base__nb_objects = 0
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
        self.b14 = Base(0.564)
        self.b15 = Base()
        self.b16 = Base()
        self.b17 = Base()

    def tearDown(self):
        """ Clean up by deleting the objects after each test """
        del self.b1
        del self.b2
        del self.b3
        del self.b4
        del self.b5
        del self.b6
        del self.b7
        del self.b8
        del self.b9
        del self.b10
        del self.b11
        del self.b12
        del self.b13
        del self.b14
        del self.b15
        del self.b16
        del self.b17

    def test_id_increment(self):
        """
        Test if the IDs are incremented properly for each object created
        """
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b5.id, 4)
        self.assertEqual(self.b11.id, 5)
        self.assertEqual(self.b12.id, 6)
        self.assertEqual(self.b15.id, 7)
        self.assertEqual(self.b16.id, 8)
        self.assertEqual(self.b17.id, 9)

    def test_custom_id(self):
        """ Test if the object with a custom ID is created correctly """
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b6.id, -1)
        self.assertEqual(self.b7.id, -2)
        self.assertEqual(self.b8.id, 2)
        self.assertEqual(self.b9.id, 0)
        self.assertEqual(self.b10.id, 23)
        self.assertEqual(self.b13.id, 'Ehiz')
        self.assertEqual(self.b14.id, 0.564)

    def test_json_serialization(self):
        """ Test if the object can be serialized to JSON correctly """
        obj_dict = {"id": self.b1.id}
        json_str = json.dumps(obj_dict)
        self.assertEqual(json.loads(json_str), obj_dict)

    def test_default_id_generation(self):
        """ Test if the default ID is generated correctly """
        obj_without_id = Base()
        self.assertNotEqual(obj_without_id.id, 5)
