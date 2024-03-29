from abc import abstractmethod, ABC
from typing import Dict


class Transaction(ABC):

    @abstractmethod
    def can_be_opened(self, candle: Dict[str, any] = None, price: Dict[str, any] = None) -> bool:
        pass

    @abstractmethod
    def open(self, candle: Dict[str, any] = None, price: Dict[str, any] = None):
        pass

    @abstractmethod
    def update_auto_close(self, candle: Dict[str, any] = None, price: Dict[str, any] = None) -> float:
        pass

    @abstractmethod
    def can_be_closed(self, close_price: float, candle: Dict[str, any] = None, price: Dict[str, any] = None) -> bool:
        pass

    @abstractmethod
    def close(self, close_price: float, close_vol: float, candle: Dict[str, any] = None, price: Dict[str, any] = None):
        pass

    @abstractmethod
    def is_closed(self) -> bool:
        pass
