# class Car:
#     color = "Black"
#     @staticmethod
#     def start():
#         print("car started....")
        
#     @staticmethod
#     def stop():
#         print("car stopped...")
        

# class BMW(Car):
#     def __init__(self, model):
#         self.model = model
        

# class sports(BMW):
#     def __init__(self, type):
#         # make changes in here
#         # output is later explained
#         self.type = type
        

# car1 = sports("petrol")

# print(car1.type)
# print(car1.color)
# car1.start()
# car1.stop()

# ------------------------------------------------------------------------------------------
# ? explanation ---> 

'''
as class sports is inherited from the class BMW . so how could class sports access the model attribute of the class BMW into the class sports..
may it be --> car1.model or what?

'''
#! ------>>
'''
Your current sports class does not correctly inherit attributes from BMW because the constructor (__init__ method) in sports overrides the constructor of BMW without calling super().__init__(). This means that the model attribute from BMW is never initialized in sports.
'''
'''
To ensure that the model attribute is properly inherited and accessible in sports, you should update the __init__ method in sports to call the constructor of BMW. Here's the corrected code:
'''

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


class Sports(BMW):
    def __init__(self, model, type):
        super().__init__(model)  # Call the constructor of BMW to initialize model
        self.type = type  # Initialize type attribute
        super().start()


#?  when we creat the object of a class the constructor is automatically called,,,although in the output we are not called the start method but we are initialized in the Sports class so, it is called automatically called whenever the constructor is called....
# Creating an instance of Sports
car1 = Sports("M5", "Petrol")

print(car1.type)  # Output: Petrol
print(car1.model)  # Output: M5
print(car1.color)  # Output: Black (Inherited from Car)
# car1.start()  # Output: car started....
car1.stop()  # Output: car stopped...


'''
Key Fixes and Explanation:
Calling super().__init__(model) inside Sports.__init__()

This ensures that the model attribute from BMW is correctly initialized.
Passing model as an argument to Sports

Since BMW requires model as an argument, Sports must also accept it.
Accessing model Attribute

Now, car1.model works correctly because model is properly inherited from BMW.
'''

'''
Key Takeaways:
When overriding __init__() in a subclass, always call super().__init__() if the parent class has an __init__() method.
super().__init__(args...) ensures that the parent class attributes are properly initialized.
Without calling super().__init__(), the attributes of the parent class won't be available in the child class.
'''

