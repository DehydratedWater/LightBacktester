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
        self.closed_with_price = []
        self.vol_opened = vol
        self.vol_closed = []
        self.sum_vol_closed = 0
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
            if price["ask"] <= self.open_price <= price["ask"] + self.slippage:
                return True
            return False

    def open(self, candle: Dict[str, any] = None, price: Dict[str, any] = None):
        if candle is not None:
            self.opened_with_price = self.open_price
        if price is not None:
            self.opened_with_price = price["ask"]

    def update_auto_close(self, candle: Dict[str, any] = None, price: Dict[str, any] = None) -> float:
        pass

    def can_be_closed(self, close_price: float, candle: Dict[str, any] = None, price: Dict[str, any] = None) -> bool:
        if candle is not None:
            if candle["low"] <= close_price <= candle["high"]:
                return True
            return False
        if price is not None:
            if price["bid"] - self.slippage <= self.open_price <= price["bid"]:
                return True
            return False

    def close(self, close_price: float, close_vol: float, candle: Dict[str, any] = None, price: Dict[str, any] = None):
        if candle is not None:
            self.closed_with_price.append(close_price)
            self.vol_closed.append(close_vol)
            self.sum_vol_closed += close_vol
        if price is not None:
            self.closed_with_price.append(price["bid"])
            self.vol_closed.append(close_vol)
            self.sum_vol_closed += close_vol

    def is_closed(self) -> bool:
        return self.vol_opened == self.sum_vol_closed

