class Product:
    def __init__(self, name: str, price: float, size = "Default", category = "Default"):
        self.name = name
        self.price = price
        self.size = size
        self.category = category
        self.availibility = True
        self.cost = 0
        self.totalCount = 0

    def setAvailibility(self, status: bool):
        self.availibility = status
    
    def setcost(self, price: float):
        self.cost = price
    
    def setPrice(self, price: float):
        self.price = price
    
    