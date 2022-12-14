from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_machine_on = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while is_machine_on:
    options = menu.get_items()
    choice = str(input(f"    What would you like? ({options}): ")).lower()

    if choice == "off":
        print("Turning machine off...")
        is_machine_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
