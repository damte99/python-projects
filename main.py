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


def check_order(choice, inventory):
    """Gives feedback of the state of the order"""
    if check_resources(MENU[choice]['ingredients'], inventory) and process_coins(MENU[choice]):
        inventory = make_coffee(MENU[choice]['ingredients'], inventory)
        print(f"Enjoy your {choice}!")
        inventory = check_money(inventory)
        inventory['money'] += MENU[choice]['cost']
    return inventory


def report():
    for asset in resources:
        if "money" != asset:
            print(f"{asset.title()}: {resources[asset]}", end=" ")
            if "coffee" != asset:
                print("ml")
            else:
                print("gr")
        else:
            print(f"{asset.title()}: ${resources[asset]}")


def check_resources(coffee, inventory):
    """Checks if there's enough ingredients to make the coffee. Returns a boolean."""
    all_ingredients = True
    for ingredient in coffee:
        if coffee[ingredient] > inventory[ingredient]:
            print(f"There's not enough {ingredient}.")
            print(f"Current: {inventory[ingredient]} ml/gr, Needed: {coffee[ingredient]} ml/gr")
            all_ingredients = False
    return all_ingredients


def process_coins(coffee):
    """Shows the price to the user and asks how many coins for each currency is going to insert. Returns true or false
    weather the payment was done successfully or not."""
    payment = 0
    print(f"That's ${coffee['cost']}")
    print(f"Please insert coins.")
    coins = {'quarters': 0.25, 'dimes': 0.1, 'nickels': 0.05, 'pennies': 0.01}
    for coin in coins:
        print(f"How many {coin}?")
        payment += float(input()) * coins[coin]
    if payment >= coffee['cost']:
        change = payment - coffee['cost']
        print(f"Your change is: {round(change, 2)}")
        return True
    else:
        print("Sorry, that's not enough.")
        return False


def make_coffee(coffee, inventory):
    """Discounts the ingredients from the inventory and returns an updated dictionary."""
    for ingredient in coffee:
        inventory[ingredient] -= coffee[ingredient]
    return inventory


def check_money(inventory):
    """Adds the entry 'money' to the dictionary if there's none. Returns an updated version with it."""
    assets = 0
    for element in inventory:
        assets += 1
    if assets == 3:
        inventory['money'] = 0
    return inventory


def replenish(inventory):
    for ingredient in inventory:
        if ingredient != 'money':
            if ingredient != 'coffee':
                inventory[ingredient] += int(input(f"How many ml of {ingredient} will you load?"))
            else:
                inventory[ingredient] += int(input(f"How many grams of {ingredient} will you load?"))
    return inventory


machine_on = True
while machine_on:
    selection = input("What would you like? (espresso/latte/cappuccino):").lower()
    if selection == 'reload':
        resources = replenish(resources)
    elif selection != 'off':
        resources = check_order(selection, resources)
    else:
        machine_on = False
