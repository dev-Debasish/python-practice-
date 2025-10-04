# TODO: global and local scope

def myFunction():
    global x
    x = 300
    
myFunction()
print(x)


#?  if you are using the [global] keyword then its priority is grater than the global veriable that you used in outside...




# TODO:  the [nonlocal] keyword

# The nonlocal keyword is used to work with variables inside nested functions.

# The nonlocal keyword makes the variable belong to the outer function.

def myfunc1():
    x = "bittu"
    def mufunc2():
        nonlocal x
        x = "radhe radhe"
    mufunc2()
    return x

print(myfunc1())