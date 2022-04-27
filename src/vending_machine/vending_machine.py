from typing import Sequence

from src.vending_machine.storage import DrinkStorage
from src.vending_machine.storage import MoneyStorage
from src.drink.drink import Drink
from src.money.money import Money


class PriceDict:
    def __init__(self, drinks: Sequence[Drink], prices: Sequence[int]):
        if not all([isinstance(i, Drink) for i in drinks]):
            raise RuntimeError('KeyはDrinkである必要があります')
        if not all([isinstance(i, int) for i in prices]):
            raise RuntimeError('価格は整数である必要があります')

        self._dict = {key: val for key, val in zip(drinks, prices)}

    def __getitem__(self, item):
        return self._dict[item]

    def __contains__(self, item):
        return item in self._dict.keys()


class VendingMachine:
    def __init__(self, drinks: DrinkStorage, moneys: MoneyStorage, prices: PriceDict):
        self.drink_storage = drinks
        self.money_storage = moneys
        self.price_dict = prices
        self.coin_mech = MoneyStorage([Money.FIVE_HUNDRED, Money.HUNDRED, Money.FIFTY, Money.TEN], [0, 0, 0, 0])

    def put_money(self, money: Money):
        if not self.coin_mech.can_handle(money):
            # 対応していないお金の場合返却する
            return money
        else:
            self.coin_mech.put(money)

    def buy(self, drink: Drink):
        total_amount = self.coin_mech.total_amount()
        drink_price = self.price_dict[drink]
        if total_amount >= drink_price:
            # todo:支払いができるかどうかの詳細な判定
            change = total_amount - drink_price
            return drink
        else:
            return None

    def _pay(self, price: int):
        if price > self.coin_mech.total_amount():
            raise RuntimeError


def get_sample_vending_machine() -> VendingMachine:
    drink_storage = DrinkStorage([Drink.COKE, Drink.DIET_COKE, Drink.GREEN_TEA], [10, 10, 10])
    money_storage = MoneyStorage([Money.FIVE_HUNDRED, Money.HUNDRED, Money.FIFTY, Money.TEN], [0, 0, 0, 0])
    price_dict = PriceDict([Drink.COKE, Drink.DIET_COKE, Drink.GREEN_TEA], [120, 120, 100])

    machine = VendingMachine(drink_storage, money_storage, price_dict)
    return machine
