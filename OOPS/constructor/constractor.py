

# in the previous program we are not created any constractor (__init__) but the class is still runs .. that is if you are not created any constractor .. the python interpreter automatically created the (__init__) function to run the program .. but you can not see it ...

# but we created it by our own 

class Student:
    fullName = "Bittu Pal"
    
    #*  in general, we are create only one constructor .. as python doesn't support different constructor or. constructor overloading..
    # default constractor
    # def __init__(self):
    #     pass
    
    #?  obj attr > class attr
    
    # parametarized constractor
    def __init__(self, name, age):
        # print(self)
        self.name = name
        self.age = age
        # print("Constractor is called automatically whenever class is invoked...")
        
    def welcome(self):
        print(f"hello, {self.name}")
        
    def get_age(self):
        return self.age
        
          

deb = Student("Debasish Pal", 21) 
print(deb.name)    
print(deb.fullName)
deb.welcome()
print(deb.get_age())

# me = Student()  

abhi = Student("Abhi pal", 23)
print(abhi.name)
print(abhi.fullName)
abhi.welcome()
print(abhi.get_age())

# since fullname is the class variable so, we can print it by using the class name itself
# so, here we don't have to create any obj of this...
print(Student.fullName)


# ----------------------------------------------------------------------------------

class Car:
    pass

class New:
    def __init__(self,atr1):
        self.atr1 = atr1
        
x = New(45)
print(x.atr1)

# delete obj property
del x.atr1

# print(x.atr1)

# delete obj
del x