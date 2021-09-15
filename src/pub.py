# from src.drink import Drink
from src.customer import Customer

class Pub:

    def __init__(self, input_name, input_till):
        self.name = input_name
        self.till = input_till
        self.drinks = []


    def add_drink_to_list(self, drink):
        self.drinks.append(drink)


    def sell_drink_to_customer(self, drink):
        self.drinks.remove(drink)

    def increase_till(self, drink):
        self.till += drink.drink_price