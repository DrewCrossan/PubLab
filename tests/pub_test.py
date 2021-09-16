import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer


class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.drinks = Drink("Miller", 2, 1)
        self.customer = Customer("Karen", 1000, 21)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_pub_has_drink(self):
        beer = Drink("Bud", 1, 1)
        self.pub.drinks.append(beer)
        self.assertEqual(1, len(self.pub.drinks))

    

    def test_add_drink_to_list(self):
        drink = Drink("Tenents", 3, 1)
        drink2 = Drink("Peroni", 4, 1)
        self.pub.add_drink_to_list(drink)
        self.pub.add_drink_to_list(drink2)
        self.assertEqual(2, len(self.pub.drinks))

    def test_sell_drink_to_customer(self):
        drink = Drink("Peroni", 4, 1)
        drink2 = Drink("cola", 10, 1)
        self.pub.add_drink_to_list(drink)
        self.pub.add_drink_to_list(drink2)
        self.pub.sell_drink_to_customer(drink)
        self.assertEqual(1, len(self.pub.drinks))

    def test_increase_pub_till_decrease_customer_wallet(self):
        drink = Drink("Peroni", 4, 1)
        drink2 = Drink("Bud", 3, 1)
        self.pub.add_drink_to_list(drink)
        self.pub.add_drink_to_list(drink2)
        self.pub.sell_drink_to_customer(drink)
        self.customer.wallet_reduced(drink)
        self.pub.increase_till(drink)
        self.assertEqual(104, self.pub.till)
        self.assertEqual(996, self.customer.wallet)
        self.assertEqual(1, len(self.pub.drinks))

    def test_check_age(self):
        person = Customer("Marion", 25, 21)
        self.assertEqual(True, self.pub.check_age(person))

    
        
