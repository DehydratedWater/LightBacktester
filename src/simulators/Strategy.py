from abc import abstractmethod
from typing import Dict, List, Union

from src.command_connectors.CommandConnector import CommandConnector


class Strategy:
    """
    Class that is base for any strategy
    This class should be inherited to create new strategy
    on_init method should be threted as constructor
    on_tick_data method is updated with every new data bit
    """

    def __init__(self, command_connector: CommandConnector):
        self.command = command_connector

    @abstractmethod
    def on_tick_data(self, data: Dict[str, List[any]], new_data: Dict[str, List[any]]) -> Union[str, None]:
        """
        This method should contain strategy logic
        :param data: dictionary with lists of previous market data
        :param new_data: dictionary with new data that triggered run of this method
        :return: return None if everything was ok or string with error message
        """
        pass

    def update(self, data: Dict[str, List[any]], new_data: Dict[str, List[any]]) -> Union[str, None]:
        """
        DO NOT USE
        This method is for internal use of DataFeed
        It runs on_tick_data and updates command_connector with new data
        :param data:
        :param new_data:
        :return:
        """
        self.command.update_with_new_data(data, new_data)
        return self.on_tick_data(data, new_data)

