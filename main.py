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
    for ingredient in MENU[user_choice]["ingredients"]:
        if MENU[user_choice]["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}")
            is_enough_ingredients = False

    return is_enough_ingredients


def process_coins(cost):
    """function to process coins. Return float"""
    print("Please insert coins.")
    total_amount = 0
    quarters = int(input("Quarters: $")) * 0.25
    total_amount = quarters
    if total_amount < cost:
        dimes = int(input("Dimes: $")) * 0.1
        total_amount += dimes
        if total_amount < cost:
            nickles = int(input("Nickels: $")) * 0.05
            total_amount += nickles
            if total_amount < cost:
                pennies = int(input("Pennies: $")) * 0.01
                total_amount += pennies
    return total_amount


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
        user_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if user_choice == "off":
            is_off = True
            print(f"Total money collected: ${total_money}")
            print("Worst coffee machine stopped!")
        elif user_choice == "report":
            print(report(total_money))
        else:
            if check_resources(user_choice):
                given_amount = process_coins(MENU[user_choice]["cost"])
                if check_transaction(given_amount, MENU[user_choice]["cost"]):
                    for ingredient in MENU[user_choice]["ingredients"]:
                        resources[ingredient] -= MENU[user_choice]["ingredients"][ingredient]
                    print(f"Here is your {user_choice}. Enjoy!\n")
                    total_money += MENU[user_choice]["cost"]


print("Welcome to the worst coffee machine!\n")
make_coffee()
