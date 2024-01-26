import art

print(art.logo)



MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    "money": 0
}

def compare_resources(coffee, resources):
    if (resources["milk"] > MENU[coffee]["ingredients"]["milk"]) and (resources["water"] > MENU[coffee]["ingredients"]["water"]) and (resources["coffee"] > MENU[coffee]["ingredients"]["coffee"]):        
        return True
    else:
        return False


def make_payment():
    print("Please insert coins. ")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    inserted_money = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    inserted_money = round(inserted_money, 2)
    return inserted_money


def give_changes(inserted_money, coffee):
    return inserted_money - MENU[coffee]["cost"]


def client_got(coffee):
    global atm_money
    atm_money += MENU[coffee]["cost"]
    resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
    resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
    resources["water"] -= MENU[coffee]["ingredients"]["water"]
    resources["money"] += MENU[coffee]["cost"]


def report():
    print(f"    Milk: {resources['milk']} ml")
    print(f"    Water: {resources['water']} ml")
    print(f"    Coffee: {resources['coffee']} g")
    print(f"    Money: {resources['money']} $")


def add():
    resources["coffee"] += int(input("How many g coffee do you want add? :"))
    resources["milk"] += int(input("How many ml milk do you want add? :"))
    resources["water"] += int(input("How many ml water do you want add? :"))


menu = ["espresso", "latte", "cappuccino"]
is_resources_enough = False
is_turn_on = True
money_enough = False
client_get_coffee = False
quarters, dimes, nickles, pennies = 0,0,0,0
inserted_money = 0.0


while True:
    coffee = input("Which coffee would you like? (espresso/latte/cappuccino): ")
    if coffee == "--report":
        report()
    elif coffee == "--add":
        add()
    if coffee in menu:
        
        inserted_money = make_payment()
        print(f"You inserted {inserted_money}")
        print(f'\n{coffee} costs {MENU[coffee]["cost"]}$.')

        if inserted_money >= MENU[coffee]["cost"]:
            
            is_resources_enough = compare_resources(coffee, resources)
            if is_resources_enough == True:
                client_got(coffee)
                print(f"Your changes {give_changes(inserted_money, coffee)}")
                print(f"Here is your {coffee}. Enjoy.")
            
            else:
                print("Sorry, machine doesn't has enough resources. ")


