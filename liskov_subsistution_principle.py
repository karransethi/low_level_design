from abc import ABC, abstractmethod 

class Accont(ABC):
    def __init__(self, bal):
        self.bal = bal
    
    @abstractmethod 
    def deposit(self, amount):
        pass
    
    
class WithdrawAcc(Accont):
    
    def __init__(self, bal):
        super().__init__(bal)
    @abstractmethod
    def withdraw(self, amount):
        pass
    
class Savings(WithdrawAcc):
    def __init__(self, bal):
        super().__init__(bal)
        
    def deposit(self, amount):
        self.bal += amount
        print(f'New balance in savings acc is {self.bal}')
        
    def withdraw(self, amount):
        self.bal -= amount
        print(f'New balance in savings acc is {self.bal}')
        
class FD(Accont):
    def __init__(self, bal):
        super().__init__(bal)
        
    def deposit(self, amount):
        self.bal += amount
        print(f'New balance in fixed deposit is {self.bal}')
        
savings = Savings(1000)
savings.deposit(2000)
savings.withdraw(450)

fd = FD(2000)
fd.deposit(200)