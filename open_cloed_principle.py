from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    
class UPI(Payment):
    def pay(self, amount : int):
        print(f'Amount paid via UPI : {amount}')
        
        
class CC(Payment):
    def pay(self, amount : int):
        print(f'Amount paid via credit card : {amount}')
        
class DC(Payment):
    def pay(self, amount : int):
        print(f'Amount paid via debit card : {amount}')
        
        
class PaymentProcessor:
    def process(self, amount : int, payment : Payment):
        payment.pay(amount)
        
        
upi = UPI()

cc= CC()

dc= DC()

payment = PaymentProcessor()

payment.process(5000, cc)