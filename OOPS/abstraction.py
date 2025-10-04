# TODO:   grok example findout for [ABSTRACTION]

# hiding the implementation details of the class and only showing the essential features to the user.

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
        
    def start(self):
        self.acc = True
        self.clutch = True
        print("car started..")
        
    def stop(self):
        self.brk = True
        self.acc = False
        self.clutch = False
        print("car Stopped...")
        
bmw = Car()
bmw.start()
bmw.stop()

# in this program we show the essential details about the car that shows the car is started and stopped but we are not shown the internal details of the car that how car is started and how the car is stopped... this is called the abstraction..>

