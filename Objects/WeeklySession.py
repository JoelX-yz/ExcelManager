from .Customer import *

class WeeklySession:
    def __init__(self):
        self.customerDict: dict[str, Customer] = {}
        self.productDict: dict[str, Product] = {}
    
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
        for k,v in self.productDict:
            total += v.price * v.number
        return total
    
    #   Return current runtime's comprehensive data
    def getAll(self) -> list:
        return [self.productList, self.getGrossSale()]
    
    #   Return a list with customer objects that the shopping cart total is greater than threshold
    def getDeliveryList(self, threshold: float = 120.0) -> list:
        return [cx for cx in self.customerList if cx.shopList.total > threshold]