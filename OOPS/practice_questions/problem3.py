class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
        
    def __gt__(self, ordr):
        return self.price > ordr.price
    

ordr1 = Order("Lays", 20)
ordr2 = Order("Kurkure", 15)

print(ordr1 > ordr2)
