class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        
    def get_brand(self):
        return f"{self.__brand}"
        
    def display(self):
        return f"you have the {self.__brand}, and the model is {self.model}"
    
    
class ElectricCar(Car):
    def __init__(self,brand, model, battery_size):
        super().__init__(brand, model)
        # super().display()
        self.battery_size = battery_size


tesla = ElectricCar("Tesla", "CyberTrack","80kwh")
# print(tesla.__brand)
print(tesla.get_brand())
print(tesla.model)
print(tesla.battery_size)
print(tesla.display())


