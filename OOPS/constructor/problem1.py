class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def get_avg(self):
        sum = 0
        for mark in self.marks:
            sum += mark
        print(f'hi {self.name}, Your AVG maks is {sum/3}')
        
deb = Student("Debasish Pal", [97, 98, 96])
deb.get_avg()

deb.name = "Bittu Pal"   # modify obj property
deb.marks = [93, 98, 88]
deb.get_avg()

