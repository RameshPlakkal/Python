# TODO:  Create a menu list/dict with details on all the items needed to make a coffee
# TODO: prompt the options to the user
# TODO: post user selection check if there are enough resources to make coffee else display sorry message
# TODO: if enough resources, give a prompt to insert coins
# TODO: validate the total amount the user has entered, if less "refund" and display insufficient amount message
# TODO: if amount is OK deliver the coffee and print the message. if excess amount given refund the change
# TODO: update the resource in the coffee machine including the money collected

# List of available menu items
coffee_menu = {
    "espresso": {
        "water": 50,
        "coffee": 18,
        "milk": 0,
        "price": 1.50
    },
    "latte": {
        "water": 200,
        "coffee": 24,
        "milk": 150,
        "price": 2.50
    },
    "cappuccino": {
        "water": 250,
        "coffee": 24,
        "milk": 100,
        "price": 3.00
    }
}

# Tracking currency with conversion rates
currency = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}

# Tracking current variables
CURRENT_RESOURCE_WATER = 300
CURRENT_RESOURCE_MILK = 200
CURRENT_RESOURCE_COFFEE = 100
COFFEE_INCOME = 0

MACHINE_ON = True


def validate_current_resource_state(user_choice):
    """This method validates the resource state based on user selection.
        Returns true if all OK else returns item that is not enough"""
    global CURRENT_RESOURCE_WATER, CURRENT_RESOURCE_MILK, CURRENT_RESOURCE_COFFEE

    resource_water = coffee_menu[user_choice]["water"]
    resource_milk = coffee_menu[user_choice]["milk"]
    resource_coffee = coffee_menu[user_choice]["coffee"]

    if CURRENT_RESOURCE_WATER > resource_water:
        if CURRENT_RESOURCE_MILK > resource_milk:
            if CURRENT_RESOURCE_COFFEE > resource_coffee:
                return True
            else:
                print("Sorry! Not enough coffee for your drink.")
                return False
        else:
            print("Sorry! Not enough milk for your drink.")
            return False
    else:
        print("Sorry! Not enough water for your drink.")
        return False


def process_inserted_coins(quarter, dime, nickle, pennie):
    """Function takes in the number of coins inserted by the user and calculates the total amount and
    returns the same"""

    user_amount = quarter * currency["quarters"] + dime * currency["dimes"] + nickle * currency["nickles"] + pennie * \
                  currency["pennies"]
    return user_amount


def check_transaction_and_deliver(user_amount, user_choice):
    """Validates the transaction status based on the user amount against the coffee choice
    Checks for excess and refunds
    returns true/false """

    coffee_price = coffee_menu[user_choice]["price"]
    if user_amount > coffee_price:
        print(f"Here's your change  ${round(user_amount - coffee_price, 2)}")
        print(f"... And your {user_choice} ☕. Enjoy!")
        track_inventory(user_choice)
        # return True
    else:
        print("Sorry! That's not enough money. Please collect the refund.")
        # return False


def track_inventory(user_choice):
    """Tracks real time inventory status based on usage"""
    global CURRENT_RESOURCE_WATER, CURRENT_RESOURCE_MILK, CURRENT_RESOURCE_COFFEE, COFFEE_INCOME

    CURRENT_RESOURCE_WATER -= coffee_menu[user_choice]["water"]
    CURRENT_RESOURCE_MILK -= coffee_menu[user_choice]["milk"]
    CURRENT_RESOURCE_COFFEE -= coffee_menu[user_choice]["coffee"]
    COFFEE_INCOME += coffee_menu[user_choice]["price"]


def print_report():
    print("Inventory Balance : ")
    print(f"WATER : {CURRENT_RESOURCE_WATER}")
    print(f"MILK : {CURRENT_RESOURCE_MILK}")
    print(f"COFFEE : {CURRENT_RESOURCE_COFFEE}")
    print(f"EARNING $: {COFFEE_INCOME}")

    start_coffee_machine()


def turn_off_machine():
    """Turns off the machine"""
    global MACHINE_ON
    MACHINE_ON = False


def start_coffee_machine():
    """Starts the Coffee Machine"""
    global MACHINE_ON

    while MACHINE_ON:
        user_choice = input("What would you like? (espresso/latte/cappuccino) : ").lower()

        if user_choice == "report":
            print_report()
        elif user_choice == "off":
            print("GoodBye!")
            exit()

        # print("in while")
        resource_state = validate_current_resource_state(user_choice)
        if resource_state:
            print("Please insert coins.")
            quarters = int(input("- How many quarters? : "))
            dimes = int(input("- How many dimes? : "))
            nickles = int(input("- How many nickles? : "))
            pennies = int(input("- How many pennies? : "))
            user_amount = process_inserted_coins(quarters, dimes, nickles, pennies)
            check_transaction_and_deliver(user_amount, user_choice)


start_coffee_machine()

