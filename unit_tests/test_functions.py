from unittest import TestCase
from functions import divide, multiply


class TestFunctions(TestCase):
    def test_divide_result(self):
        dividend = 15
        divisor=3
        expected_result = 5.0
        self.assertEqual(divide(dividend, divisor), expected_result)

    def test_divide_negative(self):
        dividend = 15
        divisor = -3
        expected_result = -5.0
        self.assertEqual(divide(dividend, divisor), expected_result)

    # def test_divide_error_on_zero(self):
    #     with self.assertRaises(ValueError):
    #         divide(25,0)

    def test_multiply_empty(self):
        with self.assertRaises(ValueError):
            multiply()

    def test_multiply_empty(self):
        inputs = (3,5)
        expected_result = 15
        self.assertEqual(multiply(*inputs), expected_result)

    def test_multiply_empty(self):
        inputs = (3,5,0)
        expected_result = 0
        self.assertEqual(multiply(*inputs), expected_result)