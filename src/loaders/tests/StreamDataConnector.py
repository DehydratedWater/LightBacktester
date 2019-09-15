from src.loaders.DataFeed import DataFeed


class StreamDataConnector:
    def __init__(self):
        self.data_feed_to_update: DataFeed = None

    def set_data_feed(self, data_feed):
        """This function allows to connect data feed to life data source"""
        self.data_feed_to_update = data_feed
