from typing import List, Callable, Dict

from src.strategy_tester.Transaction import Transaction


class Buy(Transaction):

    def __init__(self,
                 open_price: float,
                 vol: float,
                 slippage: float,
                 stop_loss: List[float, float] = None,
                 take_profit: List[float, float] = None,
                 trailing_stop_loss: List[Callable[[Dict[str, any], Dict[str, any]], (float, float)]] = None):
        self.open_price = open_price
        self.opened_with_price = 0
        self.close_price = -1
        self.transaction_opened = False
        self.vol_opened = vol
        self.vol_closed = 0
        self.slippage = slippage
        self.stop_loss = stop_loss
        self.take_profit = take_profit
        self.trailing_stop_loss = trailing_stop_loss

    def can_be_opened(self, candle: Dict[str, any] = None, price: Dict[str, any] = None) -> bool:
        if candle is not None:
            if candle["low"] <= self.open_price <= candle["high"]:
                return True
            return False
        if price is not None:
            if price["bid"] - self.slippage <= self.open_price <= price["bid"]:
                return True
            return False

    def open(self, candle: Dict[str, any] = None, price: Dict[str, any] = None):
        if candle is not None:
            self.opened_with_price = self.open_price
            self.transaction_opened = True
        if price is not None:
            self.opened_with_price = price["bid"]
            self.transaction_opened = True

    def update_auto_close(self, candle: Dict[str, any] = None, price: Dict[str, any] = None) -> int:
        pass

    def close(self, candle: Dict[str, any] = None, price: Dict[str, any] = None):
        pass

    def is_closed(self) -> bool:
        pass
