from abc import ABC, abstractmethod

class Order(ABC):
    @abstractmethod
    def make_order(self):
        pass