
'''
Why args[1:]?
In a class method, self is always the first argument (implicitly passed when you call s.say_hello()).
The decorator skips self in the log because it's not useful to see the object's memory address (e.g., <__main__.Student object at 0x...>). You care about the actual inputs like "Hello".

'''

def log_method(func):
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__} with args {args[1:]}")
        return func(*args, **kwargs)
    return wrapper

class Student:
    def __init__(self, name, fullname = None):
        self.name = name
        self.fullname = fullname if fullname else name
        

    @log_method
    def say_hello(self, greeting = "hi"):
        return f"{greeting}, I'm {self.fullname}!"

s = Student("Bittu")
print(s.say_hello())
print(s.say_hello("hello"))
    