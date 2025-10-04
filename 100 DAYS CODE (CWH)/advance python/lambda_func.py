# lambda function is the annonymous function that is generally used instead of function ..... that is basically the one-Liner mode of a function that we are directly used in the code instead of using the function..
#?  lambda argument : expression

# first write the function that doubles the input
def double(x):
    return x * 2

print(double(8))

# instead of using this we used the lambda function to do the same task in one list .... that improves the code readability....
double = lambda x : x * 2
cube = lambda y : y * y * y
avg = lambda x, y : (x + y) / 2
print(double(5))
print(cube(5))
print(avg(8, 12))


# you can also use the lambda function inside a function
def appl(fx, val):
    return 6 + fx(val)

print(appl(lambda x : x * x , 2))




#!  The power of lambda is better shown when you use them as an anonymous function inside another function.

def myFunction(x):
    return lambda a : a * x

doubler = myFunction(2)
tripler = myFunction(3)

print(doubler(12))
print(tripler(12))

