#  classmethod is bound to the class & receives the class as an implicit class arguments
#? staticmethod can't access or modify class state, it is generally used for utility

class Person:
    name = "kds"
    
    def changeName(self, name):
        self.name = name
        
p1 = Person()
p1.changeName("Bittu")
print(p1.name)
print(Person.name)

# First, we create the class attribute [name] and later we want to change the value of the class attribute that's why we create a method changeName() , but it can't do that ...as in the changeName() method it is create an another attr. name and change the value of it.. it doesn't effect the main class attr. 

# to do this >>>> one method is --->
class Person:
    name = "kds"
    
    def changeName(self, name):
        # Person.name = name
        #! or.
        self.__class__.name = name
        
p1 = Person()
p1.changeName("Bittu")
print(p1.name)
print(Person.name)


# another approach --->
class Person:
    name = "kds"
    
    @classmethod
    # def changeName(self, name):
    #     self.name = name
    #! we are doing the same as before by only using the @staticmethod decorator
    # as it is the [classmethod] so, we used {cls} inplace of {self}
    def changeName(cls, name):
        cls.name = name
    #  although it is the same approach,,as we know that usually we use anything in the place of self..it is also work as self ...so, nothing matters
        
p1 = Person()
p1.changeName("Bittu")
print(p1.name)
print(Person.name)


