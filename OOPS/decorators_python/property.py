class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        # self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"
        
    #! that works
    def calcPercentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

    #! another way
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"
        
        
s1 = Student(95, 92, 98)
# print(s1.percentage)
# print(s1.calcPercentage())

#**  by using property decorator we use the method as an attribute ...
print(s1.percentage)



s1.phy = 85
print("PHY = ", s1.phy)
# print(s1.percentage)
# print(s1.calcPercentage())

print(s1.percentage)