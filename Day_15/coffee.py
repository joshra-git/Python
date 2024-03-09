MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

total_money = ""

# print (MENU["latte"])

def coins():
    quarters = int(input (("how many quarters? "))) * 0.25
    dimes = int(input("how many dimes? ")) * 0.10
    nickles = int(input("how many nickles? ")) * 0.05
    pennies = int(input("how many pennies? ")) * 0.01

    total_money = quarters + dimes + nickles + pennies
    print (f"You have given the machine $ {total_money}")
    return total_money


def costing(monies):

    for i in MENU:
        price = float((MENU[i]["cost"]))
        if i == str(coffee):
            if price < monies:
                print ("You have enough money")
                print (f"Here is your {i}")
                print (f"Here is your $ {monies - price}")
            
            else:
                print ("You don't have enough moneys")


power = False
while power == False:

    coffee = input ("What would you like? (espresso/latte/cappuccino)")

    # print (MENU.get("{coffee}"))

    if coffee == "off":
        power = True
    elif coffee == "report":
        for key, value in resources.items():
            print(f"{key}: {value}")
    else:
        print ("Please insert coins.")

        money_from_coins = coins()

        costing(money_from_coins)

        
# I want to take my coffee choice, get the ingredients, print them