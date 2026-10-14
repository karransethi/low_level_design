from abc import ABC, abstractmethod 

class Strategy(ABC):
    @abstractmethod
    def show_discount(self):
        pass