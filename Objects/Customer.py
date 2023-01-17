from ShopList import *
from StringMethod import *

class Customer:
    def __init__(self, name: str):
        self.name: str = name
        self.alias: list[str] = []
        self.memo: str = ""
        self.shopList: ShopList = ShopList()
    
    def buy(self, product: Product, quantity: int):
        self.shopList.add(product, quantity)

    @classmethod
    def getAllCustomerNames():
        return Customer.allCustomerNames
