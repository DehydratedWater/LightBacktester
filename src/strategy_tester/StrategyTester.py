from typing import Dict, List


class StrategyTester:
    def __init__(self):
        self.transaction_list = []
        self.previous_prices: List[Dict[str, any]] = []
        self.previous_candles: List[Dict[str, any]] = []

    def update_with_price(self, candle: Dict[str, any] = None, price: Dict[str, any] = None):
        if candle is not None:
            self.previous_candles.append(candle)
            self._check_new_candle(candle)
        if price is not None:
            self.previous_prices.append(price)
            self._check_new_price(price)

    def _check_new_candle(self, candle: Dict[str, any]):
        pass

    def _check_new_price(self, price: Dict[str, any]):
        pass
