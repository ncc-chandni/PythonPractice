MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 10,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 15,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

balance = 0
def cost_balance(drink):    
    cost = MENU[drink]["cost"]
    print(type(cost))
    print(f" Cost of {drink} is Rs.{cost}")
    print("Please insert coins.")
    tens = int(input("How many Rs.10 coins do you have? "))
    fives = int(input("How many Rs.5 coins do you have? "))
    twos = int(input("How many Rs.2 coin do you have? "))
    ones = int(input("How many Rs.1 coin do you have? "))
    total = tens*10 + fives*5 + twos * 2 + ones * 1
    balance = total - cost
    if balance < 0:
        return "Sorry that's not enough money. Money refunded"
    elif balance > 0:
        return f"Here is Rs.{balance} in change "
    else:
        return f"No change required"

def resources_left():
    water = MENU[drink]["ingredients"]["water"]
    milk = MENU[drink]["ingredients"]["milk"]
    coffee = MENU[drink]["ingredients"]["coffee"]
    water_left = resources["water"] - water
    milk_left = resources["milk"] - milk
    coffee_left = resources["coffee"] - coffee
    return water_left, milk_left, coffee_left

drink = input("  What would you like? Espresso/ Latte/ Cappuccino: ").lower()
blnc = cost_balance(drink)
print(blnc)
print(type(resources_left()))


