"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_int_arguments(self):
        input = [1, 5, 10, 4]
        expected = 10
        self.assertEqual(max_integer(input), expected)

    def test_negative_arguments(self):
        input = [-2, -4, -6, -8]
        expected = -2
        self.assertEqual(max_integer(input), expected)

    def test_zero_arguments(self):
        input = [0, 0, 0, 0]
        expected = 0
        self.assertEqual(max_integer(input), expected)

    def test_empty_input(self):
        self.assertIsNone(max_integer())

if __name__ == "__main__":
    unittest.main()
