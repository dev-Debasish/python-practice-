def average(a=9,b=6):
    count = (a+b)/2
    print(count)

average(4,5)     #------->required argument
average()  # ----> default argument

# instead of assigning the value of a and b in the function parameters & the time of point the value on the function call we need not to be assigned the value as ----> DEFAULT ARGUMENTS.

# in the case of REQUIRED ARGUMENTS we need to be assigned the value of the paramaters at the time of function call as we did not assigned the value of the parameters when defining the funtion it throws an error

# if we assigned the value at the time of function call & the function defination here the function defination is not decleared the function called value are decleared....

# KEYWORDS ARGUMENTS
def name(fname,lname):
    print(fname,lname)

name(lname = "pal",fname = "bittu")

# ARBITARY ARGUMENTS

# using tuples

def avg(*numbers):
    sum = 0
    for i in numbers:
        sum = sum+i
    print("The averagee is: ",sum/len(numbers))

avg(10,15,25,56)

# using dictionary

def name(**name):
    print(name["fname"],name["lname"])

name(fname = "debasish",lname = "pal")