# for defining a function we have to declear {def} before giving the name of that function...


#                            REQUIRED ARGUMENTS
#  in required args: we don't have to define the value of the args in the func: defination section 
def gMean(a, b):     # here (a, b) are the parameters
    # print("The gMean of the 2 numbers are: ",(a * b) / (a + b))
    result = (a * b) / (a + b)
    return result

# gMean(4, 5)
c = gMean(10, 2)    # required arguments
print(c)


#                            DEFAULT ARGUMENTS
# these args are the default args: as it's values are define before the function call .
# in default args: if we put the values of the args: in the function call section, it pefers it most .
def avg(c = 10, d = 5):    # default args: 
    print("the Average of the numbers is: ",(c + d) / 2)

avg()
avg(10, 12)
avg(15)
avg(d = 9)      # work as keyword arguments


#                            KEYWORD ARGUMENTS
# In keyword arguments we have to define the args: as the user want but 
# todo: {we have to declear the keyword of that at the function call}.

avg(d = 4, c = 12)
avg(d = 4,)
avg(c = 12)

# ----------------------------------------------------------------------------------
def my_function():
    pass
# ----------------------------------------------------------------------------------

#                            Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

# E.g. if you send a List as an argument, it will still be a List when it reaches the function:
def func(foods):
    for food in foods:
        print(food)

fruits = ["apple", "orange", "avocardo", "kiwi"]

func(fruits)

# 