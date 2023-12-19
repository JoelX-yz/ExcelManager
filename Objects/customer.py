from .cart import *
from Modules.StringMethod import *

class Customer:
    def __init__(self, name: str):
        self.name: str = name
        self.alias: list[str] = []
        self.memo: str = ""
        self.cart: Cart = Cart()
    
    def add_to_cart(self, product: Product, quantity: int):
        self.cart.add(product, quantity)
