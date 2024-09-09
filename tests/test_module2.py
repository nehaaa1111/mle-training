import unittest

import pandas as pd

from PricePrediction.train import (
    train_decision_tree,
    train_linear_regression,
    train_random_forest_1,
    train_random_forest_2,
)


class TestModelTraining(unittest.TestCase):
    def setUp(self):
        # sample DataFrame
        data = {
            "median_income": [4.0, 2.0, 1.0, 3.0, 5.0],
            "total_rooms": [500, 100, 300, 200, 600],
            "households": [80, 20, 10, 40, 50],
            "total_bedrooms": [2, 5, 10, 4, 40],
            "population": [500, 100, 250, 200, 100],
            "ocean_proximity": [0, 1, 1, 1, 0],
            "median_house_value": [300000, 350000, 100000, 250000, 400000],
        }
        self.training_data = pd.DataFrame(data)

    def test_train_random_forest_1(self):
        model = train_random_forest_1(self.training_data)
        self.assertIsNotNone(model)

    def test_train_random_forest_2(self):
        model = train_random_forest_2(self.training_data)
        self.assertIsNotNone(model)

    def test_train_linear_regression(self):
        model = train_linear_regression(self.training_data)
        self.assertIsNotNone(model)

    def test_train_decision_tree(self):
        model = train_decision_tree(self.training_data)
        self.assertIsNotNone(model)


if __name__ == "__main__":
    unittest.main()

