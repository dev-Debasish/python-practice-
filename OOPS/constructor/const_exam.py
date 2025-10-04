'''
Defines a Student class with attributes name, age, and hobbies (a list).
Adds a method list_hobbies that prints each hobby in the list with a message like "I like to [hobby]."
Creates a Student object with your own info and calls the list_hobbies method.
'''

class Student:
    def __init__(self, name, age, hobbies):
        self.name = name
        self.age = age
        self.hobbies = hobbies
        
    def list_hobbies(self):
        for hobby in self.hobbies:
            print(f"I like to {hobby}")
            

me = Student("Debasish", 21, ["Coding", "photoGraphy", "Exercise"])
me.list_hobbies()