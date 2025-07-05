MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0
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



#☕
water_main=300
milk_main=200
coffee_main=100
money_main=0

paise = 0.1
ruppee=1

def report():
    print(f"water: {water_main}ml")
    print(f"Milk: {milk_main}ml")
    print(f"coffee: {coffee_main}g")
    print(f"money: ${money_main}")

def check_resources(ask):
    if MENU[ask]['ingredients']['water'] > water_main:
        print("Sorry there is not enough water.")
        return False
    if MENU[ask]['ingredients']['milk'] > milk_main:
        print("Sorry there is not enough milk.")
        return False
    if MENU[ask]['ingredients']['coffee'] > coffee_main:
        print("Sorry there is not enough coffee.")
        return False
    return True

def process_coins(ask):
    a = int(input("How many paise:"))
    b = int(input("How many Ruppee:"))
    global money_main, water_main, milk_main, coffee_main
    gain = a * paise + b * ruppee

    price = MENU[ask]['cost']

    if gain < price:
        print("Sorry that's not enough money. Money refunded.​")
    else:
        money_main += gain
        change = gain - price
        print(f"Here is ${change:.2f} in change")
        print(f"Here is your {ask} ☕Enjoy!")
        money_main -= change
        water_main -= MENU[ask]['ingredients']['water']
        milk_main -= MENU[ask]['ingredients']['milk']
        coffee_main -= MENU[ask]['ingredients']['coffee']

while True:
    ask = input("What would you like? (espresso/latte/cappuccino):").lower()

    if ask == "report":
        report()
    elif ask == "off":
        break
    elif ask in ["espresso", "cappuccino", "latte"]:
        if check_resources(ask):
            process_coins(ask)
        else:
            break


