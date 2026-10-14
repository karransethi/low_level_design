from phone import Phone
from desktop import Desktop
from weather_station import WeatherStation

weather = WeatherStation()
phone = Phone()
desktop = Desktop()

weather.add_devices(phone)
weather.add_devices(desktop)
weather.update_temp(10)
weather.update_temp(20)
