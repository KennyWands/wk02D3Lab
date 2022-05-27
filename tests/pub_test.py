import unittest

from src.customer import Customer
from src.pub import Pub
from src.drink import Drink
from src.food import Food

# from folder.file import Class

# 3 A's of testing: Arrange, Act, Assert
# Arrange: set up test enviroment
# Act: perform action we are testing
# Assert: perform test


class TestPub(unittest.TestCase):
    # this class inherits from unittest.TestCase
    def setUp(self):
        # runs before each test creating data used for the tests
        self.customer0 = Customer("Sandy", 10, 19, 0)  # pass all test
        self.customer1 = Customer("Kenny", 0, 19, 0)  # fail wallet
        self.customer2 = Customer("Bilbo", 10, 5, 0)  # fail age
        self.customer3 = Customer("Frodo", 10, 19, 100)  # fail drunk
        self.pub = Pub("The Prancing Pony", 100)
        self.drink = Drink("Whisky", 2, 20)
        self.food = Food("Steak", 5, 20)

    def test_pub_has_name(self):
        # test_ identifies this as a test to be run, to the IDE
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        # (expected, actual)
        self.assertEqual(100, self.pub.till)

    def test_increase_till(
        self,
    ):
        self.pub.increase_till(self.drink)
        self.assertEqual(102, self.pub.till)

    def test_check_enough_cash(self):
        self.assertEqual(True, self.pub.check_enough_cash(self.customer0, self.drink))
        self.assertEqual(False, self.pub.check_enough_cash(self.customer1, self.drink))

    def test_Check_customer_age(self):
        self.assertEqual(True, self.pub.check_age(self.customer0))
        self.assertEqual(False, self.pub.check_age(self.customer2))

    def test_customer_drunk(self):
        self.pub.check_customer_drunk(self.customer0)
        self.assertEqual(False, self.pub.check_customer_drunk(self.customer0))
        self.assertEqual(True, self.pub.check_customer_drunk(self.customer3))

    def test_drink_sold(self):
        self.pub.increase_till(self.drink)
        self.assertEqual(102, self.pub.till)

    def test_sell_drink(self):
        self.pub.sell_drink(self.drink, self.customer0)
        self.assertEqual(102, self.pub.till)
        self.assertEqual(8, self.customer0.wallet)

    def test_sell_drink__no_money(self):
        self.pub.sell_drink(self.drink, self.customer1)
        self.assertEqual(100, self.pub.till)
        self.assertEqual(0, self.customer1.wallet)

    def test_sell_drink__underaged(self):
        self.pub.sell_drink(self.drink, self.customer2)
        self.assertEqual(100, self.pub.till)
        self.assertEqual(10, self.customer2.wallet)

    def test_sell_drink__drunk(self):
        self.pub.sell_drink(self.drink, self.customer3)
        self.assertEqual(100, self.pub.till)
        self.assertEqual(10, self.customer3.wallet)

    def test_sell_food(self):
        self.pub.sell_food(self.customer0, self.food)  ############
        self.assertEqual(105, self.pub.till)
        self.assertEqual(5, self.customer0.wallet)
