from .product import *

"""
Object works as a shopping cart
Holds products of an order
"""
class  Cart:
    def __init__(self):
        self.order_items: dict[Product,int] = {}
        self.total: float = 0
    
    #   Add a product to shopping cart and add price to total
    def add(self, product: Product, quantity: int):
        if product in self.order_items:
            self.order_items[product] += quantity
        else:
            self.order_items[product] = quantity

        if product.price is not None:
            self.total += product.price * quantity
            self.total = round(self.total, 2)

        #   ---------------Statistical operations----------
        #   Count total number of products
        product.total_count += quantity

    #   Print current object's shopping cart
    def show_order_items(self):
        for k, v in self.order_items.items():
            print(k.name, v)




    

