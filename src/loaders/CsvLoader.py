from typing import Dict
import pandas as pd


default_params = {
    "date": 0,
    "datetime": 1,
    "open": 2,
    "high": 3,
    "low": 4,
    "close": 5,
    "volume": -1}


class CsvLoader:
    """Class for opening csv files"""

    def __init__(self, path, params: Dict[str, int] = default_params):
        self.loading_params = params
        self.path = path

    def load_data(self):
        raw_data = pd.read_csv(self.path)
        data = {}
        for key in self.loading_params.keys():
            if self.loading_params[key] > -1:
                data[key] = raw_data.values[:, self.loading_params[key]]
        return data


