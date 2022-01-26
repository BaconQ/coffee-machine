from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
switch = True

display = menu.display()
while switch:

    print(display)
    drink = input("What would you like?: ")
    drink.lower()

    if drink == "off":
        swtich = False
        break

    elif drink == "report":
        coffee_maker.report()

    elif menu.find_drink(drink) != None:

        if coffee_maker.is_resource_sufficient(menu.menu[menu.drink_order(drink)]) == True:
            if money_machine.make_payment(menu.drink_order(drink)):
                    coffee_maker.make_coffee(menu.menu[menu.drink_order(drink)])
                    
    

