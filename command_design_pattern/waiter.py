from order import Order


class Waiter:
    def __init__(self, order : Order):
        self.__order = order
        
    def execute(self):
        self.__order.make_order()
        