import unittest

from src.customer import Customer
from src.pub import Pub
from src.drink import Drink
from src.food import Food


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Sandy", 10, 19, 20)
        self.pub = Pub("The Prancing Pony", 100)
        self.drink = Drink("Whisky", 2, 20)
        self.food = Food("Steak", 5, 20)

    def test_customer_has_name(self):
        self.assertEqual("Sandy", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(10, self.customer.wallet)

    def test_buy_drink(self):
        self.customer.buy_drink(self.pub, self.drink, self.customer)
        self.assertEqual(40, self.customer.drunk)
        self.assertEqual(8, self.customer.wallet)

    def test_buy_food(self):
        self.customer.buy_food(self.food)
        self.assertEqual(5, self.customer.wallet)
        self.assertEqual(0, self.customer.drunk)
