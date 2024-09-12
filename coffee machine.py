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
money_in_machine = 0

valid_choices = ["espresso", "latte", "cappuccino", "report"]

while True:

    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    while user_choice not in valid_choices:
        print("Please choose a valid option")
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()


        #REPORT
        #how much water the coffee machine has - it starts off with 300ml
        #how much milk the coffee machine has - it starts off with 200ml
        #how much coffee the coffee machine has - it starts off with 100g coffee
        #how much money the coffee machine has - it is in dollars
        #print the report

    def report():
        global MENU

        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money_in_machine}")


    def check_resources(user_choice):
        global MENU

        for i in MENU[user_choice]["ingredients"]:
            if MENU[user_choice]["ingredients"][i] > resources[i]:
                print(f"Sorry there is not enough {i}.")
                return False
            else:
                resources[i] -= MENU[user_choice]["ingredients"][i]
        return True




    if user_choice == "report" or user_choice == "Report":
        report()
        continue



    if check_resources(user_choice) is False:
        continue

    else:
        print("Please insert coins.")

        quarters = input("How many quarters?: ")
        while quarters.isdigit() is False:
            print("Please enter a valid number.")
            quarters = input("How many quarters?: ")

        dimes = input("How many dimes?: ")
        while dimes.isdigit() is False:
            print("Please enter a valid number.")
            dimes = input("How many dimes?: ")

        nickels = input("How many nickels?: ")
        while nickels.isdigit() is False:
            print("Please enter a valid number.")
            nickels = input("How many nickels?: ")

        pennies = input("How many pennies?: ")
        while pennies.isdigit() is False:
            print("Please enter a valid number.")
            pennies = input("How many pennies?: ")

        quarters = int(quarters)
        dimes = int(dimes)
        nickels = int(nickels)
        pennies = int(pennies)
        user_total_coins = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01    


    def check_money(user_choice):
        global money_in_machine 

        if MENU[user_choice]["cost"] > user_total_coins:
            if user_choice == "espresso" or user_choice == "Espresso":
                resources["water"] += MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] += MENU["espresso"]["ingredients"]["coffee"]
                return False

            elif user_choice == "latte" or user_choice == "Latte" or user_choice == "cappuccino" or user_choice == "Cappuccino":
                resources["water"] += MENU[user_choice]["ingredients"]["water"]
                resources["coffee"] += MENU[user_choice]["ingredients"]["coffee"]
                resources["milk"] += MENU[user_choice]["ingredients"]["milk"]
                return False


        elif MENU[user_choice]["cost"] <= user_total_coins:
            change = round(user_total_coins - MENU[user_choice]["cost"], 2)
            print(f"Here is ${change} in change.")
            money_in_machine += MENU[user_choice]["cost"]
            return True


    if check_money(user_choice) is False:
        print("Sorry that's not enough money. Money refunded.")
        continue
    else:
        print(f"Here is your {user_choice}. Enjoy!")
