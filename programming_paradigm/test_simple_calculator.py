import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.addition(2, 3), 5)
        self.assertEqual(self.calc.addition(-1, 1), 0)
        self.assertEqual(self.calc.addition(0, 0), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtraction(10, 5), 5)
        self.assertEqual(self.calc.subtraction(-1, 1), -2)
        self.assertEqual(self.calc.subtraction(0, 0), 0)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiplication(3, 5), 15)
        self.assertEqual(self.calc.multiplication(-1, 1), -1)
        self.assertEqual(self.calc.multiplication(0, 100), 0)

    def test_division(self):
        self.assertEqual(self.calc.division(10, 2), 5)
        self.assertEqual(self.calc.division(-10, 2), -5)
        self.assertEqual(self.calc.division(0, 1), 0)
        self.assertEqual(self.calc.division(10, 0), "Error: Division by zero is not allowed.")
        
if __name__ == '__main__':
    unittest.main()
