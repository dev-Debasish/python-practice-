# for tuples

# we have to use the parameter name as (args)
def sum_all(*args):
    print(args)   # it returns tuple
    # it is an iterable obj. so,we have to print it using loop
    for i in args:
        print(2 * i)
    
    print(*args)    # it only returns the normal value that is in the args
    
    return sum(args)

# using (*args) we have to use this in the infinite no. of arguments... that is returns as tuple 
print(sum_all(1,2,4,3))
print(sum_all(1,2))
print(sum_all(1,2,3))


# ------------------------------------------------------------------------------


# for dictioanry ----->
# we have to use the parameter name as (kwargs)
def myDict(**kwargs):
    # to print the key-value pair we have to use the loop for the iteration of the key-value..
    for key, value in kwargs.items():
        print(f"{key} : {value}")
        

# using the (**kwargs) we use the multiple key-value arguments in the function call...
myDict(name = "debasish", age = 21)
print()
myDict(name = "debasish", age = 21, love = "sports", like = "anime")
print()
myDict(name = "debasish", age = 21, city = "midnapore(WEST)")



#! ================= #? ---------------------------- #*^^^^^^^^^^^^^^^^^^^^^^^^^^
# ================================================================
# factory function // closure // function upon function .....


def f1(num):
    def f2(x):
        return x ** num
    return f2

# return keyword not only return the value but also return the full reference of the variable as well as the function itself.. 
a = f1(3)
b = f1(2)

# In this program the f1() function return the value as well as the reference of the another function f2()... 
print(a)
print(b) 
#? while we use the variable[a, b] as function... to print the exact answer..
print(a(3))    # cube
print(b(3))    # square


# ===============================================================================