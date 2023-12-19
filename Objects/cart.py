from .Product import *

"""
Object works as a shopping cart
Holds products of an order
"""
class  ShopList:
    def __init__(self):
        self.shoppingCart: dict[Product,int] = {}
        self.total: float = 0
    
    #   Add a product to shopping cart and add price to total
    def add(self, product: Product, quantity: int):
        if product in self.shoppingCart:
            self.shoppingCart[product] += quantity
        else:
            self.shoppingCart[product] = quantity

        if product.price is not None:
            self.total += product.price * quantity
            self.total = round(self.total,2)

        #   ---------------Statistical operations----------
        #   Count total number of products
        product.totalCount += quantity

    #   Print current object's shopping cart
    def showShoppingCart(self):
        for k, v in self.shoppingCart.items():
            print(k.name,v)




    

