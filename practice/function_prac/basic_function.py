def myFunction():
    print("hello, from function !")

myFunction()
# -------------------------------------------------------------------
def name(fname):
    print("hello",fname)
    print("hello" + fname)

name("bittu")
# -------------------------------------------------------------------
# Arbitrary Arguments, *args
# If the number of arguments is unknown, add a * before the parameter name
# tuples
def kidsName(*kids):
    print("The name of the kids are: ",kids)  # returns a tuple
    print("The eldest child is: ",kids[2])    # debasish

kidsName("bittu", "abhi", "debasish")
# -------------------------------------------------------------------
# Arbitrary Keyword Arguments, **kwargs
# If the number of keyword arguments is unknown, add a double ** before the parameter name:
# dictionary
def kids(**kid):
    print("His Title is: ",kid["lname"])

kids(lname = "Pal", fname = "Debasish")
# -------------------------------------------------------------------
def myFunction(x):
    return 5 * x

print(myFunction(5))
print(myFunction(6))
print(myFunction(8))
# -------------------------------------------------------------------
'''
Positional-Only Arguments
You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.

To specify that a function can have only positional arguments, add [, /] after the arguments:
'''
def myFunc(x,/):
    print(x)

myFunc(5)

'''
Without the [, /] you are actually allowed to use keyword arguments even if the function expects positional arguments:
'''
def my_function(x):
  print(x)

my_function(x = 3)

'''
But when adding the [, /] you will get an error if you try to send a keyword argument:
'''
# def my_function(x, /):
#   print(x)

# my_function(x = 3)

'''
Traceback (most recent call last):
  File "./prog.py", line 4, in <module>
TypeError: my_function() got some positional-only arguments passed as keyword arguments: 'x'
'''
# -------------------------------------------------------------------
'''
Keyword-Only Arguments
To specify that a function can have only keyword arguments, add [*,] before the arguments:
'''
def my_function(*, x):
  print(x)

my_function(x = 3)
'''
Without the [*,] you are allowed to use positionale arguments even if the function expects keyword arguments:
'''
def my_function(x):
  print(x)

my_function(3)
'''
But with the [*,] you will get an error if you try to send a positional argument:
'''
# def my_function(*, x):
#   print(x)

# my_function(3)
'''
Traceback (most recent call last):
  File "./prog.py", line 4, in <module>
TypeError: my_function() takes 0 positional arguments but 1 was given
'''
# -------------------------------------------------------------------
'''
Combine Positional-Only and Keyword-Only
You can combine the two argument types in the same function.

Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
'''
def myFunc(a,b,/,*,c,d):
   print(a+b+c+d)

myFunc(5, 6, c = 7, d = 8)

# ! every print statement returns [None] type

