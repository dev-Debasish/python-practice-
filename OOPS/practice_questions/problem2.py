class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
        
    def showDetails(self):
        print("ROLE = ", self.role)
        print("DEPT. = ", self.dept)
        print("SALARY = ", self.salary)
        

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # if you want to put the attribute name then you have to initialize it in the constructor first...
        super().__init__("Enginner", "IT", "80,000")
        

deb = Engineer("Debasish pal", 22)
deb.showDetails()
    