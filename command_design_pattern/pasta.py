from order import Order
from chef import Chef

class Pasta(Order):
    
    def __init__(self, chef : Chef):
        self.__chef = chef
        
    def make_order(self):
        print("Making Pasta")
        self.__chef.cook_pasta()