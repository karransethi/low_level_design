from pizza import Pizza
from pasta import Pasta
from waiter import Waiter
from chef import Chef

chef = Chef()
pizza = Pizza(chef)
pasta = Pasta(chef)


waiter = Waiter(pasta)
waiter.execute()