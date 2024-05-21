from data import MENU, resources

OFF = "off"
REPORT = "report"
money = 0


def get_input():
    """
    Returns either "espresso", "latte", "cappucino", "off", or "report"
    """
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ")

        if choice in MENU or choice == OFF or choice == REPORT:
            return choice


def print_report():
    """
    Prints available resources an money
    """
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def resources_are_enough(ingredients):
    """
    Returns True if resources are enough, or False if otherwise
    """
    for i in ingredients:
        if resources[i] < ingredients[i]:
            print(f"Sorry there is not enough {i}.")
            return False

    return True


def get_coins():
    """
    Returns the total value of inserted coins
    """
    print("Please insert coins.")

    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.1
    nickles = int(input("How many nickles? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01

    return quarters + dimes + nickles + pennies


def inserted_enough_money(money, cost):
    """
    Calculate change and returns True if money is greater than cost, or False if otherwise
    """
    change = money - cost

    if change > 0:
        print(f"Here is ${'{:.2f}'.format(change)} dollars in change.")
    elif change < 0:
        print("Sorry that's not enough money. Money refunded.")

    return change >= 0


def make_coffee(name, ingredients):
    """
    Deduct resources based on given ingredients
    """
    for i in ingredients:
        resources[i] -= ingredients[i]

    print(f"Here is your {name}. Enjoy!")


while True:
    user_input = get_input()

    if user_input == OFF:
        break
    elif user_input == REPORT:
        print_report()
    else:
        coffee = MENU[user_input]
        ingredients = coffee["ingredients"]

        if resources_are_enough(ingredients=ingredients):
            coins = get_coins()
            cost = coffee["cost"]

            if inserted_enough_money(money=coins, cost=cost):
                money += cost
                make_coffee(name=user_input, ingredients=ingredients)
