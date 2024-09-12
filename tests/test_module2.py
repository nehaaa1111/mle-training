"""
Unit tests for the model training functions in the PricePrediction package.

This module contains unit tests for various machine learning model training functions 
from the `PricePrediction.train` module, including decision tree, linear regression, 
and random forest models.

Classes
-------
TestModelTraining : unittest.TestCase
    Unit tests for model training functions, ensuring they return non-null models.

Methods
-------
setUp()
    Sets up the training data for the tests.
test_train_random_forest_1()
    Tests the random forest training function (version 1) to ensure it returns a valid model.
test_train_random_forest_2()
    Tests the random forest training function (version 2) to ensure it returns a valid model.
test_train_linear_regression()
    Tests the linear regression training function to ensure it returns a valid model.
test_train_decision_tree()
    Tests the decision tree training function to ensure it returns a valid model.
"""
import unittest
import pandas as pd

from PricePrediction.train import (
    train_decision_tree,
    train_linear_regression,
    train_random_forest_1,
    train_random_forest_2,
)


class TestModelTraining(unittest.TestCase):
    """
    Unit tests for machine learning model training functions in `PricePrediction.train`.

    The test cases ensure that the model training functions return valid trained models 
    (i.e., they are not `None`).

    Methods
    -------
    setUp()
        Initializes a sample training dataset for the tests.
    test_train_random_forest_1()
        Tests the `train_random_forest_1` function with the sample data.
    test_train_random_forest_2()
        Tests the `train_random_forest_2` function with the sample data.
    test_train_linear_regression()
        Tests the `train_linear_regression` function with the sample data.
    test_train_decision_tree()
        Tests the `train_decision_tree` function with the sample data.
    """

    def setUp(self):
        """
        Set up the test data for training models.

        This method initializes a pandas DataFrame with sample housing data, including features 
        such as `median_income`, `total_rooms`, `households`, `total_bedrooms`, `population`, 
        `ocean_proximity`, and `median_house_value`. The data is used to test the model training functions.
        """
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
        """
        Test the random forest training function (version 1).

        This test checks that the `train_random_forest_1` function successfully trains a model
        using the sample data and returns a valid model (not `None`).

        Raises
        ------
        AssertionError
            If the returned model is `None`.
        """
        model = train_random_forest_1(self.training_data)
        self.assertIsNotNone(model)

    def test_train_random_forest_2(self):
        """
        Test the random forest training function (version 2).

        This test checks that the `train_random_forest_2` function successfully trains a model
        using the sample data and returns a valid model (not `None`).

        Raises
        ------
        AssertionError
            If the returned model is `None`.
        """
        model = train_random_forest_2(self.training_data)
        self.assertIsNotNone(model)

    def test_train_linear_regression(self):
        """
        Test the linear regression training function.

        This test checks that the `train_linear_regression` function successfully trains a model
        using the sample data and returns a valid model (not `None`).

        Raises
        ------
        AssertionError
            If the returned model is `None`.
        """
        model = train_linear_regression(self.training_data)
        self.assertIsNotNone(model)

    def test_train_decision_tree(self):
        """
        Test the decision tree training function.

        This test checks that the `train_decision_tree` function successfully trains a model
        using the sample data and returns a valid model (not `None`).

        Raises
        ------
        AssertionError
            If the returned model is `None`.
        """
        model = train_decision_tree(self.training_data)
        self.assertIsNotNone(model)


if __name__ == "__main__":
    unittest.main()
