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
        money_machine.report()

    else:
        cup = menu.find_drink(drink)
        if coffee_maker.is_resource_sufficient(cup) and money_machine.make_payment(cup.cost):
            
                coffee_maker.make_coffee(cup)
                    
    

