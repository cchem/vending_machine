from src.vending_machine.storage import DrinkStorage
from src.vending_machine.storage import MoneyStorage
from src.drink.drink import Drink
from src.money.money import Money


class VendingMachine:
    def __init__(self, drink_storage: DrinkStorage, money_storage: MoneyStorage):
        self.drink_storage = drink_storage
        self.money_storage = money_storage
        self.coin_mech = MoneyStorage([Money.FIVE_HUNDRED, Money.HUNDRED, Money.FIFTY, Money.TEN], [0, 0, 0, 0])


def get_sample_vending_machine() -> VendingMachine:
    drink_storage = DrinkStorage([Drink.COKE, Drink.DIET_COKE, Drink.GREEN_TEA], [10, 10, 10])
    money_storage = MoneyStorage([Money.FIVE_HUNDRED, Money.HUNDRED, Money.FIFTY, Money.TEN], [0, 0, 0, 0])

    machine = VendingMachine(drink_storage, money_storage)
    return machine
