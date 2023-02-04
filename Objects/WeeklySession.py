from .Customer import *

class WeeklySession:
    def __init__(self):
        self.customerDict: dict[str, Customer] = {}
        self.productDict: dict[str, Product] = {}
        self.filepath =  ""
    
    def addProduct(self, product: Product):
        self.productDict[product.name] = product
    
    def addCustomer(self, customer: Customer):
        self.customerDict[customer.name] = customer

    def next(self, customerName: str,memo: str, productName: str, productPrice: float, quantity: float):
        # if the object is not None, then add it to the dict, otherwise find the obj in the dict
        if customerName not in self.customerDict:
            customer = Customer(customerName)
            self.addCustomer(customer)
        else:
            customer = self.customerDict[customerName]
        
        if productName not in self.productDict:
            product = Product(productName,productPrice)
            self.addProduct(product)
        else:
            product = self.productDict[productName]
        
        customer.memo = memo
        customer.buy(product, quantity)

    #   Calculates current runtime's total sale
    def getGrossSale(self) -> float:
        total = 0
        for v in self.productDict.values():
            total += v.price * v.totalCount
        return total
    
    #   Return a list with customer objects that the shopping cart total is greater than threshold
    def getDeliveryList(self, threshold: float = 120.0) -> list[Customer]:
        return [cx for cx in self.customerDict.values() if cx.shopList.total > threshold]