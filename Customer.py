from ShopList import *
from StringMethod import *

class Customer:
    def __init__(self, name):
        self.name = name
        self.memo = ""
        self.shopList = ShopList()