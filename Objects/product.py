class Product:
    def __init__(self, name: str, price: float, size = "Default", category = "Default"):
        self.name = name
        self.price = price
        self.size = size
        self.category = category
        self.availibility = True
        self.cost = 0
        self.total_count = 0

    def set_availibility(self, status: bool):
        self.availibility = status
    
    def set_cost(self, price: float):
        self.cost = price
    
    def set_price(self, price: float):
        self.price = price
    
    