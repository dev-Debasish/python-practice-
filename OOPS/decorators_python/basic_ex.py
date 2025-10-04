def my_decorators(func):
    def wrapper():
        print("before!")
        func()   # call the original function
        print("After!")
    return wrapper

@my_decorators
def say_hello():
    print("Hello !!")
    
# call the decorated function 
say_hello()



#! Decorators with Arguments

def my_decorators(func):
    def wrapper(*args, **kwargs):
        print("before!")
        result = func(*args, **kwargs)   # pass the arguments to the original function
        print("After!")
        return result
    return wrapper

@my_decorators
def greet(name):
    return f'hello {name}!'
    
# call the decorated function 
print(greet("bittu"))