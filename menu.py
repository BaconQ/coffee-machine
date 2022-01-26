from prettytable import PrettyTable
table = PrettyTable()

class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")

    def drink_order(self, order_name):
        for i in range(len(self.menu)):
            if self.menu[i].name == order_name:
                return i

    def drink_cost(self, order_name):
            for i in range(len(self.menu)):
                if self.menu[i].name == order_name:
                    return self.menu[i].cost
    
    def display(self):
        
        print(r"""
    (  )   (   )  )
     ) (   )  (  (
     ( )  (    ) )
     _____________
    <_____________> ___
    |             |/ _ \
    |               | | |
    |               |_| |
 ___|             |\___/
/    \___________/    \
\_____________________/
                """)
        table.field_names = ["Coffee", "Price",]

        for i in range(len(self.menu)):
            table.add_row(
                [self.menu[i].name, f"${self.menu[i].cost}"]
            )
        table.align = "l"
        return table
