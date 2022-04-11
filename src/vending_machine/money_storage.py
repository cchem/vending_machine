from typing import Sequence

from src.money.money import Money


class MoneyStorage:
    def __init__(self, money_list: Sequence[Money], number: int):
        self.storage = {key: val for key, val in money_list, number}

    def add_money(self, money: Money, num: int):
        self.storage[money] += num
