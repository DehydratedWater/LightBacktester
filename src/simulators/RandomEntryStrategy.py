import random
from typing import Dict, List, Union

from src.command_connectors.CommandConnector import CommandConnector
from src.simulators.Strategy import Strategy


class RandomEntryStrategy(Strategy):

    def __init__(self, command_connector: CommandConnector):
        super().__init__(command_connector)
        self.last_direction: str = "BUY"
        self.threshold = 0.1

    def on_tick_data(self, data: Dict[str, List[any]], new_data: Dict[str, List[any]]) -> Union[str, None]:
        make_transaction = random.random() < self.threshold
        if make_transaction:
            if self.last_direction == "BUY":
                self.command.sell({"price": new_data["close"], "type": "SELL"})
                self.last_direction = "SELL"
            else:
                self.command.buy({"price": new_data["close"], "type": "BUY"})
                self.last_direction = "BUY"
        return None
