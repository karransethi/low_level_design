from diwali import Diwali
from new_user_discount import NewUserDis
from discount_finder import DiscountFinder


diwali = Diwali()
new_user = NewUserDis()


dis = DiscountFinder(new_user)

dis.get_discount()