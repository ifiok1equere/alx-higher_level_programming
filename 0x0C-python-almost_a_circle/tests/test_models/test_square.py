#!/usr/bin/python3
"""This module define a test suite"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
import sys


class TestSquare(unittest.TestCase):
    """This class defines series test suite"""

    def setUp(self):
        """This method creates Rectangle class instances"""

        self.s1 = Square(5)
        self.s2 = Square(2, 2)
        self.s3 = Square(3, 1, 3)
        self.s4 = Square(9, 7, 5, 12)

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

        self.assertEqual(self.s1.__class__.__name__, "Square")
        self.assertEqual(type(self.s1), Square)
        self.assertIsInstance(self.s1, Square)
        self.assertIsInstance(self.s1, Rectangle)
        self.assertIsInstance(self.s1, Base)

    def test_inheritance(self):
        """This method tests for inheritance"""

        self.assertTrue(issubclass(Square, Rectangle))
        self.assertTrue(issubclass(Square, Base))

    def test_attribute(self):
        """Test to ensure attribute is correctly instantiated"""

        self.assertFalse(hasattr(self.s1, 'size'))
        self.assertTrue(hasattr(self.s1, 'id'))
        self.assertTrue(hasattr(self.s1, 'width'))
        self.assertTrue(hasattr(self.s1, 'height'))
        self.assertTrue(hasattr(self.s1, 'x'))
        self.assertTrue(hasattr(self.s1, 'y'))

    def test_unique_attribute_values(self):
        """The method tests if unique id' are created for each instance"""

        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 2)
        self.assertEqual(self.s1.width, 5)
        self.assertEqual(self.s1.height, 5)
        self.assertEqual(self.s2.width, 2)
        self.assertEqual(self.s2.height, 2)
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s1.y, 0)

    def test_custom_attribute_values(self):
        """This method tests if instances have a custom id when id is not
        None"""

        self.assertEqual(self.s4.id, 12)
        self.assertEqual(self.s2.x, 2)
        self.assertEqual(self.s3.y, 3)
        self.assertEqual(self.s3.id, 3)
        self.assertEqual(self.s4.x, 7)
        self.assertEqual(self.s4.y, 5)

    def test_incremental_id(self):
        """This method tests if the id attribute is incremented correctly"""

        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 2)
        self.assertEqual(self.s3.id, 3)
        self.assertEqual(self.s4.id, 12)

    def test_input_validation(self):
        """This method tests for valid inputs during class instantiation"""

        # Test suite for TypeError
        with self.assertRaises(TypeError):
            self.s4 = Square(1.035, 2)
        with self.assertRaises(TypeError):
            self.s5 = Square(3.5, 2)
        with self.assertRaises(TypeError):
            self.s6 = Square(15, "equere")
        with self.assertRaises(TypeError):
            self.s7 = Square(15, 16.9)
        with self.assertRaises(TypeError):
            self.s8 = Square(15.0, 16.9)
        with self.assertRaises(TypeError):
            self.s9 = Square("ifiok", "equere")
        with self.assertRaises(TypeError):
            self.s10 = Square("1", 2)
        with self.assertRaises(TypeError):
            self.s11 = Square(8, "2")
        with self.assertRaises(TypeError):
            self.s12 = Square("0", "0")
        with self.assertRaises(TypeError):
            self.s13 = Square()
        with self.assertRaises(TypeError):
            self.s13 = Square(None)
        with self.assertRaises(TypeError):
            self.s14 = Square(3, 2, "2", 3)
        with self.assertRaises(TypeError):
            self.s15 = Square(3, 2, "3")
        with self.assertRaises(TypeError):
            self.s16 = Square(3, 2, "2", "3")
        with self.assertRaises(TypeError):
            self.s17 = Square(3, 2, "2", "3")
        with self.assertRaises(TypeError):
            self.s30 = Square(5, 6, None, -3, )
        with self.assertRaises(TypeError):
            self.s31 = Square(5, 6, [2])
        with self.assertRaises(TypeError):
            self.s32 = Square(5, 6, {}, 4)
        with self.assertRaises(TypeError):
            self.s34 = Square("", 6, "", 4)
        with self.assertRaises(TypeError):
            self.s35 = Square("", 6, 7, 54)
        with self.assertRaises(TypeError):
            self.s36 = Square(5, 6, "")
        with self.assertRaises(TypeError):
            self.s37 = Square(None, 6, 7, 3)
        with self.assertRaises(TypeError):
            self.s38 = Square(1, None, 7, 0)
        with self.assertRaises(TypeError):
            self.s40 = Square("wisdom")
        with self.assertRaises(TypeError):
            self.s45 = Square({})
        with self.assertRaises(TypeError):
            self.s28 = Square(5, "6, 8", -5)

        # Test suite for ValueError
        with self.assertRaises(ValueError):
            self.s18 = Square(-1, 2)
        with self.assertRaises(ValueError):
            self.s19 = Square(1, -2)
        with self.assertRaises(ValueError):
            self.s20 = Square(-1, -2)
        with self.assertRaises(ValueError):
            self.s21 = Square(0, 2)
        with self.assertRaises(ValueError):
            self.s22 = Square(0, 0)
        with self.assertRaises(ValueError):
            self.s23 = Square(0, 0)
        with self.assertRaises(ValueError):
            self.s24 = Square(5, -6, 0, 3)
        with self.assertRaises(ValueError):
            self.s25 = Square(5, 6, -4, 0)
        with self.assertRaises(ValueError):
            self.s26 = Square(-5, -6, -4, -1)
        with self.assertRaises(ValueError):
            self.s27 = Square(-5, -6, -3, -7)
        with self.assertRaises(ValueError):
            self.s29 = Square(5, 6, -2, -3)

        try:
            self.s = Square(10, "2")
        except Exception as e:
            self.assertEqual(str(e), "x must be an integer")

        try:
            self.s = Square(10, 2)
            self.s.width = -10
        except Exception as e:
            self.assertTrue(str(e) == "width must be > 0")

        try:
            self.s = Square(10, 2)
            self.s.x = {}
        except Exception as e:
            self.assertTrue(str(e) == "x must be an integer")

        try:
            self.s = Square(10, 2, -3, -1)
        except Exception as e:
            self.assertTrue(str(e) == "y must be >= 0")

    def test_display(self):
        """Test for correct square display"""

        # Test for s1 instance
        # create StringIO object
        std_out_capture = StringIO()
        # re-direct stdout to StringIO object
        sys.stdout = std_out_capture
        # call method to print to stdout (i.e to StringIO object)
        self.s1.display()
        # store stdout in a variable after stripping trailing newline character
        printed_output = std_out_capture.getvalue().rstrip('\n')
        # output to be tested against
        expected_output = "#####\n#####\n#####\n#####\n#####"
        self.assertEqual(printed_output, expected_output)

        # Test for s2 instance
        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        self.s2.display()
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "  ##\n  ##"
        self.assertEqual(printed_output, expected_output)

        # Test for s3 instance
        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        self.s3.display()
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "\n\n\n ###\n ###\n ###"
        self.assertEqual(printed_output, expected_output)

        # reset stdout to terminal output
        sys.stdout = sys.__stdout__

    def test_str(self):
        """This method tests for the unofficial string rep of the square
        object
        """

        # Test for s1 instance
        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        print(self.s1)
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "[Square] (1) 0/0 - 5"
        self.assertEqual(printed_output, expected_output)

        # Test for s2 instance
        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        print(self.s2)
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "[Square] (2) 2/0 - 2"
        self.assertEqual(printed_output, expected_output)

        # Test for s3 instance
        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        print(self.s3)
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "[Square] (3) 1/3 - 3"
        self.assertEqual(printed_output, expected_output)

        # reset stdout to terminal output
        sys.stdout = sys.__stdout__

    def test_dispay_updated(self):
        """This method tests for the updated square display method
        """

        # Reset class variable _nd_instance so id count is not affected
        # with new instance creation
        self.tearDown()

        self.s1 = Square(2, 3, 2, 2)
        self.s2 = Square(3, 2, 1, 0)
        self.s3 = Square(2, 3)
        self.s4 = Square(3, 2, 0, 2)
        self.s5 = Square(3, 2, 2)

        # Test for s1 instance
        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        self.s1.display()
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "\n\n   ##\n   ##"
        self.assertEqual(printed_output, expected_output)

        # Test for s2 instance
        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        self.s2.display()
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "\n  ###\n  ###\n  ###"
        self.assertEqual(printed_output, expected_output)

        # Test for s3 instance
        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        self.s3.display()
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "   ##\n   ##"
        self.assertEqual(printed_output, expected_output)

        # Test for s4 instance
        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        self.s4.display()
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "  ###\n  ###\n  ###"
        self.assertEqual(printed_output, expected_output)

        # Test for s5 instance
        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        self.s5.display()
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "\n\n  ###\n  ###\n  ###"
        self.assertEqual(printed_output, expected_output)

        # reset stdout to terminal output
        sys.stdout = sys.__stdout__
