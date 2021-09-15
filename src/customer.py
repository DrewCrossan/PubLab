# from src.pub import Pub
class Customer:

    def __init__(self, input_name, input_wallet, input_age):
        self.name = input_name
        self.wallet = input_wallet
        self.age = input_age
        self.drunkeness = 0

    def wallet_reduced(self, beverage):
        self.wallet -= beverage.drink_price

    def increase_customer_drunkness(self, drink):
        self.drunkeness += drink.alcohol_level

    def customer_too_drunk(self):
        if self.drunkeness > 5:
            return True
        return False


        

        

    