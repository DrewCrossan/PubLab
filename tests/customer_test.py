import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Karen", 1000, 21)

    def test_customer_has_name(self):
        self.assertEqual("Karen", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(1000, self.customer.wallet)

    def test_wallet_reduced(self):
        drink = Drink("Bud", 2, 1)
        self.customer.wallet_reduced(drink)
        self.assertEqual(998, self.customer.wallet)


    def test_increase_customer_drunkness(self):
        drink = Drink("Bud", 2, 1)
        drink2 = Drink("JD & Coke", 5, 3)
        self.customer.increase_customer_drunkness(drink)
        self.customer.increase_customer_drunkness(drink2)
        self.assertEqual(4, self.customer.drunkeness)

    def test_customer_too_drunk(self):
        drink = Drink("Bud", 2, 1)
        drink2 = Drink("JD & Coke", 5, 3)
        drink3 = Drink("JD & Coke", 5, 3)
        self.customer.increase_customer_drunkness(drink)
        self.customer.increase_customer_drunkness(drink2)
        self.customer.increase_customer_drunkness(drink3)
        self.assertEqual(True, self.customer.customer_too_drunk())
