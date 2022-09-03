MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
flag = True
money = 0


def report_print():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")
    print("\n")


def resource_checker(ing):
    if resources['water'] < ing['water']:
        print("Sorry there is not enough water.")
        return False
    elif resources['milk'] < ing['milk']:
        print("Sorry there is not enough milk.")
        return False
    elif resources['coffee'] < ing['coffee']:
        print("Sorry there is not enough coffee.")
        return False
    return True


def process_coins():
    q = int(input("How many quarters?: "))
    d = int(input("How many dimes?: "))
    n = int(input("How many nickels?: "))
    p = int(input("How many pennies?: "))
    total = round((q*0.25) + (d*0.10) + (n*0.05) + (p*0.01), 2)
    return total


def transaction_checker(ing2, insert_money2):
    global money
    if ing2 > insert_money2:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif ing2 < insert_money2:
        change = round(insert_money2 - ing2, 2)
        money += ing2
        print(f"Here is ${change} in change.")
        return True
    else:
        money += insert_money2
        return True


def update_resources(ing3, res):
    res['water'] -= ing3['water']
    res['milk'] -= ing3['milk']
    res['coffee'] -= ing3['coffee']


def prompt_checker(prompt2):
    if prompt2 == "espresso":
        if resource_checker(MENU["espresso"]["ingredients"]):
            print(f"Please insert ${MENU['espresso']['cost']} in coins.")
            insert_money = process_coins()
            if transaction_checker(MENU['espresso']['cost'], insert_money):
                print("Here is your espresso. Enjoy!")
                update_resources(MENU["espresso"]["ingredients"], resources)
                print("\n")
        return True
    elif prompt2 == "latte":
        if resource_checker(MENU["latte"]["ingredients"]):
            print(f"Please insert ${MENU['latte']['cost']} in coins.")
            insert_money = process_coins()
            if transaction_checker(MENU['latte']['cost'], insert_money):
                print("Here is your latte. Enjoy!")
                update_resources(MENU["latte"]["ingredients"], resources)
                print("\n")
        return True
    elif prompt2 == "cappuccino":
        if resource_checker(MENU["cappuccino"]["ingredients"]):
            print(f"Please insert ${MENU['cappuccino']['cost']} in coins.")
            insert_money = process_coins()
            if transaction_checker(MENU['cappuccino']['cost'], insert_money):
                print("Here is your cappuccino. Enjoy!")
                update_resources(MENU["cappuccino"]["ingredients"], resources)
                print("\n")
        return True
    elif prompt2 == "report":
        report_print()
        print("\n")
        return True
    elif prompt2 == "off":
        return False
    else:
        print("WRONG input try again")
        print("\n")
        return True


while flag:
    prompt = input("What would like?(espresso/latte/cappuccino): ").lower()
    flag = prompt_checker(prompt)
