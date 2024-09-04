# tests/test_module1.py

import unittest

import pandas as pd  # type: ignore

from src.nonstandardcode import income_cat_proportions


class TestIncomeCatProportions(unittest.TestCase):

    def setUp(self):
        """Set up a simple DataFrame for testing."""
        self.data = pd.DataFrame({
            "income_cat": 
            ["high", "medium", "high", "low",
                "medium", "medium", "low", "high"]
        })

    def test_income_cat_proportions(self):
        """Test the income_cat_proportions function."""
        result = income_cat_proportions(self.data)
        expected = pd.Series({
            "high": 0.375,
            "medium": 0.375,
            "low": 0.25
        })
        pd.testing.assert_series_equal(result, expected)


if __name__ == "__main__":
    unittest.main()
