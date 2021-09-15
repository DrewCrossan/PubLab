import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Karen", 1000, 21)

    def test_customer_has_name(self):
        self.assertEqual("Karen", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(1000, self.customer.wallet)

    def test_wallet_reduced(self):
        drink = Drink("Bud", 2)
        self.customer.wallet_reduced(drink)
        self.assertEqual(998, self.customer.wallet)


        