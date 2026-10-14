from typing import List
from observer import Observer

class WeatherStation():
    def __init__(self):
        self.__temp = 0
        self.__devices : List[Observer] = []
        
    def update_temp(self, temp):
        self.__temp = temp
        self.update_devices()
    
    def update_devices(self):
        for device in self.__devices :
            device.update_weather(self.__temp)
            
    def add_devices(self, device : Observer):
        self.__devices.append(device)
        
    def remove_device(self, device : Observer):
        self.__devices.remove(device)