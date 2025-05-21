import unittest
from src.data_processing import load_data, clean_data
import pandas as pd

class TestDataProcessing(unittest.TestCase):

    def setUp(self):
        self.test_file = 'data/stock_data.csv'
        self.df = load_data(self.test_file)

    def test_load_data(self):
        self.assertIsInstance(self.df, pd.DataFrame)
        self.assertFalse(self.df.empty)

    def test_clean_data(self):
        cleaned_df = clean_data(self.df)
        self.assertTrue(cleaned_df.isnull().sum().sum() == 0)

if __name__ == '__main__':
    unittest.main()