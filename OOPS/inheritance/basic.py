class Car:
    color = "Black"
    @staticmethod
    def start():
        print("car started....")
        
    @staticmethod
    def stop():
        print("car stopped...")
        

class BMW(Car):
    def __init__(self, model):
        self.model = model
    
m5 = BMW("competition")

m5.start()
print(m5.model)

# as color is the class variable of Car class, it can be accessed using the instance of BMW class
# and also using the class name & the object name also
print(m5.color)
print(Car.color)
print(BMW.color)

m5.stop()