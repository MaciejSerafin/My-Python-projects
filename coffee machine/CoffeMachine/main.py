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

# TODO: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino): "
# TODO 2: 2. Turn off the Coffee Machine by entering “off” to the prompt

money = 0

def report_money(choice):
    global money
    if choice == "espresso":
        money += 1.5
        print(f"Money: 1.5")
    elif choice == "latte":
        money += 2.0
        print(f"Money: 2.0")
    elif choice == "cappuccino":
        money += 2.5
        print(f"Money: 2.5")
    elif choice == "report":
        print(f"Money: ${money}")

def report_espresso(MENU, resources):
  resources["water"] = resources["water"] - MENU[choice]['ingredients']['water']
  resources["coffee"] = resources["coffee"] - MENU[choice]['ingredients']['coffee']
def report_f(MENU, resources):
  resources["water"] = resources["water"] - MENU[choice]['ingredients']['water']
  resources["milk"] = resources["milk"] - MENU[choice]['ingredients']['milk']
  resources["coffee"] = resources["coffee"] - MENU[choice]['ingredients']['coffee']






should_continue = True
while should_continue:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "espresso":
        print("Here is your espresso")
        report_espresso(MENU, resources)
        report_money(choice)
    elif choice == "latte":
        print("Here is your latte")
        report_f(MENU, resources)
        report_money(choice)
    elif choice == "cappuccino":
        print("Here is your cappuccino")
        report_f(MENU, resources)
        report_money(choice)
    elif choice == "off":
        print("Machine turn off")
        should_continue = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffe: {resources['coffee']}g")
        report_money(choice)
    else:
        print("Invalid")
        should_continue = False

# TODO 3: 3. Print report