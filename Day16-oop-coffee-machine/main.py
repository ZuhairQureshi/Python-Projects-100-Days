from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

coffee_machine = CoffeeMaker()
the_menu = Menu()
money_withdrawer = MoneyMachine()

while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_machine.report()
        money_withdrawer.report()
    else:
      drink = the_menu.find_drink(choice)
      if coffee_machine.is_resource_sufficient(drink):
            if money_withdrawer.make_payment(drink.cost):
              coffee_machine.make_coffee(drink)  
