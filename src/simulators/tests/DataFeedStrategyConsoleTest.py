import os
import unittest

from src.command_connectors.ConsoleTextConnector import ConsoleTextConnector
from src.loaders import CsvLoader, DataFeed
from src.simulators.RandomEntryStrategy import RandomEntryStrategy

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

local_path = __location__.split("src\\", 1)[0]
example_data_path_1 = str(local_path)+"src/example_data/DAT_MT_EURUSD_M1_201908.csv"
example_data_path_2 = str(local_path)+"src/example_data/DAT_ASCII_EURUSD_M1_2018.csv"

class DataFeedStrategyConsoleTest(unittest.TestCase):
    def test_connected_trio_static_data(self):
        print("\nTest of DataFeed connected to cvs file, with ConsoleTextConnector")
        data = CsvLoader(example_data_path_1).load_data()
        if data is not None:
            print("Data loaded")
        data_feed = DataFeed(data)
        print("Data feed created")
        command_connector = ConsoleTextConnector()
        random_entry_strategy = RandomEntryStrategy(command_connector)
        data_feed.subscribe_strategy(random_entry_strategy)
        data_feed.run()
        print("*******************************************\n")
        pass


if __name__ == '__main__':
    unittest.main()
