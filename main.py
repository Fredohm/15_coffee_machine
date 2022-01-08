from menu import MENU, resources


def report(money_count):
    """function to print report"""
    return f"Water: {resources['water']}ml\n" \
           f"Milk: {resources['milk']}ml\n" \
           f"Coffee: {resources['coffee']}g\n" \
           f"Money: ${money_count}\n"


def check_type(user_choice):
    return user_choice != "espresso"


def check_resources(user_choice):
    """function to check resources, print message if not enough and return boolean"""
    # check ingredients against user_choice
    is_enough_ingredients = True
    has_milk = check_type(user_choice)

    if MENU[user_choice]["ingredients"]["water"] <= resources["water"]:
        if MENU[user_choice]["ingredients"]["coffee"] <= resources["coffee"]:
            if has_milk:
                if MENU[user_choice]["ingredients"]["milk"] <= resources["milk"]:
                    resources["milk"] -= MENU[user_choice]["ingredients"]["milk"]
                else:
                    print("Sorry, there is not enough milk.")
                    is_enough_ingredients = False
            resources["water"] -= MENU[user_choice]["ingredients"]["water"]
            resources["coffee"] -= MENU[user_choice]["ingredients"]["coffee"]
        else:
            print("Sorry, there is not enough coffee.")
            is_enough_ingredients = False
    else:
        print("Sorry, there is not enough water.")
        is_enough_ingredients = False

    return is_enough_ingredients


def process_coins():
    """function to process coins. Return float"""
    quarters = int(input("Quarters: $"))
    dimes = int(input("Dimes: $"))
    nickles = int(input("Nickels: $"))
    pennies = int(input("Pennies: $"))
    return 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies


def check_transaction(given_amount, coffee_price):
    """function to check if the user give enough coins and print change amount if price too high. return boolean"""
    if given_amount == coffee_price:
        return True
    elif given_amount > coffee_price:
        print(f"Here is ${round((given_amount - coffee_price), 2)} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee():
    """function to run coffee machine."""
    is_off = False
    total_money = 0
    while not is_off:
        user_choice = input("What would you like? (espresso/latte/cappuccino):\n")
        if user_choice == "espresso":
            if check_resources(user_choice):
                given_amount = process_coins()
                if check_transaction(given_amount, MENU[user_choice]["cost"]):
                    print(f"Here is your {user_choice}. Enjoy!")
                    total_money += MENU[user_choice]["cost"]
        elif user_choice == "latte":
            if check_resources(user_choice):
                given_amount = process_coins()
                if check_transaction(given_amount, MENU[user_choice]["cost"]):
                    print(f"Here is your {user_choice}. Enjoy!")
                    total_money += MENU[user_choice]["cost"]
        elif user_choice == "cappuccino":
            if check_resources(user_choice):
                given_amount = process_coins()
                if check_transaction(given_amount, MENU[user_choice]["cost"]):
                    print(f"Here is your {user_choice}. Enjoy!")
                    total_money += MENU[user_choice]["cost"]
        elif user_choice == "report":
            print(report(total_money))
        else:
            if user_choice == "off":
                is_off = True
                print("Worst coffee machine stopped!")
            else:
                return total_money


print("Welcome to the worst coffee machine!\n")
make_coffee()
