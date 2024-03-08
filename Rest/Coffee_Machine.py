import sys
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


# TODO 4. CHECK TRANSACTION SUCCESSFUL
# TODO 5. MAKE COFFEe

#user make a choice what would he like
def user_input(choice):
    # program shut down with hidden commend off
    if choice == "off":
        print("...System closing...")
        return sys.exit()
    # report resources
    elif choice == "report":
        for key, value in resources.items():
           print(f"{key.capitalize()}: {value}")
        print(f"Money: ${money}")
    else:
        return choice

#check resources sufficient
def resources_sufficient(choice):
    if choice in MENU:
        ingredients_needed = MENU[choice]["ingredients"]
        for ingredient, amount_needed in ingredients_needed.items():
            if resources[ingredient] < amount_needed:
                return f"Sorry, not enough {ingredient}..."

    elif choice not in ["espresso" ,"latte" ,"cappucino",]:
        return "Sorrry, not available..."
    return None


#calculate the monetary values
def insert_coins():
    # printing message if resprces are NOT SUFFICIENT
    if resources_sufficient(choice) is not None:
        print(resources_sufficient(choice))
        print("Please insert resources \n...System closing...")
        return sys.exit()
    # calculate the monetary values
    else:
        print("Please insert coins: ")
        Quarters = input("1) Quarters (0,25$): ")
        Dimes = input("2) Dimes (0,10$): ")
        Nickles = input("3) Nickles (0,05$): ")
        Pennies = input("4) Pennies (0.01$): ")
        money = int(Quarters)/4 + int(Dimes)/10 + int(Nickles)/20 + int(Pennies)/100
        return money

def transaction_succesful(money):
    if money < MENU[choice]["cost"]:
        return "Sorry, that's not enough money"
    else:
        change = money - MENU[choice]["cost"]
        return f"Transaction successful! Your change is ${change:.2f}"

def resources_update(choice):
    if choice in MENU:
        ingredients_needed = MENU[choice]["ingredients"]
        for ingredient,amount_needed in ingredients_needed.items():
            resources[ingredient] -= amount_needed
        return resources


coffee_machine = True
while coffee_machine:
    money = 0
    choice = input("What would you like? (espresso, latte, cappuccino): \n").lower()
    if user_input(choice) is choice:
        money = insert_coins()
        print(transaction_succesful(money))
        resources_update(choice)
