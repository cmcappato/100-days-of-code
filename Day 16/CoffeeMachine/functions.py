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
    "money": 0,
}


def manage_resources(coffee_type):
    coffee_ingredient = MENU[coffee_type]["ingredients"]

    for resource in coffee_ingredient:
        if coffee_ingredient[resource] > resources[resource]:
            print(f"Sorry, there is not enough {resource}")
            return False
        else:
            resources[resource] -= coffee_ingredient[resource]

    return True


# Takes the amount and coffee type in order to make it
def make_coffee(amount, coffee_type):
    coffee_price = MENU[coffee_type]["cost"]

    if coffee_price > amount:
        print("Sorry, that's not enough money. Money refunded")
    else:
        remainder = round(amount - coffee_price, 2)
        resources["money"] += coffee_price
        print(f'Here is ${remainder} in change')
        print(f"Here is your {coffee_type} ☕. Enjoy!")


# Asks for the coins to the user and returns the total amount
def process_coins():
    print("Please insert coins")

    total = int(input("Hoy many quarters?: ")) * 0.25
    total += int(input("Hoy many dimes?: ")) * 0.10
    total += int(input("Hoy many nickles?: ")) * 0.05
    total += int(input("Hoy many pennies?: ")) * 0.01

    return total


# Prints the resources that the coffee machine has left
def print_report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${resources["money"]}')


