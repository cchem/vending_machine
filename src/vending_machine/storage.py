from typing import Sequence

from src.drink.drink import Drink
from src.money.money import Money


class Storage:
    def __init__(self, kinds: Sequence, numbers: Sequence[int]):
        self._storage = {key: val for key, val in kinds, numbers}

    def can_handle(self, kind):
        return kind in self._storage.keys()

    def exists(self, kind):
        return self._storage[kind] > 0

    def put(self, kind, number=1):
        if not self.can_handle(kind):
            return kind

        self._storage[kind] += number

    def get(self, drink: Drink):
        if self.exists(drink):
            self._storage -= 1
            return drink
        else:
            return None

    def get_all(self):
        return [key for key in self._storage.keys() for _ in self._storage[key]]


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

    def total_amount(self):
        return sum(self.get_all())

    def can_pay(self, price: int):
        raise NotImplemented

    def get(self, price: int):
        raise NotImplemented
