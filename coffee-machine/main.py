import menu

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()



is_on =  True
while is_on:
    options = menu.get_items()
    choices = input(f"what do you want to order? ({options})")
    if choices == "off":
        is_on=False
    elif choices == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choices)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

