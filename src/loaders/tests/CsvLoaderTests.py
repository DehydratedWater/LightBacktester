import os
import unittest

from src.loaders.CsvLoader import CsvLoader

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

example_data_path_1 = os.path.join(__location__, "DAT_MT_EURUSD_M1_201908.csv")
example_data_path_2 = os.path.join(__location__, "DAT_ASCII_EURUSD_M1_2018.csv")


class CsvLoaderTest(unittest.TestCase):

    def test_loading_files(self):
        print("\nTest for file opening")
        f = open(example_data_path_1, "r")
        print("File path: ", example_data_path_1)
        contents = f.read()
        print(contents[:100])
        f.close()
        print("*********************************\n")
        self.assertEqual(1, 1)

    def test_loading_default_file(self):
        print("\nTest loading data from default csv file")
        data = CsvLoader(example_data_path_1).load_data()
        for key in data.keys():
            print(key, " -> ", data[key][:5])
        print("*********************************\n")


    def test_loading_custom_file(self):
        print("\nTest loading data from custom csv file")
        custom_params = {
            "date": -1,
            "datetime": 0,
            "open": 1,
            "high": 2,
            "low": 3,
            "close": 4,
            "volume": 5}
        data = CsvLoader(example_data_path_2, params=custom_params, data_transformations={}).load_data()
        for key in data.keys():
            print(key, " -> ", data[key][:5])
        print("*********************************\n")



if __name__ == '__main__':
    unittest.main()


