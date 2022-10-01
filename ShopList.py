from Product import *

"""
Object works as a shopping cart
Holds products of an order
"""
class  ShopList:

    def __init__(self):
        self.container = {}
        self.total = 0
    
    def add(self, product, quantity):
        if product in self.container:
            self.container[product] += quantity
        else:
            self.container[product] = quantity
        
        if product.price is not None:
            self.total += product.price * quantity
            self.total = round(self.total,1)

        product.count += quantity   #   Count total number of products


    def show(self):
        for k, v in self.container.items():
            print(k.name,v)
    

