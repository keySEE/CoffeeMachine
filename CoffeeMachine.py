class CoffeeMachine:
    # available ingredients
    ingredients = ["ml of water", "ml of milk", "grams of coffee beans", "disposable cups of coffee", "money"]
    ingredients_available = [400, 540, 120, 9, 550]
    # coffee_ingredients
    espresso = [250, 0, 16, 1, -4]
    latte = [350, 75, 20, 1, -7]
    cappuccino = [200, 100, 12, 1, -6]

    def menu(self):
        while 1:
            action_selected = input("Write action (buy, fill, take, remaining, exit):")
            if action_selected == "exit":
                break

            if action_selected == "remaining":
                CoffeeMachine.coffee_machine_state(self)
                return CoffeeMachine.menu(self)

            if action_selected == "take":
                print("I gave you ${}".format(CoffeeMachine.ingredients_available[4]))
                CoffeeMachine.ingredients_available[4] = 0
                return CoffeeMachine.menu(self)

            if action_selected == "fill":
                n = 0
                while n < len(CoffeeMachine.ingredients_available) - 1:
                    CoffeeMachine.ingredients_available[n] += int(input("Write how many " + CoffeeMachine.ingredients[n] + " do you want to add:"))
                    n += 1
                return CoffeeMachine.menu(self)

            if action_selected == "buy":
                coffee_selected = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
                if coffee_selected == "back":
                    continue
                elif coffee_selected == "1":
                    if CoffeeMachine.check_ingredients_availability(self, CoffeeMachine.espresso):
                        CoffeeMachine.make_coffee(self, CoffeeMachine.espresso)
                elif coffee_selected == "2":
                    if CoffeeMachine.check_ingredients_availability(self, CoffeeMachine.latte):
                        CoffeeMachine.make_coffee(self, CoffeeMachine.latte)
                elif coffee_selected == "3":
                    if CoffeeMachine.check_ingredients_availability(self, CoffeeMachine.cappuccino):
                        CoffeeMachine.make_coffee(self, CoffeeMachine.cappuccino)
                return CoffeeMachine.menu(self)

    # function section
    def coffee_machine_state(self):
        n = 0
        print("The coffee machine has:")
        while n < len(CoffeeMachine.ingredients_available):
           print(CoffeeMachine.ingredients_available[n], "of", CoffeeMachine.ingredients[n])
           n += 1

    def check_ingredients_availability(self, coffee_type):
        n = 0
        while n < len(coffee_type):
            if CoffeeMachine.ingredients_available[n] < coffee_type[n]:
                print("Sorry, not enough ", CoffeeMachine.ingredients[n], "!")
                return False
            n += 1
        return True

    def make_coffee(self, coffee_type):
        n = 0
        print("I have enough resources, making you a coffee!")
        while n < len(coffee_type):
            CoffeeMachine.ingredients_available[n] -= coffee_type[n]
            n += 1


coffee_machine = CoffeeMachine()
coffee_machine.menu()
