def upperCase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.upper()
        return result
    return wrapper

@upperCase
def greet(name):
    return f'hello, {name}!'

@upperCase
def say_bye(name, time):
    return f'Goodbye {name}, keep in {time} :)'

@upperCase
def add(a,b):
    return a+ b

print(greet("Bittu"))
print(say_bye("lipi", "touch"))
print(add(4, 5))


'''
def wrapper(*args, **kwargs):
    result = func(*args, **kwargs)
'''
#TODO:  [*args, **kwargs],,this is used for flexibility , here we can take any no. of arguments without modifying the original code .. and also handel the edge case if the argument is not String what happens/!!

