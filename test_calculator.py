import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(5, 10), 15)
    def test_add_with_negative_number(self):
        self.assertEqual(self.calc.add(10, -5), 5)

    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
    def test_subtract_to_negative_result(self):
        self.assertEqual(self.calc.subtract(3, 8), -5)

    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(10, 0), 0)

    def test_divide_simple(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
    def test_divide_with_remainder(self):
        self.assertEqual(self.calc.divide(7, 3), 2)

    def test_modulo_simple(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)
    def test_modulo_zero_remainder(self):
        self.assertEqual(self.calc.modulo(10, 2), 0)

if __name__ == '__main__':
    unittest.main()