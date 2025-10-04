
# private attribute can be accessed only within the class, not outside the class

class Person:
    __name = "Debasish"  # it the private arrtibute 
    
    def __hello(self):
        print("hello :>", self.__name)
        
    def welcome(self):
        self.__hello()
        
p1 = Person()

#? it throws an error as __name is private attribute
# print(p1.__name)
# p1.__hello()

#* here the welcome() fuc. is not the private method but it returns the private method called __hello() 
# only through this we can access the private attributes as well as the private method in python
p1.welcome()
