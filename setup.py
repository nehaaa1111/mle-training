# tests/test_nonstandardcode.py

import unittest
import pandas as pd
from src.nonstandardcode import fetch_housing_data
from src.nonstandardcode import load_housing_data, prepare_data, train_model


class TestHousingData(unittest.TestCase):

    def setUp(self):
        # Create a small mock dataset
        data = {
            'median_income': [1.0, 2.0, 3.0, 4.0, 5.0],
            'total_rooms': [1000, 1500, 2000, 2500, 3000],
            'households': [300, 400, 500, 600, 700],
            'total_bedrooms': [200, 300, 400, 500, 600],
            'population': [800, 900, 1000, 1100, 1200],
            'ocean_proximity': ['NEAR BAY', 'INLAND', 'NEAR OCEAN',
                                'ISLAND', 'NEAR BAY']
        }
        self.housing = pd.DataFrame(data)
        self.train_set, self.test_set = prepare_data(self.housing)

    def test_load_data(self):
        # Test if the data loading works
        fetch_housing_data()
        data = load_housing_data()
        self.assertIsInstance(data, pd.DataFrame)

    def test_prepare_data(self):
        # Test if data preparation works
        self.assertEqual(len(self.train_set), 4)  # Example
        self.assertEqual(len(self.test_set), 1)   # Example

    def test_train_model(self):
        # Test if the model training works
        housing_prepared = self.train_set.drop("median_house_value", axis=1)
        housing_labels = self.train_set["median_house_value"].copy()
        lin_rmse, lin_mae = train_model(housing_prepared, housing_labels)
        self.assertIsInstance(lin_rmse, float)
        self.assertIsInstance(lin_mae, float)


if __name__ == '__main__':
    unittest.main()
