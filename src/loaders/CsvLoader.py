from typing import Dict
import pandas as pd
import datetime

default_params = {
    "date": 0,
    "datetime": 1,
    "open": 2,
    "high": 3,
    "low": 4,
    "close": 5,
    "volume": -1}


default_transformations = {
    "date": '%Y.%m.%d',
    "datetime": '%H:%M'
}


class CsvLoader:
    """Class for opening csv files"""

    def __init__(self,
                 path,
                 params: Dict[str, int] = default_params,
                 data_transformations: Dict[str, str] = default_transformations):
        """
        :param path: path to csv file
        :param params: types of data that is writen in csv file with number of columns,
            -1 means that this data is not in file
        :param data_transformations: Allows for specification of data formatting in file, to parse it to datetime object
        """
        self.loading_params = params
        self.path = path
        self.data_transformations = data_transformations

    def load_data(self):
        """
        :return: Dictionary with arrays of data from csv file, after all transformations
        """
        raw_data = pd.read_csv(self.path)
        data = {}
        for key in self.loading_params.keys():
            if self.loading_params[key] > -1:
                if key not in self.data_transformations.keys():
                    data[key] = raw_data.values[:, self.loading_params[key]]
                else:
                    data[key] = [datetime.datetime.strptime(x, self.data_transformations[key])
                                 for x in raw_data.values[:, self.loading_params[key]]]
        return data


