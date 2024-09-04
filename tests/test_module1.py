# tests/test_math_operations.py

import unittest
from src.nonstandardcode import sum

class TestMathOperations(unittest.TestCase):

    def test_sum_positive_numbers(self):
        self.assertEqual(sum(1, 2), 3)
    
    def test_sum_negative_numbers(self):
        self.assertEqual(sum(-1, -2), -3)
    
    def test_sum_positive_and_negative(self):
        self.assertEqual(sum(-1, 2), 1)

    def test_sum_with_zero(self):
        self.assertEqual(sum(0, 5), 5)
        self.assertEqual(sum(5, 0), 5)

if __name__ == '__main__':
    unittest.main()
