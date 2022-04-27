from typing import Sequence

from src.drink.drink import Drink
from src.money.money import Money


class Storage:
    def __init__(self, kinds: Sequence, numbers: Sequence[int]):
        self.storage = {key: val for key, val in kinds, numbers}

    def exists(self, kind):
        return self.storage[kind] > 0

    def get(self, drink: Drink):
        if self.exists(drink):
            self.storage -= 1
            return drink
        else:
            return None


class DrinkStorage(Storage):
    def __init__(self, kinds: Sequence[Drink], numbers: Sequence[int]):
        if not all([isinstance(i, Drink) for i in kinds]):
            raise RuntimeError('Key must be object of Drink')
        super().__init__(kinds, numbers)


class MoneyStorage(Storage):
    def __init__(self, kinds: Sequence[Money], numbers: Sequence[int]):
        if not all([isinstance(i, Money) for i in kinds]):
            raise RuntimeError('Key must be object of Drink')
        super().__init__(kinds, numbers)
