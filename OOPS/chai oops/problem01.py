class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def display(self):
        return f"you have the {self.brand}, and the model is {self.model}"
    
    
class ElectricCar(Car):
    def __init__(self,brand, model, battery_size):
        super().__init__(brand, model)
        # super().display()
        self.battery_size = battery_size
        
        
    
       
# porsha = Car("Porsha", "GT3-RS")
# print(porsha.brand)
# print(porsha.model)
# print(porsha.display())


tesla = ElectricCar("Tesla", "CyberTrack","80kwh")
print(tesla.brand)
print(tesla.model)
print(tesla.battery_size)
print(tesla.display())


