from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update_weather(self, temp):
        pass