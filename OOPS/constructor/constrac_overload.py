
#! in general, python doesn't support constructor overloading ... but we can do it 

#? <<   Constructor overloading is when a class has multiple constructors (special methods that initialize objects) with different parameter lists. This lets you create objects in different ways depending on what data you provide. It’s common in languages like Java or C++, where you define multiple versions of the constructor explicitly.  >>

# Python doesn’t support constructor overloading directly because it doesn’t allow multiple methods with the same name (like __init__) distinguished only by parameters. Instead, Python uses a single __init__ method and handles flexibility with techniques like default arguments, variable-length arguments (*args, **kwargs), or conditional logic. Let’s explore this with examples!


class Student:
    def __init__(self, name, age = 21):
        self.name = name 
        self.age = age
        

s1 = Student("Bittu")
s2 = Student("Debasish", 23)

print(s1.name, s1.age)
print(s2.name, s2.age)



#!  Example 2: Using **kwargs for More Flexibility
'''
class Student:
    def __init__(self, name, **kwargs):
        self.name = name
        self.age = kwargs.get("age", 0)      # Default to 0 if age not provided
        self.hobbies = kwargs.get("hobbies", [])  # Default to empty list

# Different ways to create objects
s1 = Student("Bittu")                     # Just name
s2 = Student("Deb", age=20)               # Name and age
s3 = Student("Abhi", age=22, hobbies=["code", "music"])  # Name, age, hobbies

print(s1.name, s1.age, s1.hobbies)        # Prints: Bittu 0 []
print(s2.name, s2.age, s2.hobbies)        # Prints: Deb 20 []
print(s3.name, s3.age, s3.hobbies)        # Prints: Abhi 22 ['code', 'music']

'''


#! Example 3: Conditional Logic
'''
class Student:
    def __init__(self, name, extra=None):
        self.name = name
        if extra is None:
            self.age = 0
            self.hobbies = []
        elif isinstance(extra, int):
            self.age = extra
            self.hobbies = []
        elif isinstance(extra, list):
            self.age = 0
            self.hobbies = extra

# Different ways to create objects
s1 = Student("Bittu")             # Just name
s2 = Student("Deb", 20)           # Name and age
s3 = Student("Abhi", ["code"])    # Name and hobbies

print(s1.name, s1.age, s1.hobbies)  # Prints: Bittu 0 []
print(s2.name, s2.age, s2.hobbies)  # Prints: Deb 20 []
print(s3.name, s3.age, s3.hobbies)  # Prints: Abhi 0 ['code']

'''



