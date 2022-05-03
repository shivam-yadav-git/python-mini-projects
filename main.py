ingredients_available = {
    "coffee": 50,
    "milk": 50,
    "water": 50
}

coffee_price = {
    "espresso": 10,
    "latte": 20,
    "cappuccino": 30
}


def report(change):
    print(f'Report:\n Water: {ingredients_available["water"]}ml\n Coffee: '
          f'{ingredients_available["coffee"]}g\n Milk: {ingredients_available["milk"]}ml ')
    if change != 'first':
        print(f"Change: {change} Rs\n Enjoy your coffee")


def check_ingredients(coffee):
    print("Status")


def make_espresso():
    print("espresso consumes 5g coffee, 10ml water and 10 ml milk")
    if ingredients_available["coffee"] >= 5 and ingredients_available["milk"] >= 10 and ingredients_available[
        "water"] >= 10:
        ingredients_available["coffee"] -= 5
        ingredients_available["milk"] -= 10
        ingredients_available["water"] -= 10
        return 1
    else:
        print("Sorry!! We do not have enough ingredients to make your coffee")
        return 0


def make_latte():
    print("Latte consumes 10g coffee, 10ml water and 20 ml milk")
    if ingredients_available["coffee"] >= 10 and ingredients_available["milk"] >= 20 and ingredients_available[
        "water"] >= 10:
        ingredients_available["coffee"] -= 10
        ingredients_available["milk"] -= 20
        ingredients_available["water"] -= 10
        return 1
    else:
        print("Sorry!! We do not have enough ingredients to make your coffee")
        return 0


def make_cappuccino():
    print("cappuccino consumes 10g coffee, 10ml water and 20 ml milk")
    if ingredients_available["coffee"] >= 20 and ingredients_available["milk"] >= 30 and ingredients_available[
        "water"] >= 10:
        ingredients_available["coffee"] -= 20
        ingredients_available["milk"] -= 30
        ingredients_available["water"] -= 10
        return 1
    else:
        print("Sorry!! We do not have enough ingredients to make your coffee")
        return 0


def check_amount(amount, coffee_rate):
    if amount >= coffee_rate:
        return amount - coffee_rate
    else:
        print(f"Not enough money please provide {coffee_rate - amount} more\n")
        amt = float(input("Money: "))
        amount += amt
        check_amount(amount, coffee_rate)


def get_coffee():
    report('first')
    coffee_type = input("What would you like to have:\n A. Espresso : 10Rs \n B. Latte : 20Rs\n C. Cappuccino : 30Rs\n")
    if coffee_type == 'A':
        amount = float(input(f"Please provide {coffee_price['espresso']} rs\n"))
        status = make_espresso()
        if status == 1:
            change_money = check_amount(amount, coffee_price['espresso'])
        else:
            change_money = amount

    elif coffee_type == 'B':
        amount = float(input(f"Please provide {coffee_price['latte']} rs\n"))
        status = make_latte()
        change_money = check_amount(amount, coffee_price['latte'])
        if status == 1:
            change_money = check_amount(amount, coffee_price['latte'])
        else:
            change_money = amount
    elif coffee_type == 'C':
        amount = float(input(f"Please provide {coffee_price['cappuccino']} rs\n"))
        status = make_cappuccino()
        change_money = check_amount(amount, coffee_price['cappuccino'])
        if status == 1:
            change_money = check_amount(amount, coffee_price['cappuccino'])
        else:
            change_money = amount

    else:
        print("Please choose a correct coffee")
        get_coffee()
    report(change_money)


while input("Would you like to have coffee\n 'YES' \n 'NO'\n").lower() == 'yes':
    get_coffee()
