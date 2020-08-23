# coffeemachine 6/6

class CoffeeMachine:

    def __init__(self, water, milk, coffee, cups, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money
        self.user = ''


    def choices(self):
        if self.user != "exit":
            self.user = input("Write action (buy, fill, take, remaining, exit):\n>")

            if self.user == "buy":
                CoffeeMachine.buy(self)
            if self.user == "remaining":
                CoffeeMachine.remaining(self)
            if self.user == "fill":
                CoffeeMachine.fill(self)
            if self.user == "take":
                CoffeeMachine.take(self)
        else:
            exit()

    def remaining(self):
        print("The coffee machine has:\n"
              f"{self.water} of water\n"
              f"{self.milk} of milk\n"
              f"{self.coffee} of coffee beans\n"
              f"{self.cups} of disposable cups\n"
              f"{self.money} of money")
        self.choices()

    def buy(self):
        buys = (input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n>"))

        if buys == "1":
            if self.water - 250 >= 0 and self.coffee - 16 >= 0 and self.cups - 1 >= 0:
                self.water -= 250
                self.coffee -= 16
                self.money += 4
                self.cups -= 1
                print("I have enough resources, making you a coffee!")
                self.choices()
            else:
                print("Sorry, not enough water!")
                self.choices()

        elif buys == "2":
            if self.water - 350 >= 0 and self.coffee - 20 >= 0 and self.milk - 75 >= 0 and self.cups - 1 >= 0:
                self.water -= 350
                self.coffee -= 20
                self.milk -= 75
                self.money += 7
                self.cups -= 1
                print("I have enough resources, making you a coffee!")
                self.choices()
            else:
                print("Sorry, not enough water!")
                self.choices()

        elif buys == "3":
            if self.water - 200 >= 0 and self.coffee - 12 >= 0 and self.milk - 100 >= 0 and self.cups - 1 >= 0:
                self.water -= 200
                self.milk -= 100
                self.coffee -= 12
                self.cups -= 1
                self.money += 6
                print("I have enough resources, making you a coffee!")
                self.choices()
            else:
                print("Sorry, not enough water!")
                self.choices()

        elif buys == "back":
            self.choices()

    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add: "))
        self.milk += int(input("Write how many ml of milk do you want to add: "))
        self.coffee += int(input("Write how many grams of coffee beans do you want to add: "))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add: "))
        self.choices()

    def take(self):
        print("I gave you", self.money,"\n")
        self.money -= self.money
        self.choices()

cof = CoffeeMachine(400, 540, 120, 9, 550)
cof.choices()

