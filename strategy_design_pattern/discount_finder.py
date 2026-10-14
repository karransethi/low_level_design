from strategy import Strategy


class DiscountFinder():
    def __init__(self, discount : Strategy):
        self.__discount = discount
        
    def get_discount(self):
        self.__discount.show_discount()