from typing import Dict, List

from src.command_connectors.CommandConnector import CommandConnector


class ConsoleTextConnector(CommandConnector):

    def buy(self, params: Dict[str, any]) -> int:
        print("Buy ", params)
        return -1

    def sell(self, params: Dict[str, any]) -> int:
        print("Sell ", params)
        return -1

    def buy_stop(self, params: Dict[str, any]) -> int:
        print("Buy stop ", params)
        return -1

    def sell_stop(self, params: Dict[str, any]) -> int:
        print("Sell stop ", params)
        return -1

    def buy_limit(self, params: Dict[str, any]) -> int:
        print("Buy limit ", params)
        return -1

    def sell_limit(self, params: Dict[str, any]) -> int:
        print("Sell limit ", params)
        return -1

    def close_order(self, params: Dict[str, any]) -> int:
        print("Close order ", params)
        return -1

    def cancel_order(self, params: Dict[str, any]) -> int:
        print("Cancel order ", params)
        return -1

    def update_with_new_data(self, data: Dict[str, List[any]], new_data: Dict[str, List[any]]):
        print("DATA: ", new_data)



