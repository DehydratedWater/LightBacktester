from typing import Dict, Union, List
from abc import abstractmethod


class CommandConnector:
    """
    This class is connector between strategy and simulator or broker's api
    It's meant to be inherited and specified for use with any api or simulator
    Not all functions must be covered
    but they should throw error "Functionality not supported: [name of action]" in such case
    """

    @abstractmethod
    def update_with_new_data(self, data: Dict[str, List[any]], new_data: Dict[str, List[any]]):
        pass

    @abstractmethod
    def buy(self, params: Dict[str, any]) -> int:
        pass

    @abstractmethod
    def sell(self, params: Dict[str, any]) -> int:
        pass

    @abstractmethod
    def buy_stop(self, params: Dict[str, any]) -> int:
        pass

    @abstractmethod
    def sell_stop(self, params: Dict[str, any]) -> int:
        pass

    @abstractmethod
    def buy_limit(self, params: Dict[str, any]) -> int:
        pass

    @abstractmethod
    def sell_limit(self, params: Dict[str, any]) -> int:
        pass

    @abstractmethod
    def close_order(self, params: Dict[str, any]) -> int:
        pass

    @abstractmethod
    def cancel_order(self, params: Dict[str, any]) -> int:
        pass
