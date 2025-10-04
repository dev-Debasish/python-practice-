class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
        
    def show_num(self):
        print(self.real, "+", self.img, "j")
    
    
    # this is the dunder function that is inbuild in python, which used as + operation....
    def __add__(self, num):
        newReal = self.real + num.real
        newImg = self.img + num.img
        return Complex(newReal, newImg)
    
num1 = Complex(4, 5)
num1.show_num()
num2 = Complex(3, 8)
num2.show_num()

# here we are not only used the method but also used the operator that reflects the + operation...
num3 = num1 + num2
num3.show_num()
