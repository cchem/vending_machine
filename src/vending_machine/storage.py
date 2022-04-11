from typing import Sequence

from src.drink.drink import Drink


class Storage:
    def __init__(self, drink_lineup: Sequence[Drink], number: int):
        self.storage = {key: val for key, val in drink_lineup, number}

    def has_stock(self, drink: Drink):
        return self.storage[drink] > 0
