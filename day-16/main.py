from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
machine = CoffeeMaker()
money = MoneyMachine()

machine_on = True
while machine_on:
    selection = input(f"What would you like? {menu.get_items().title()}")

    if selection == "off":
        machine_on = False
    elif selection == "report":
        machine.report()
        money.report()
    else:
        coffee = menu.find_drink(selection)
        if machine.is_resource_sufficient(coffee) and money.make_payment(coffee.cost):
            machine.make_coffee(coffee)



