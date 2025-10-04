class Car:
    call = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.call += 1
        
    def get_brand(self):
        return f"{self.__brand}"
    
    
    
Car("Porsha", "GT3-RS")
Car("M5", "Competition")

# print(Car.mro())
print(Car.call)
