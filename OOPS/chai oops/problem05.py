class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        
    def get_brand(self):
        return f"{self.__brand}"
    
    @staticmethod    
    def fuel_type():
        return "petrol or.Diesel"
    
    
    
class ElectricCar(Car):
    def __init__(self,brand, model, battery_size):
        super().__init__(brand, model)
        # super().display()
        self.battery_size = battery_size
        
    @staticmethod    
    def fuel_type():
        return "Eletric Charge"


tesla = ElectricCar("Tesla", "CyberTrack","80kwh")
print(tesla.fuel_type())
print(ElectricCar.fuel_type())

porsha = Car("Porsha", "GT3-RS")
print(porsha.fuel_type())
print(Car.fuel_type())


