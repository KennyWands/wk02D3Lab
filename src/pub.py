class Pub:
    def __init__(self, get_name, get_till):
        self.name = get_name
        self.till = get_till

    def increase_till(self, drink):
        self.till += drink.price

    def check_enough_cash(self, customer, item):
        if customer.wallet >= item.price:
            return True
        return False

    def check_age(self, customer):
        if customer.age >= 18:
            return True
        return False

    def check_customer_drunk(self, customer):
        if customer.drunk < 100:
            return False

        return True

    def sell_drink(self, drink, customer):
        if (
            self.check_enough_cash(customer, drink) == True
            and self.check_age(customer) == True
            and self.check_customer_drunk(customer) == False
        ):
            self.increase_till(drink)
            customer.decrease_wallet(drink)
            print(f"Would you like ice {customer.name}?")
        elif self.check_enough_cash(customer, drink) != True:
            print(f"Damn it {customer.name} this isn't a charity!")
            return False
        elif self.check_age(customer) != True:
            print(f"Sorry {customer.name}, maybe you would like a Coke?")
            return False
        elif self.check_customer_drunk(customer):
            print(f"{customer.name}! Dude, you need to sober up!!")
            return False

    def sell_food(self, customer, food):
        if self.check_enough_cash(customer, food) == True:
            self.increase_till(food)
            customer.decrease_wallet(food)


# stock value ie.value of all drinks
