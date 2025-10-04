
# without __str__():

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)


#? The __str__() function controls what should be returned when the class object is represented as a string.

# with __str__():

class Person:
    def __init__(self, name, age):
       self.name = name
       self.age = age
       
    def __str__(self):
        return f'{self.name}({self.age})'
    

p1 = Person("Bittu", 21)
print(p1)
