from typing import List, Dict, Union
from src.loaders.tests.StreamDataConnector import StreamDataConnector
from src.simulators.Strategy import Strategy


class DataFeed:
    """
    This class main purpose is to feed data to subscribed strategies
    Data can be transferred from multiple type of sources
    As static data, that is CsvLoader type data
    Or ad dynamic data, that may be life streamed data from brokers api
    No matter the source, DataFeed will pass unified this data and pass it
    """
    def __init__(self, data_source):
        """
        :param data_source: static or dynamic source of data,
            static source of data is dictionary with data arrays
            dynamic source of data is object of StreamDataConnector
        """
        self.previous_data = {}

        self.data: Union[Dict[str, List[any]], None] = None
        self._feeding_started: bool = False
        if type(data_source) is StreamDataConnector:
            data_source.set_data_feed(self)
        else:
            self.data = data_source
        self.strategies_to_feed: List[Strategy] = []

    def connect_simulator_to_data_feed(self, strategy: Strategy):
        """
        By passing strategy to this method, strategy becomes subscriber of this data feed
        :param strategy:
        :return:
        """
        self.strategies_to_feed.append(strategy)

    def update_simulators(self, type_of_data: str, new_data: Dict[str, any]):
        """
        DO NOT USE
        this method is for StreamDataConnector internal use
        it's purpose is to receive data from StreamDataConnector
        and feed it to strategies as transformed format
        """
        pass

    def run(self):
        """
        This method starts passing data to all subscribed strategies
        Depended on data source it will start _stream_historic_data_by_candle(self)
        for static data or set flag that allows dynamic data to pass
        :return:
        """
        if self.data is not None:
            self._stream_historic_data_by_candle()
        else:
            self._feeding_started = True

    def stop(self):
        self._feeding_started = False

    def _stream_historic_data_by_candle(self):
        """
        This method cuts static data candle by candle and feeds it to all subscribed strategies
        :return:
        """
        self.previous_data = {}
        for i in range(len(self.data[self.data.keys()[0]])):
            new_data = {}
            for key in self.data.keys():
                if key not in self.previous_data:
                    self.previous_data[key] = []
                self.previous_data[key].append(self.data[key][i])
                new_data[key] = self.data[key][i]

            for strategy in range(len(self.strategies_to_feed)):
                self.strategies_to_feed[strategy].update(self.previous_data, new_data)

