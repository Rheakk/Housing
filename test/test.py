import unittest
import logging
import os
from Housing.GetData import load_housing_data, fetch_housing_data


class TestHousing(unittest.TestCase):

    def setUp (self):
        logging.getLogger().setLevel (logging.INFO)
        
    def test_fetch_data(self):
        expectedFile = os.path.join (os.environ["DATA_DIR"], "housing.csv")
        self.assertEqual (fetch_housing_data (), expectedFile)

    def test_load_data(self):
        housing = load_housing_data ()
        # usually the data downloaded as about 20K rows in it
        self.assertGreater(housing.longitude.data.shape[0], 20000, "Failed to downloaded enough data")

if __name__ == '__main__':
    unittest.main()
    
