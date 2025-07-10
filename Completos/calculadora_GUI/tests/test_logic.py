# Archivo test_logic.py

# IMPORTS --------------------------------------------------------

import unittest
from core.calculator_logic import evaluate_expression

# CLASS ----------------------------------------------------------
class TestCalculatorLogic(unittest.TestCase):
    def test_addition(self):
        result, error = evaluate_expression("2+3")
        self.assertEqual(result, 5)
        self.assertIsNone(error)

    def test_division_by_zero(self):
        result, error = evaluate_expression("5/0")
        self.assertIsNotNone(error)
        self.assertEqual(error, "Cannot divide by zero")

    def test_invalid_expression(self):
        result, error = evaluate_expression("5++")
        self.assertIsNotNone(error)

    def test_multiplication(self):
        result, error = evaluate_expression("4*2")
        self.assertEqual(result, 8)
# MAIN -----------------------------------------------------------
if __name__ == "__main__":
    unittest.main()