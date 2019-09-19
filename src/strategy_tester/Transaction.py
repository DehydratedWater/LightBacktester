from abc import abstractmethod
from typing import Dict


class Transaction:

    @abstractmethod
    def can_be_opened(self) -> bool:
        pass

    @abstractmethod
    def should_be_closed(self, candle: Dict[str, any] = None, price: Dict[str, any] = None) -> int:
        pass

    @abstractmethod
    def is_closed(self) -> bool:
        pass
