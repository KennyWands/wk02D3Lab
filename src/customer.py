class Customer:
    def __init__(self, get_name, get_wallet, get_age, set_drunk):
        self.name = get_name
        self.wallet = get_wallet
        self.age = get_age
        self.drunk = set_drunk

    def decrease_wallet(self, price):
        self.wallet -= price.price

    def increase_drunk(self, alcohol):
        drunkenness += alcohol

    def buy_drink(self, pub, drink, customer):
        pub.sell_drink(drink, customer)
        self.drunk += drink.alcohol

    def buy_food(self, snack):
        self.wallet -= snack.price
        self.drunk -= snack.rejuv
