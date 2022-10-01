class Product:
    def __init__(self, name, price, size = "Default", category = "Default"):
        self.name = name
        self.price = price
        self.size = size
        self.category = category
        self.availibility = True
        self.importPrice = 0
        self.count = 0