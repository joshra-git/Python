from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# 1. Print Report
# 2. Check resources sufficient?
# 3. Process Coins
# 4. Check transaction successsful?
# 5. Make Coffee
ordering = Menu()
zloty = MoneyMachine()
drinky_poo = CoffeeMaker()

# Gets the order of which I want
c_order = input("What would you like? latte, esspresso or cappuccino?: ")

# Feeds that order in to ensure it is actually an option to be able to select
drinky_poo = ordering.find_drink(c_order)

# Gets the items that are required in order to make it
cost = ordering.get_items()



asdf = ordering.menu

print (asdf)

# zloty.process_coins(dollary)

# zloty.make_payment(dollary)

