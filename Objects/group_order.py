from .customer import *

class GroupOrder:
    def __init__(self):
        self.all_customers: dict[str, Customer] = {}
        self.all_products: dict[str, Product] = {}
        self.filepath =  ""
    
    def add_product(self, product: Product):
        self.all_products[product.name] = product
    
    def add_customer(self, customer: Customer):
        self.all_customers[customer.name] = customer

    def add_order(self, customer_name: str, memo: str, 
                  product_name: str, product_price: float, quantity: float):
        # if the object is not None, add it to the dict,
        # otherwise find the obj in the dict
        if customer_name not in self.all_customers:
            customer = Customer(customer_name)
            self.add_customer(customer)
        else:
            customer = self.all_customers[customer_name]
        
        if product_name not in self.all_products:
            product = Product(product_name,product_price)
            self.add_product(product)
        else:
            product = self.all_products[product_name]
        
        if customer.memo == '':
            customer.memo = memo
            
        customer.add_to_cart(product, quantity)

    #   Calculates current runtime's total sale
    def calc_gross_revenue(self) -> float:
        total = 0

        for v in self.all_products.values():
            total += v.price * v.total_count
        return total
    
    #   Return a list with customer objects that the shopping cart total is greater than threshold
    def get_delivery_customer(self, threshold: float = 120.0) -> list[Customer]:
        return [cx for cx in self.all_customers.values() if cx.cart.total > threshold]