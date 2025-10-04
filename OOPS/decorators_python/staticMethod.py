
# staticmethod are the methods that don't use the self parameter (work at class level)

# decoretors allow us to wrap another function in order to extend the behavior of the wrapped function, without parmanently modifying it..

'''
A decorator is a function that takes another function as an argument, adds some functionality to it, and returns a new function. Think of it as "wrapping" a function with extra behavior. In Python, decorators are marked with the @ symbol above a function definition.
''' 


#? in general decorators are the function that takes function as parameter and returns function as output...

class Student:
    def __init__(self, name):
        self.name = name
    
    @staticmethod   
    def hello():
        print("hello")
        

me = Student("Debasish Pal")
print(me.name)
me.hello()