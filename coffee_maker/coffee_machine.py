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
profit = 0
def cost_balance(drink):    
    cost = MENU[drink]["cost"]
    print(f" Cost of {drink} is Rs.{cost}")
    print(" Please insert coins.")
    total = int(input("How many Rs.10 coins do you have? ")) * 10
    total += int(input("How many Rs.5 coins do you have? ")) * 5
    total += int(input("How many Rs.2 coin do you have? ")) * 2
    total += int(input("How many Rs.1 coin do you have? ")) * 1
    balance = total - cost
    if balance < 0:
        print("Sorry that's not enough money. Money refunded")
        return False
    elif balance >= 0:
        print( f"Here is Rs.{balance} in change ")
        global profit
        profit += cost
        return True


def resource_left(drink_ingredients):
    for item,quantity in drink_ingredients.items():
        if quantity > resources[item]:
            print(f"Insufficent {item}")
            return False
        else:
            return True
            
is_on = True
while is_on:
    choice = input("What would you like? Espresso/ Latte/ Cappuccino: ").lower()
    if choice == "report":
        print(f'Water left: {resources["water"]} \nMilk left: {resources["milk"]} \nCoffee left: {resources["coffee"]}')
        print(f"Profit: {profit}")
    elif choice == "off":
        is_on = False
    else:
        blnc = cost_balance(choice)
        if blnc == True:
            drink = MENU[choice]
            if resource_left(drink["ingredients"]) == True:
                print(f"Here is your {choice}. Enjoy")
                for item,quantity in drink["ingredients"].items():
                    resources[item] -= quantity
    
